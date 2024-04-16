"""
TFV Accessor module to add functionality to native xarray

A Waterhouse

This module provides "meta" functions to access, analyse and plot TUFLOW FV result files, based around underlying Xarray datasets.
The intention of this module is to replace the use of the individual function calls by providing convienent "one-stop shop" methods.
"""

from inspect import getdoc
from pathlib import Path
import re
import xarray as xr

from tqdm import tqdm
from typing import Union, Literal
import matplotlib
from matplotlib.path import Path as mpath
from matplotlib.ticker import FormatStrFormatter
from scipy.spatial import Delaunay
from scipy.interpolate import LinearNDInterpolator, CloughTocher2DInterpolator

from tfv.miscellaneous import *
from tfv.extractor import FvExtractor, _strip_dataset
from tfv.timeseries import FvTimeSeries
from tfv.visual import *
from tfv._grid_to_tfv import grid_remap

import warnings


def read_tfv(file: Union[str, Path, list], restype="auto"):
    try:
        ds = FvExtractor(file).ds
    except TypeError:
        print("Data does not appear to be a valid TUFLOW FV spatial netcdf file")
    return ds


def _pipe_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper


def _check_tfv_type(ds):
    atype = ds.attrs.get("Type", "")
    atype = atype.lower()

    if (atype == "cell-centred tuflowfv output") | ("NumCells2D" in ds.dims):
        restype = "domain"

    elif atype == "curtain tuflowfv output":
        restype = "curtain"

    elif atype in ["tuflowfv profile output", "profile cell from tuflowfv output"]:
        restype = "timeseries"

    else:
        restype = "unknown"

    return restype


@xr.register_dataset_accessor("tfv")
class TfvAccessor:
    def __init__(self, xarray_obj):
        self._obj = xarray_obj
        self.restype = _check_tfv_type(xarray_obj)

        if self.restype == "domain":
            self._tfv = TfvDomain(self._obj)

        elif self.restype == "curtain":
            raise NotImplementedError

        elif self.restype == "timeseries":
            self._tfv = TfvTimeseries(self._obj)

        # Register functions from the appropriate module
        for x in dir(self._tfv):
            if x.startswith("_") is False:
                setattr(self, x, getattr(self._tfv, x))

    def __getattr__(self, item):
        # To prevent breaking in-built funcs (e.g., _repr...)
        if item.startswith("_"):
            raise AttributeError(item)

        result = getattr(self._obj, item)

        # Run function, if applicable
        if callable(result):
            result = _pipe_call(result)

        return result

    def __getitem__(self, item):
        result = self._obj[item]
        return result

    def __setitem__(self, item, value):
        self._obj[item] = value

    def _repr_html_(self):
        return self._tfv._repr_html_()

    def __repr__(self):
        return self._tfv.__repr__()


class TfvBase:
    def __init__(self, xarray_obj):
        self._obj = xarray_obj
        self.geo_coords = []

    def __getitem__(self, item):
        result = self._obj[item]
        return result

    def __setitem__(self, item, value):
        self._obj[item] = value

    def _getvar_(self, variable, skip=[]):
        try:
            # Take first variable if not specified
            if variable is None:
                for k, v in self.variables.items():
                    if k not in skip:
                        variable = k
                        attrs = v
                        break
            if variable == "V":
                attrs = {"long_name": "current speed", "units": "m s^-1"}
            elif variable == "VDir":
                attrs = {"long_name": "current direction", "units": "degN TO"}
            elif variable.split("Dir")[0] in self.vector_variables:
                if "Dir" in variable:
                    v = self.vector_variables[variable.split("Dir")[0]]
                    ln = f"direction `{v[0]}` & `{v[1]}`"
                    attrs = {"long_name": "direction", "units": "degN TO"}
                else:
                    v = self.vector_variables[variable]
                    try:
                        units = self.variables[v[0]]["unit"]
                    except:
                        units = ""
                    ln = f"magnitude `{v[0]}` & `{v[1]}`"
                    attrs = {"long_name": ln, "units": units}

            elif (variable == "Zb") | (variable == "cell_Zb"):
                # cell Zb doesn't have time dim, and hence will need to be expanded to work with tfv.plot
                variable = "Zb"
                attrs = self._obj["cell_Zb"].attrs

            else:
                attrs = self.variables[variable]

            if ("long_name" in attrs) & ("units" in attrs):
                label = f"{attrs['long_name']} ({attrs['units']})"
            else:
                label = f"{variable} ( - )"
        except AttributeError:
            print(
                "Specified time is not clear - supply Datetime, str date (in ISO format) or integer"
            )
        return variable, label

    def _getattr_(self, variable):
        if variable in self.variables:
            attrs = self.variables[variable]
        elif variable == "V":
            attrs = {"long_name": "current speed", "units": "m s^-1"}
        elif variable == "VDir":
            attrs = {"long_name": "current direction", "units": "degN TO"}
        elif variable.split("Dir")[0] in self.vector_variables:
            if "Dir" in variable:
                v = self.vector_variables[variable.split("Dir")[0]]
                ln = f"direction `{v[0]}` & `{v[1]}`"
                attrs = {"long_name": "direction", "units": "degN TO"}
            else:
                v = self.vector_variables[variable]
                try:
                    units = self.variables[v[0]]["units"]
                except:
                    units = ""
                ln = f"magnitude `{v[0]}` & `{v[1]}`"
                attrs = {"long_name": ln, "units": units}
        else:
            attrs = {"long_name": "", "units": ""}

        return attrs

    @property
    def dims(self):
        return self._obj.dims

    @property
    def sizes(self):
        return self._obj.sizes

    @property
    def data_vars(self):
        return self._obj.drop_vars(self.geo_coords).data_vars

    @property
    def variables(self):
        return {
            k: v.attrs
            for k, v in self.data_vars.items()
            if k not in ["ResTime", "stat", "layerface_Z"]
        }

    @property
    def vector_variables(self):
        vecvar_map = {}
        for var in self.variables:
            if var[-2:] == "_x":
                basevar = var[:-2]
                if basevar + "_y" in self.variables:
                    vecvar_map[basevar] = (basevar + "_x", basevar + "_y")
        return vecvar_map

    def sel(self, *args, **kwargs):
        """pipe sel back through to the tfv object"""
        subset = self._obj.sel(*args, **kwargs)
        tvar = list(self.data_vars.keys())
        if "Time" not in subset.dims:
            subset[tvar] = subset[tvar].expand_dims("Time")
        return subset.tfv

    def isel(self, *args, **kwargs):
        """pipe sel back through to the tfv object"""
        subset = self._obj.isel(*args, **kwargs)
        tvar = list(self.data_vars.keys())
        if "Time" not in subset.dims:
            subset[tvar] = subset[tvar].expand_dims("Time")
        return subset.tfv

    def to_netcdf(self, *args, **kwargs):
        """Writes NETCDF result"""
        self._obj.to_netcdf(*args, **kwargs)


class TfvDomain(TfvBase):
    """Xarray accessor object for working with TUFLOW FV domain (spatial) netcdf files.

    Extends the functionality of native xarray to add methods that assist with typical analyses.

    To use this, call `.tfv` on an xarray dataset based on a TUFLOW FV domain file.
    """

    def __init__(self, xarray_obj):
        TfvBase.__init__(self, xarray_obj)
        self.xtr = None
        self.__load_tfv_domain()

    def __repr__(self):
        if is_notebook() is False:
            return self._obj.drop_vars(self.geo_coords).__repr__()
        else:
            return "TUFLOW FV domain xarray accessor object"

    def _repr_html_(self):
        from IPython.display import display

        return display(self._obj.drop_vars(self.geo_coords))

    def __convert_coords__(self):
        """Promote tfv geometry to coordinates"""
        ds = self._obj

        # Copy all geo variables into coordinates:
        self.geo = {}
        for dv in ds.data_vars.keys():
            if "Time" not in ds[dv].dims:
                if dv in ["idx2", "idx3"]:
                    self.geo[dv] = ds[dv].values - 1
                else:
                    self.geo[dv] = ds[dv].values

        # self._obj = ds.drop([c for c in self.geo.keys()])
        self.geo_coords = [c for c in self.geo.keys()]

    def __load_tfv_domain(self):
        if self.xtr is None:
            try:
                self.xtr = FvExtractor(self._obj)
                self.__convert_coords__()
            except TypeError:
                print(
                    "Data does not appear to be a valid TUFLOW FV spatial netcdf file"
                )

    def get_cell_index(self, x, y):
        """Returns the cell index(s) containing coordinate(s) x and y.

        Multiple cell indexes will be returned using this command if x/y are 1D.

        Args:
            x (float): x-coordinate
            y (float): y-coordinate

        Returns:
            cell_index (int): index of corresponding cell containing coordinates (x,y)
        """
        return self.xtr.get_cell_index(x, y)
    

    def get_cell_inpolygon(self, polygon):
        """Returns the cell indexes inside a specified polygon.

        The polygon should be provided as either a 2D Numpy ndarray (i.e., Nx2 array), 
        or if the `Shapely` package is available, a WKT String polygon or shapely Polygon object can be provided.

        Args:
            polygon ([np.ndarray, str, shapely.geometry.Polygon]): A single polygon feature, provided as a 2D numpy array (Nx2).
                If `shapely` is available, polygon may also be provided as a wkt string, or a shapely Polygon feature.

        Returns:
            cell_indexes (np.ndarray): indexes of cells falling inside the provided polygon.
        """
        if isinstance(polygon, str):
            try:
                import shapely.wkt
            except:
                raise ImportError(
                    "`shapely` is required for converting a polygon WKT string. Please either install shapely, or provide the polygon as a Nx2 numpy array."
                )
            shp = shapely.wkt.loads(polygon)
            polygon = np.stack(shp.boundary.xy).T

        elif not isinstance(polygon, np.ndarray):
            try:
                from shapely.geometry import Polygon
            except:
                raise ValueError(
                    "Polygon should be an Nx2 numpy array or (if Shapely is available), a WKTString poylgon or Shapely `Polygon` object"
                )

            if isinstance(polygon, Polygon):
                polygon = np.stack(polygon.boundary.xy).T
            else:
                raise ValueError('Unrecognised `polygon`. Please provide either a numpy ndarray (Nx2), a WKTString Polygon, or a Shapely Polygon object')

        fv_cells = np.stack((self.xtr.cell_x, self.xtr.cell_y)).T
        indexes = mpath(polygon).contains_points(fv_cells)
        return np.where(indexes)[0]
    

    def get_sheet(
        self,
        variables: Union[str, list],
        time: Union[str, int, pd.Timestamp, slice] = None,
        datum: Literal["sigma", "height", "depth", "elevation"] = "sigma",
        limits: tuple = (0, 1),
        agg: Literal["min", "mean", "max"] = "mean",
    ):
        """Extract a 2D sheet timeseries

        General purpose method for extracting 2D sheet data from a TfvDomain object. This will handle dimension reduction of 3D variables (by default will average over the depth column, i.e., depth-averaged), as well as handling single or multiple timesteps or slices.

        Args:
            variables ([str, list]): variables to extract. ("V" or "VDir" may be requested if "V_x" and "V_y" are present)
            time ([str, pd.Timestamp, int, slice], optional): time indexer for extraction. Defaults to the entire dataset.
            datum (['sigma', 'height', 'depth', 'elevation'], optional): depth-averaging datum. Defaults to 'sigma'. Choose from `height`, `depth`, `elevation` or `sigma`.
            limits (tuple, optional): depth-averaging limits. Defaults to (0,1).
            agg (['min', 'mean', 'max'], optional): depth-averaging aggregation function. Defaults to 'mean'. Choose from `min`, `mean`, or `max`.

        Returns:
            TfvDomain: new TfvDomain object with the requested timeseries variables

        """
        # Use sliced xarray dataset
        xtr = self.xtr
        dsx = xtr._subset_dataset(time)

        times = dsx["Time"]
        ts = [xtr._timestep_index(t) for t in times.values]
        nt = times.shape[0]
        ns = dsx.sizes["NumCells2D"]

        # Check input
        if isinstance(variables, str):
            variables = [variables]

        # Init output array
        nv = len(variables)
        array = np.ma.zeros((nv, nt, ns))

        # Check if z_data is required.
        # Need to check that a "meta" variable (e.g., 'V') isn't being requested
        depth_int = False
        for v in variables:
            if v in self.variables:
                if "NumCells3D" in dsx[v].dims:
                    depth_int = True

        c = 0
        z_data = None
        for t in tqdm(
            ts,
            desc="...extracting sheet data",
            colour="green",
            delay=1,
        ):
            if depth_int:
                z_data = xtr.get_integral_data(t, datum, limits)

            array[:, c, :] = xtr.get_sheet_cell(
                variables, t, datum, limits, agg=agg, z_data=z_data
            )
            c += 1

        dso = _strip_dataset(dsx.copy(deep=True))
        dims = ("Time", "NumCells2D")
        for v in variables:
            dso[v] = (dims, array[variables.index(v)])
            dso[v].attrs = self._getattr_(v)

        dso.attrs = self._obj.attrs

        return dso.tfv

    def get_statistics(
        self,
        stats: list[str],
        variables: Union[list, str],
        time: slice = None,
        datum: str = "sigma",
        limits: tuple = (0, 1),
        agg: str = "mean",
        fillna=None,
        skipna=True,
    ):
        """Extract statistics on 2D variables.

        General purpose method for extracting statistics using typical statistic functions (e.g., 'mean', 'max'...).

        Percentiles can be obtained using the string format 'pX' (e.g., for 10th and 90th: stats = ['p10', 'p90']).

        This function will first call `get_sheet` to obtain the data for calculating statistics on. All arguments for `get_sheet` can be passed through to this method.

        Args:
            stats (list[str]): list of statistics, e.g., ['min', 'mean', 'p50', 'p95']
            variables ([list, str]): variables to do statistics on
            time ([list, slice], optional): time indexer (e.g., slice(50) for the first 50 timesteps, or slice('2012-01-01', '2012-02-01'))
            datum (['sigma', 'height', 'depth', 'elevation'], optional): depth-averaging datum. Defaults to 'sigma'. Choose from `height`, `depth`, `elevation` or `sigma`.
            limits (tuple, optional): depth-averaging limits. Defaults to (0,1).
            agg (['min', 'mean', 'max'], optional): depth-averaging aggregation function. Defaults to 'mean'. Choose from `min`, `mean`, or `max`.
            fillna (float, optional): Fill nan values (e.g., dried out cells) with this value before doing statistics. Defaults to None.
            skipna (bool, optional): Skip nan values. Defaults to True.

        Returns:
            TfvDomain: new TfvDomain object with the requested timeseries variables

        """

        # Convert variable if provided as a singular string
        if isinstance(variables, str):
            variables = [variables]

        # BUG: Variables is being modified in-place by self.get_sheet
        # I don't know why, this is a quick-fix
        reqvars = variables.copy()

        # Convert stat variable if provided as a singular string
        if isinstance(stats, str):
            stats = [stats]

        # Check if data needs extracting (i.e., have I been chained?)
        extract = False
        for v in variables:
            # Unfortunate check because of virtual variables ('V', 'VDir')
            if v in self.variables:
                if "NumCells3D" in self[v].dims:
                    extract = True
            else:
                extract = True

        # Extract data, if required (yes I've been chained)
        if extract:
            ds_2d = self.get_sheet(reqvars, time, datum, limits, agg)
        else:
            ds_2d = self

        if fillna:
            ds_2d = ds_2d.fillna(fillna)

        # Prep output dataset (blank, Time == 1)
        dso = _strip_dataset(self._obj.isel(Time=[0]))

        # Process the requested statistics
        funcs = []
        quantiles = []
        for x in stats:
            if re.match(r"p\d+", x):
                quantiles.append(float(re.findall(r"[-+]?(?:\d*\.*\d+)", x)[0]) / 100)
            else:
                funcs.append(x)

        # Run functions
        # Supress all-nan slice warning here - this is common for TFV outputs!
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", r"All-NaN (slice|axis) encountered")

            # Run built-in xarray functions
            for f in funcs:
                for v in variables:
                    vname = f"{v}_{f}"
                    try:
                        func = getattr(ds_2d[v], f)
                        dso[vname] = func(dim="Time", skipna=skipna).expand_dims("Time")
                        dso[vname].attrs = ds_2d[v].attrs
                        dso[vname].attrs["long_name"] = vname
                    except AttributeError:
                        print(
                            f"{f} is not supported - see xarray documentation for available functions"
                        )

            # Run quantiles (all in one)
            if len(quantiles) > 0:
                for v in variables:
                    qarr = ds_2d[v].quantile(quantiles, skipna=skipna, dim="Time")
                    for ii, q in enumerate(quantiles):
                        vname = f"{v}_p{q*100:n}"
                        dso[vname] = qarr.isel(quantile=ii).expand_dims("Time")
                        dso[vname].attrs = ds_2d[v].attrs
                        dso[vname].attrs["long_name"] = vname

        dso = dso.drop_vars("quantile", errors="ignore")
        dso.attrs = self._obj.attrs

        return dso.tfv

    def get_profile(
        self,
        point: Union[tuple, dict],
        time: slice = None,
        variables: list[str] = None,
    ):
        """Extract profile timeseries at a single location

        Simple method to extract a profile timeseries at a single location.
        This returns a native Xarray dataset, and does not have the methods available using the TfvTimeseries Xarray accessor.

        NOTE - This method does not currently support adding "meta" variables like "V" in lieu of hypot(V_x, V_y).

        Args:
            point ([tuple, dict]): Single location to extract profile as a tuple (X,Y) or dictionary dict(loc_01=(X,Y)).
            time ([str, pd.Timestamp, int, slice], optional): time indexer for extraction. Defaults to the entire dataset.
            variables (list[str], optional): List of variables. Defaults to all variables.

        Returns:
            xr.Dataset: a native Xarray dataset containing the profile timeseries.

        """
        # Subset time
        xtr = self.xtr
        if time is not None:
            dsx = xtr._subset_dataset(time)
        else:
            dsx = xtr._subset_dataset(slice(None))

        # Convert point argument
        if isinstance(point, dict):
            assert (
                len(point) == 1
            ), "Can only extract ONE profile at a time, please reduce locations to a single {name: (x, y)} format"
            name = list(point.keys())[0]
            point = point[name]
        else:
            name = "loc01"

        # Convert variables if required
        if isinstance(variables, tuple):
            variables = list(variables)
        elif variables is None:
            variables = list(self.variables.keys())

        evariables = []  # variables to assign
        vvariables = []  # variables to calc later
        for v in variables:
            if v in self.variables:
                evariables.append(v)
            # I haven't thought this deeply through - 'V' for 'VDir' etc. sho¨uld work?
            elif v[0] in self.vector_variables:
                vvariables.append(v)
                evariables.extend(self.vector_variables[v[0]])
            else:
                raise ValueError(f"Variable {v} not found in dataset - please check")
        evariables = np.unique(evariables).tolist()

        # Grab cell indicies
        i2 = xtr.get_cell_index(point[0], point[1])[0]
        i3 = np.where(self.xtr.idx2 == i2)[0]
        i4 = np.where(self.xtr.idx4 == i2)[0]
        if i2 == -999:
            print(f"WARNING: point '{name}' is outside of model domain")
        dsx = dsx.sel(NumCells2D=i2, NumCells3D=i3, NumLayerFaces3D=i4)

        # Refactor, this is yucky
        dsx = dsx.drop_vars(
            [
                "ResTime",
                "cell_Nvert",
                "NL",
                "cell_node",
                "cell_A",
                "node_X",
                "node_Y",
                "node_Zb",
                "idx2",
                "idx3",
                "node_NVC2",
                "node_cell2d_idx",
                "node_cell2d_weights",
            ],
            errors="ignore",
        )
        dsx = dsx.rename(
            dict(
                cell_X="X",
                cell_Y="Y",
                cell_Zb="Z",
                NumCells3D="NumLayers",
                NumLayerFaces3D="NumLayerFaces",
            )
        )

        dsx["Z"] = (
            ("Time", "NumLayers"),
            np.mean((dsx["layerface_Z"][:, :-1], dsx["layerface_Z"][:, 1:]), axis=0),
        )

        for var in dsx.data_vars.keys():
            if len(dsx[var].dims) == 1:
                dsx[var] = dsx[var].expand_dims(dim="N1", axis=1)

        # Add N1 dim to match TUFLOW-FV Output
        dsx["X"] = dsx["X"].expand_dims(dim="N1")
        dsx["Y"] = dsx["Y"].expand_dims(dim="N1")

        dsx.attrs["Loc. name"] = name
        dsx.attrs["Loc. coords"] = point
        dsx.attrs["Origin"] = (
            "Profile extracted from TUFLOWFV cell-centered output using `tfv` xarray accessor"
        )
        dsx.attrs["Type"] = "Profile cell from TUFLOWFV output"

        # Add back in the magic variables
        for v in vvariables:
            x = self.vector_variables[v[0]]

            if "Dir" in v:
                dsx[v] = (90 - np.arctan2(dsx[x[1]], dsx[x[0]]) * 180 / np.pi) % 360
            else:
                dsx[v] = np.hypot(dsx[x[0]], dsx[x[1]])
            dsx[v].attrs = self._getattr_(v)

        # re-order and only pull out the requested variables
        dsx = dsx[["X", "Y", "Z", "stat", "layerface_Z"] + variables]

        return dsx

    def get_longsection(
        self,
        polyline: np.ndarray,
        variables: Union[str, list],
        time: Union[str, int, pd.Timestamp, slice] = None,
        datum: Literal["sigma", "height", "depth", "elevation"] = "sigma",
        limits: tuple = (0, 1),
        agg: Literal["min", "mean", "max"] = "mean",
    ):
        """Get a 2D Longsection of model data

        Args:
            polyline (np.ndarray): a Nx2 array containing the X and Y coordinates to extract the curtain over.
            variables ([str, list]): single or list of variables to extract
            time ([str, pd.Timestamp, int, slice], optional): time indexer for extraction. Defaults to the entire dataset.
            datum (['sigma', 'height', 'depth', 'elevation'], optional): depth-averaging datum. Defaults to 'sigma'. Choose from `height`, `depth`, `elevation` or `sigma`.
            limits (tuple, optional): depth-averaging limits. Defaults to (0,1).
            agg (['min', 'mean', 'max'], optional): depth-averaging aggregation function. Defaults to 'mean'. Choose from `min`, `mean`, or `max`.
        """
        xtr = self.xtr

        polyline = _convert_polyline(polyline)
        dsx = xtr._subset_dataset(time)
        times = dsx["Time"]
        ts = [xtr._timestep_index(t) for t in times.values]

        # Get "2D curtain cell intersections"
        line_index, cell_idx3 = xtr.get_curtain_cell_index(polyline)
        geo = xtr.get_curtain_cell_geo(0, polyline)

        # cell idx3 includes cells  so now cast to find the 2D cell
        chainage = np.reshape(geo[0], (-1, 4))
        tmpstat = np.in1d(cell_idx3, xtr.idx3)
        cell_idx3 = cell_idx3[tmpstat]
        cell_idx2 = xtr.idx2[cell_idx3]
        chainage = chainage[tmpstat, :]
        chainage = 0.5 * (chainage[:, 0] + chainage[:, 1])

        x_data = xtr.get_intersection_data(polyline)

        # Get dims
        nc = chainage.shape[0]
        nt = times.shape[0]

        if isinstance(variables, str):
            variables = [variables]

        nv = len(variables)

        # Check if spherical
        if self._obj.attrs.get("Spherical", "true") == "true":
            unit = "decimal degrees"
        else:
            unit = "m"

        dstx = xr.Dataset(
            coords=dict(
                Time=(("Time",), times.values),
                Chainage=(("Chainage"), chainage),
            ),
            data_vars=dict(
                cell_X=(("Chainage"), np.mean((x_data[0][:-1], x_data[0][1:]), axis=0)),
                cell_Y=(("Chainage"), np.mean((x_data[1][:-1], x_data[1][1:]), axis=0)),
                cell_Zb=(("Chainage"), self.geo["cell_Zb"][cell_idx2]),
            ),
        )
        dstx["Chainage"].attrs = {"long_name": "chainage", "units": "m"}
        dstx["cell_X"].attrs = {
            "long_name": "Cell Centroid X-Coordinate",
            "units": unit,
        }
        dstx["cell_Y"].attrs = {
            "long_name": "Cell-Centroid Y-Coordinate",
            "units": unit,
        }
        dstx["cell_Zb"].attrs = {"long_name": "Cell Bed Elevation", "units": "m"}

        # Init variables
        for v in variables:
            dstx[v] = (("Time", "Chainage"), np.zeros((nt, nc)))
            dstx[v].attrs = self._getattr_(v)

        # Init output array
        array = np.ma.zeros((nv, nt, nc))
        c = 0
        for t in tqdm(
            ts,
            desc="...extracting longsection data",
            colour="green",
            delay=1,
        ):
            tmp = xtr.get_sheet_cell(variables, t, datum=datum, limits=limits, agg=agg)

            # Need to pad the first dimension because we'll index the 2nd dim.
            if len(variables) == 1:
                tmp = tmp[None, :]

            array[:, c, :] = tmp[:, cell_idx2]
            c += 1

        for v in variables:
            dstx[v].values = array[variables.index(v)]

        dstx.attrs = {
            "Origin": "Longsection extracted from TUFLOWFV Output",
            "Type": "Longsection TUFLOWFV output",
        }

        return dstx

    def get_curtain(
        self,
        polyline: np.ndarray,
        variables: Union[str, list],
        time: Union[str, int, pd.Timestamp, slice] = None,
    ):
        """Extract a 2D curtain timeseries, returned as an Xarray dataset.

        Note:
            This is a work-in-progress method, and is not directly used in any other methods currently.
            If you wish to view curtain plots, please use the `plot_curtain` or `plot_curtain_interactive` methods

        Args:
            polyline (np.ndarray): a Nx2 array containing the X and Y coordinates to extract the curtain over.
            variables ([str, list]): single or list of variables to extract
            time ([str, pd.Timestamp, int, slice], optional): time indexer for extraction. Defaults to the entire dataset.

        Returns:
            xr.Dataset: Xarray dataset object
        """
        xtr = self.xtr
        # Use sliced xarray dataset
        dsx = xtr._subset_dataset(time)
        times = dsx["Time"]
        ts = [xtr._timestep_index(t) for t in times.values]
        nt = times.shape[0]

        if isinstance(variables, str):
            variables = [variables]

        polyline = _convert_polyline(polyline)

        line_index, line_cell_3D = xtr.get_curtain_cell_index(polyline)
        nx, nz, tri = xtr.get_curtain_cell_geo(ts[0], polyline)
        x_data = xtr.get_intersection_data(polyline)
        ns = tri.shape[0]  # Num cell
        # print(x_data[2])

        cells_2d = x_data[2][x_data[2] >= 0]
        cell_X = self.geo["cell_X"][cells_2d]
        cell_Y = self.geo["cell_Y"][cells_2d]
        cell_Zb = self.geo["cell_Zb"][cells_2d]

        if self._obj.attrs.get("Spherical", "true") == "true":
            unit = "decimal degrees"
        elif self._obj.attrs.get("spherical", "true") == "true":
            unit = "decimal degrees"
        else:
            unit = "m"

        dstx = xr.Dataset(
            coords=dict(
                Time=(("Time",), times.values),
            ),
            data_vars=dict(
                node_X=(("NumVert1D"), x_data[0]),
                node_Y=(("NumVert1D"), x_data[1]),
                cell_X=(("NumCells1D"), cell_X),
                cell_Y=(("NumCells1D"), cell_Y),
                cell_Zb=(("NumCells1D"), cell_Zb),
                line_cells_2D=(("NumCells1D"), cells_2d),
                line_cells_3D=(("NumVert2D"), line_cell_3D),
                line_index=(("NumVert2D"), line_index),
                Chainage=(("NumVert2D", "MaxNumCellVert"), nx[tri]),
                Z=(("Time", "NumVert2D", "MaxNumCellVert"), np.zeros((nt, ns, 4))),
            ),
        )
        dstx["Chainage"].attrs = {"long_name": "chainage", "units": "m"}
        dstx["cell_X"].attrs = {
            "long_name": "Cell Centroid X-Coordinate",
            "units": unit,
        }
        dstx["cell_Y"].attrs = {
            "long_name": "Cell-Centroid Y-Coordinate",
            "units": unit,
        }
        dstx["cell_Zb"].attrs = {"long_name": "Cell Bed Elevation", "units": "m"}
        dstx["node_X"].attrs = {"long_name": "Node X-Coordinate", "units": unit}
        dstx["node_Y"].attrs = {"long_name": "Node Y-Coordinate", "units": unit}
        dstx["line_cells_2D"].attrs = {
            "long_name": "Cell-Centroid Y-Coordinate",
            "units": unit,
        }
        dstx["line_cells_3D"].attrs = {
            "long_name": "Cell-Centroid Y-Coordinate",
            "units": unit,
        }
        dstx["line_index"].attrs = {
            "long_name": "Cell-Centroid Y-Coordinate",
            "units": unit,
        }
        dstx["Z"].attrs = {"long_name": "elevation in water column", "units": "m"}

        # Init variables
        for v in variables:
            dstx[v] = (("Time", "NumVert2D"), np.zeros((nt, ns)))
            dstx[v].attrs = self._getattr_(v)

        # Add V/VDir methods
        requested_vars = variables.copy()
        if "V" in variables:
            variables.extend(["V_x", "V_y"])
            variables.pop(variables.index("V"))
        if "VDir" in variables:
            variables.extend(["V_x", "V_y"])
            variables.pop(variables.index("VDir"))
        variables = np.unique(variables).tolist()

        # Init output array
        nv = len(variables)
        array = np.ma.zeros((nv, nt, ns))

        c = 0
        for t in tqdm(
            ts,
            desc="...extracting sheet data",
            colour="green",
            delay=1,
        ):
            # Fetch elevation
            nx, nz, tri = xtr.get_curtain_cell_geo(ts[0], polyline)
            dstx["Z"][c, :] = nz[tri]

            array[:, c, :] = xtr.get_curtain_cell(variables, t, polyline)
            c += 1
        for v in requested_vars:
            if v == "V":
                vxi = variables.index("V_x")
                vyi = variables.index("V_y")
                arr = np.hypot(array[vxi], array[vyi])
                dstx[v].values = arr

            elif v == "VDir":
                vxi = variables.index("V_x")
                vyi = variables.index("V_y")
                arr = (90 - np.arctan2(array[vyi], array[vxi]) * 180 / np.pi) % 360
                dstx[v].values = arr

            else:
                dstx[v].values = array[variables.index(v)]

        dstx.attrs = {
            "Origin": "Curtain extracted from TUFLOWFV Output",
            "Type": "Curtain TUFLOWFV output",
        }

        return dstx

    def get_timeseries(
        self,
        variables: Union[str, list],
        points: Union[tuple, dict],
        time: Union[str, int, pd.Timestamp, slice] = None,
        datum: Literal["sigma", "height", "depth", "elevation"] = "sigma",
        limits: tuple = (0, 1),
        agg: Literal["min", "mean", "max"] = "mean",
    ):
        """Get timeseries at point location(s) in the model

        Args:
            variables ([str, list]): variables to extract.
            points ([tuple, dict]): locations to extract (e.g., a tuple (x,y) or a dict {'name': (x,y), ...})
            time ([str, pd.Timestamp, int, slice], optional): time indexer for extraction. Defaults to the entire dataset.
            datum (['sigma', 'height', 'depth', 'elevation'], optional): depth-averaging datum. Defaults to 'sigma'. Choose from `height`, `depth`, `elevation` or `sigma`.
            limits (tuple, optional): depth-averaging limits. Defaults to (0,1).
            agg (['min', 'mean', 'max'], optional): depth-averaging aggregation function. Defaults to 'mean'. Choose from `min`, `mean`, or `max`.

        Returns:
            xr.Dataset: A timeseries dataset in xarray format
        """
        # Use sliced xarray dataset
        dsx = self.xtr._subset_dataset(time)

        if isinstance(variables, str):
            variables = [variables]

        # Get 2D cell index
        if isinstance(points, dict):
            index = []
            for pt in points.values():
                index.append(self.xtr.get_cell_index(pt[0], pt[1]).item())
            if len(points) == 1:
                pt = list(points.values())[0]
                index = self.xtr.get_cell_index(pt[0], pt[1])
                points = pt
        else:
            index = self.xtr.get_cell_index(points[0], points[1])
            assert index >= 0, "Point is not inside model domain"

        dst = xr.Dataset(coords=dict(Time=dsx.Time), attrs=dsx.attrs)
        dst.attrs["Origin"] = (
            "Timeseries extracted from TUFLOWFV cell-centered output using `tfv` python tools"
        )
        dst.attrs["Type"] = "Timeseries cell from TUFLOWFV Output"
        dst.attrs["Datum"] = str(datum)
        dst.attrs["Limits"] = str(limits)
        dst.attrs["Agg Fn"] = agg

        # Add coordinate locations
        if len(index) > 1:
            dst = dst.assign_coords(
                dict(
                    Location=(("Location"), [x for x in points.keys()]),
                    x=(("Location"), [x[0] for x in points.values()]),
                    y=(("Location"), [x[1] for x in points.values()]),
                    z=(("Location"), self.geo["cell_Zb"][index]),
                )
            )
        else:
            dst = dst.assign_coords(
                dict(
                    Location=(("Location"), [0]),
                    x=(("Location",), [points[0]]),
                    y=(("Location",), [points[1]]),
                )
            )

        # Add output variables to dataset
        for v in variables:
            dst[v] = (("Time", "Location"), np.zeros((dst.sizes["Time"], len(index))))
            dst[v].attrs = self._getattr_(v)

        ii = 0
        for t in tqdm(
            dsx["Time"].values, desc="Extracting timeseries, please wait", colour="blue"
        ):
            val = self.xtr.get_sheet_cell(variables, t, datum, limits, agg)

            # Now cut down to the cells
            if val.shape[0] != len(variables):
                val = val[None, :]
            val = val[:, index]

            for c, v in enumerate(variables):  # ToDO: vectorise this
                dst[v][ii] = val[c]
            ii += 1

        if len(index) == 1:
            dst = dst.isel(Location=0)

        return dst

    def get_sheet_grid(
        self,
        variables: Union[str, list] = None,
        time: Union[str, int, pd.Timestamp, slice] = None,
        bbox=None,
        dx=None,
        dy=None,
        nx=100,
        ny=100,
        method="nearest",
        crs=None,
        datum: Literal["sigma", "height", "depth", "elevation"] = "sigma",
        limits: tuple = (0, 1),
        agg: Literal["min", "mean", "max"] = "mean",
    ):
        """Extract a 2D sheet grid timeseries

        General purpose method for extracting 2D grid data from a TfvDomain object. This will handle dimension reduction of 3D variables (by default will average over the depth column, i.e., depth-averaged), as well as handling single or multiple timesteps or slices.

        This method accepts either dx/dy (grid step in meters or degrees), or nx/ny (number of grid cells in x/y). Dx/dy are given higher priority.

        There are three interpolation methods available:
        - (DEFAULT) 'nearest': takes the  cell centered values onto the grid. Fastest method for extraction.
        - 'linear': Linear interpolation using Scipy's LinearNDInterpolator
        - 'cubic': Cubic interpolation using Scipy's `CloughTocher2DInterpolator`

        If an optional EPSG CRS is supplied (`crs`), the output dataset will include CRS information. *Requires pyproj* to be available.

        Args:
            variables ([str, list], optional): list of variables to extract. Defaults to all real variables.
            time ([str, int, pd.Timestamp, slice], optional): time indexer for extraction. Defaults to the entire dataset.
            bbox ([tuple, list], optional): Bounding box of the grid (xmin, ymin, xmax, ymax). Defaults to the entire model mesh.
            dx (float, optional): x grid step in mesh coordinates. If not supplied, variable `nx` will be used.
            dy (float, optional): y grid step in mesh coordinates. If not supplied, variable `ny` will be used.
            nx (int, optional): number of grid steps in x. Will be ignored if `dx` is supplied. Defaults to 1000.
            ny (int, optional): number of grid steps in y. Will be ignored if `dy` is supplied. Defaults to 1000.
            method (str, optional): Grid interpolation method. Defaults to 'nearest'.
            crs (int, optional): epsg code of crs for attributes. must have pyproj library available. Defaults to None.
            datum (['sigma', 'height', 'depth', 'elevation'], optional): depth-averaging datum. Defaults to 'sigma'. Choose from `height`, `depth`, `elevation` or `sigma`.
            limits (tuple, optional): depth-averaging limits. Defaults to (0,1).
            agg (['min', 'mean', 'max'], optional): depth-averaging aggregation function. Defaults to 'mean'. Choose from `min`, `mean`, or `max`.

        Returns:
            xr.Dataset: Xarray grid dataset
        """

        xtr = self.xtr
        dsx = xtr._subset_dataset(time)  # Slice xarray dataset
        times = dsx["Time"]
        ts = [xtr._timestep_index(t) for t in times.values]
        nt = dsx["Time"].shape[0]

        if variables is None:
            variables = list(self.variables.keys())
        elif isinstance(variables, str):
            variables = [variables]
        nv = len(variables)

        if bbox is None:
            bbox = [
                self.geo["cell_X"].min(),
                self.geo["cell_Y"].min(),
                self.geo["cell_X"].max(),
                self.geo["cell_Y"].max(),
            ]
        bbox = np.asarray(bbox)

        xlim = bbox[[0, 2]]
        ylim = bbox[[1, 3]]
        assert (
            xlim[1] > xlim[0]
        ), "Grid x-limits must be increasing (i.e., xmax > xmin). Please check `bbox`"
        assert (
            ylim[1] > ylim[0]
        ), "Grid y-limits must be increasing (i.e., ymax > ymin). Please check `bbox`"

        # Set x-grid array
        if (dx is None) & (nx is not None):
            dx = (xlim[1] - xlim[0]) / nx
        xv = np.arange(xlim[0], xlim[1], dx)
        nx = xv.shape[0]

        # Set y-grid array
        if (dy is None) & (ny is not None):
            dy = (ylim[1] - ylim[0]) / ny
        yv = np.arange(ylim[0], ylim[1], dy)
        ny = yv.shape[0]

        # Warn user if they're trying to extract a huge grid
        if any((nx > 5000, ny > 5000)):
            warnings.warn(
                f"A very large number of grid points are being requested: ({ny}, {nx}).\nAre you sure this is what you want?"
            )

        # Setup the output xarray dataset
        if self.xtr.is_spherical:
            coords = dict(time=dsx["Time"].data, latitude=yv, longitude=xv)
            dims = ("time", "latitude", "longitude")
        else:
            coords = dict(time=dsx["Time"].data, yp=yv, xp=xv)
            dims = ("time", "yp", "xp")

        dvars = {k: (dims, np.full((nt, ny, nx), np.nan)) for k in variables}

        attrs = {
            "Origin": "2D Grid extracted from TUFLOW FV cell-centered output using `tfv` xarray accessor",
            "Type": "2D Grid from TUFLOW FV output",
            "Datum": datum,
            "Limits": limits,
            "Agg": agg,
            "Grid method": method,
        }

        dg = xr.Dataset(
            coords=coords,
            data_vars=dvars,
            attrs=attrs,
        )

        # Setup Interpolation Method
        grid_index = self.xtr.get_grid_index(xv, yv)
        mask = np.equal(grid_index, -999)
        valid = np.equal(mask, False)
        if method == "nearest":

            def get_data(t):
                return xtr.get_sheet_cell(v, t, datum, limits, agg, z_data)

            def interp(data):
                return data[grid_index[valid]]

        elif method in ["linear", "cubic"]:
            nodes = np.stack((self.geo["node_X"], self.geo["node_Y"])).T
            tri = Delaunay(nodes)  # Compute the triangulation

            X, Y = np.meshgrid(xv, yv)
            points = np.stack((X[valid], Y[valid])).T
            # valid = np.ones((ny, nx), dtype=bool)

            def get_data(t):
                return xtr.get_sheet_node(v, t, datum, limits, agg, z_data)

            if method == "linear":

                def interp(data):
                    fn = LinearNDInterpolator(tri, data)
                    return fn(points)

            elif method == "cubic":

                def interp(data):
                    fn = CloughTocher2DInterpolator(tri, data)
                    return fn(points)

        # Loop through and depth average
        for i, t in enumerate(tqdm(ts, delay=2)):
            z_data = xtr.get_integral_data(t, datum, limits)
            for v in variables:
                data = get_data(t)  # gets either cells or nodes, based on `method`
                dg[v][i].data[valid] = interp(data)  # interp, based on method.

        # Update variable attributes
        for v in variables:
            dg[v].attrs = self._getattr_(v)

        mcrs = False
        if crs is not None:
            try:
                from pyproj import CRS

                pcrs = CRS.from_epsg(crs)
                if self.xtr.is_spherical:
                    dg["latitude"].attrs = pcrs.cs_to_cf()[0]
                    dg["longitude"].attrs = pcrs.cs_to_cf()[1]
                else:
                    dg["xp"].attrs = pcrs.cs_to_cf()[0]
                    dg["yp"].attrs = pcrs.cs_to_cf()[1]
                dg.attrs["epsg"] = pcrs.to_epsg()
                dg.attrs["crs_wkt"] = pcrs.to_wkt()
                dg.attrs["crs"] = crs

            except:  # Pyproj wasn't able to be imported - use manual labelling.
                warnings.warn(
                    f"`crs={crs} was supplied but `pyproj` was not able to be imported. Ignoring crs specification"
                )
                mcrs = True
        else:
            mcrs = True

        # Manual labelling of the grid attributes
        if ("latitude" in dg) & (mcrs is True):
            dg["latitude"].attrs = {
                "standard_name": "latitude",
                "long_name": "latitude coordinate",
                "units": "degrees_north",
                "axis": "Y",
            }
            dg["longitude"].attrs = {
                "standard_name": "longitude",
                "long_name": "longitude coordinate",
                "units": "degrees_east",
                "axis": "X",
            }
            if crs is not None:
                dg.attrs["crs"] = crs
        elif ("yp" in dg) & (mcrs is True):
            dg["xp"].attrs = {
                "axis": "X",
                "long_name": "Easting",
                "standard_name": "projection_x_coordinate",
                "units": "metre",
            }
            dg["yp"].attrs = {
                "axis": "Y",
                "long_name": "Northing",
                "standard_name": "projection_y_coordinate",
                "units": "metre",
            }
            if crs is not None:
                dg.attrs["crs"] = crs

        return dg

    def plot(
        self,
        variable: str = None,
        time: Union[str, pd.Timestamp, int] = 0,
        colorbar=True,
        shading="patch",
        ax: plt.Axes = None,
        **kwargs,
    ):
        """General 2D sheet plot method

        By default, this function will plot the first variable and timestep.

        This function is a general wrapper around the tfv.visual "Sheet" methods. Kwargs will be supplied through to the underlying matplotlib function.

        Depth-averaging logic can be handled by passing through the optional keywords `datum, limits, agg` as required.

        Several magic "variables" are available via this method including:
            - Plot bed elevation using variable 'Zb'
            - Plot current speed or direction using either 'V' or 'VDir' respectively

        Args:
            variable (str, optional): variable to plot. Defaults to alphabetical first.
            time ([str, pd.Timestamp, int], optional): Timestep to plot, provided as str (e.g., '2010-01-01'), int, Timestamp object, etc. Defaults to 0.
            colorbar (bool, optional): Show colorbar (best to turn off if making subplots). Defaults to True.
            shading (str, optional): Figure shading type, which changes the underlying matplotlib function.
                Options include:
                    "patch" that calls tfv.visual.SheetPatch and Matplotlib's `PolyCollection`
                    "interp" that calls tfv.visual.SheetPatch and Matplotlib's `TriMesh`
                    "contour" that calls tfv.visual.SheetContour and Matplotlib's `TriContourSet`
                Defaults to "patch".
            ax (plt.Axes, optional): Matplotlib axis to draw on. Default will create a new figure and axis.
            kwargs (dict, optional): Keyword arguments. These are passed to the underlying matplotlib method if not a tfv specific method (e.g., depth averaging kwargs).
                Common examples include: cmap, clim, levels, norm, datum, limits, agg

        Returns:
            Sheet: tfv.visual.Sheet<X> Object, depending on the shading option.
        """
        variable, label = self._getvar_(variable)

        # Special cases (data without a time dimension)
        if variable == "Zb":
            if shading == "patch":
                variable = self._obj["cell_Zb"].values
            else:
                variable = self._obj["node_Zb"].values
            static = True
        else:
            static = False

        fig, ax, zoom = _prep_axis(ax, kwargs)

        depth_kwargs = dict(
            datum=kwargs.pop("datum", "sigma"),
            limits=kwargs.pop("limits", (0, 1)),
            agg=kwargs.pop("agg", "mean"),
        )

        if shading == "patch":
            edgecolor = kwargs.pop("edgecolor", "face")
            sheet = SheetPatch(
                ax,
                self.xtr,
                variable,
                edgecolor=edgecolor,
                zoom=zoom,
                **depth_kwargs,
                **kwargs,
            )
            mappable = sheet.patch

        elif shading == "interp":
            sheet = SheetPatch(
                ax,
                self.xtr,
                variable,
                shading=shading,
                zoom=zoom,
                **depth_kwargs,
                **kwargs,
            )
            mappable = sheet.patch

        elif shading == "contour":
            sheet = SheetContour(
                ax, self.xtr, variable, zoom=zoom, **depth_kwargs, **kwargs
            )
            mappable = sheet.cont

        # Update to current time
        if static == False:
            sheet.set_time_current(time)

            date_title = sheet.get_time_current().strftime("%Y-%m-%d %H:%M")
            ax.set_title(date_title)

        if colorbar:
            fig.colorbar(mappable, ax=ax, label=label)

        # Set tick format to float
        ax.yaxis.set_major_locator(plt.MaxNLocator(5))
        ax.xaxis.set_major_locator(plt.MaxNLocator(5))
        if self.xtr.is_spherical:
            ax.yaxis.set_major_formatter(FormatStrFormatter("%.3f"))
            ax.xaxis.set_major_formatter(FormatStrFormatter("%.3f"))
        else:
            ax.yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
            ax.xaxis.set_major_formatter(FormatStrFormatter("%.0f"))

        if ("ipympl" in matplotlib.get_backend()) & (shading != "contour"):
            z = mappable.get_array()
            xf = self.geo["cell_X"].flatten()
            yf = self.geo["cell_Y"].flatten()
            zf = z.flatten()

            def fmt_coord(x, y):
                dist = np.linalg.norm(np.vstack([xf - x, yf - y]), axis=0)
                idx = np.argmin(dist)
                z = zf[idx]
                return f"x={x:.5f}  y={y:.5f}  var={z:.5f}"

            plt.gca().format_coord = fmt_coord

        return sheet

    def plot_vector(
        self,
        variables: Union[list, tuple] = None,
        time: Union[str, pd.Timestamp, int] = 0,
        plot_type: Literal["quiver"] = "quiver",
        ax: plt.Axes = None,
        convention: Literal["cartesian", "polar"] = "cartesian",
        convention_base: Literal["north", "east"] = "east",
        convention_heading: Literal["CW", "CCW"] = "CCW",
        **kwargs,
    ):
        """General 2D vector plot method

        Generic method to call tfv.visual's `SheetVector`. This can be used to overlay vector plots on other figures.
        By default, this method will plot vectors using V_x and V_y to give velocity vectors, however a list/tuple of an x/y component can be provided.

        kwargs passed to this function are supplied to the underlying matplotlib function (e.g., Quiver or Streamplot).
        The default vector scaling for velocity is usually ok; however in some cases you may need to scale the vectors (e.g., scale=100).

        Vectors can also be set to a uniform length using `normalised=True`.

        Depth-averaging logic can be handled by passing through the optional keywords `datum, limits, agg` as required.

        Args:
            variables ([list, tuple], optional): Variables to create vector (X-comp, Y-comp). Defaults to None.
            time ([str, pd.Timestamp, int], optional): Timestep to plot, provided as str (e.g., '2010-01-01'), int, Timestamp object, etc. Defaults to 0.
            plot_type (['quiver'], optional): Plot type {'quiver'}. Defaults to "quiver".
            ax (plt.Axes, optional): Matplotlib axis to draw on. Default will create a new figure and axis.
            convention (["cartesian", "polar"], optional): Convention basis upon which to calculate vectors. Defaults to 'cartesian'.
            convention_base (["north", "east"]): Base from which angles are measured from. Defaults to 'east'
            convention_heading (["CW", "CCW"]): Direction which the angles are measured along. Defaults to 'CCW'
            kwargs (dict, optional): Keyword arguments. These are passed to the underlying matplotlib method if not a tfv specific method (e.g., depth averaging kwargs).
                Common examples include: scale, normalised, datum, limits, agg.

        Returns:
            SheetVector: `tfv.visual.SheetVector` object.
        """

        if (variables is None) | (variables == "V"):
            variables = ["V_x", "V_y"]

        fig, ax, zoom = _prep_axis(ax, kwargs)

        depth_kwargs = dict(
            datum=kwargs.pop("datum", "sigma"),
            limits=kwargs.pop("limits", (0, 1)),
            agg=kwargs.pop("agg", "mean"),
        )

        vectors = SheetVector(
            ax,
            self.xtr,
            variables,
            zorder=99,
            zoom=zoom,
            convention=convention,
            convention_base=convention_base,
            convention_heading=convention_heading,
            plot_type=plot_type,
            **depth_kwargs,
            **kwargs,
        )
        # BUG: This is required to make SheetVector respect axis xlims. Fix this later
        vectors.__static_update__()

        # Update to current time
        vectors.set_time_current(time)

        date_title = vectors.get_time_current().strftime("%Y-%m-%d %H:%M")
        ax.set_title(date_title)

        return vectors

    def plot_curtain(
        self,
        polyline: np.ndarray,
        variable: str = None,
        time: Union[str, pd.Timestamp, int] = 0,
        ax: plt.Axes = None,
        colorbar=True,
        crs=None,
        **kwargs,
    ):
        """General 2D curtain  plot method

        By default, this function will plot the first variable and timestep. A polyline is always required.

        This function is a general wrapper around the tfv.visual.CurtainPatch method. kwargs will be supplied through to the underlying matplotlib function.

        A polyline (Nx2 `numpy.ndarray`) needs to be supplied containing the X and Y coordinates in columns 0 and 1 respectively.

        Args:
            polyline (np.ndarray): a Nx2 array containing the X and Y coordinates to extract the curtain over.
            variable (str, optional): variable to plot. Defaults to 'V' if available, otherwise the first variable alphabetically.
            time ([str, pd.Timestamp, int], optional): Timestep to plot, provided as str (e.g., '2010-01-01'), int, Timestamp object, etc. Defaults to 0.
            ax (plt.Axes, optional): Matplotlib axis to draw on. Default will create a new figure and axis.
            colorbar (bool, optional): Show colorbar (best to turn off if making subplots). Defaults to True.
            crs (int, optional): EPSG Code for accurate coordinate transformation for spherical models. Requires pyproj to be installed

        Returns:
            CurtainPatch: `tfv.visual.CurtainPatch` object
        """
        if variable is None:
            if ("V_x" in self.variables) & ("V_y" in self.variables):
                variable = "V"
            elif self.variables[0] != "H":
                variable = self.variables[0]
            else:
                raise ValueError(
                    "Unable to detect what variable to plot - please specify a variable"
                )

        attrs = self._getattr_(variable)

        if ("long_name" in attrs) & ("units" in attrs):
            label = f"{attrs['long_name']} ({attrs['units']})"

        # Check and convert polyline
        polyline = _convert_polyline(polyline)

        fig, ax, zoom = _prep_axis(ax, kwargs, equal=False)

        curtain = CurtainPatch(
            ax, self.xtr, variable, polyline, zoom=zoom, crs=crs, **kwargs
        )

        # Update to current time
        curtain.set_time_current(time)

        date_title = curtain.get_time_current().strftime("%Y-%m-%d %H:%M")
        ax.set_title(date_title)
        ax.set_ylabel("Elevation (m)")
        ax.set_xlabel("Chainage (m)")

        if colorbar:
            fig.colorbar(curtain.patch, ax=ax, label=label)

        return curtain

    def plot_profile(
        self,
        point: tuple,
        variable: str = None,
        time: Union[str, pd.Timestamp, int] = 0,
        ax: plt.Axes = None,
        **kwargs,
    ):
        # Get variable label and a default var if necessary
        variable, label = self._getvar_(variable)

        kwargs["zoom"] = kwargs.pop("zoom", False)
        equal = False
        fig, ax, zoom = _prep_axis(ax, kwargs, equal=equal)
        # fig, ax = plt.subplots()

        prof = ProfileCell(ax, self.xtr, variable, point, **kwargs)
        prof.set_time_current(time)

        xx, yy = prof.line.get_data()

        ax.set_xlim([xx.min() * 1.2, xx.max() * 1.2])
        ax.set_ylim([yy.min(), yy.max() * 1.2])

        date_title = prof.get_time_current().strftime("%Y-%m-%d %H:%M")
        ax.set_title(date_title)

        return prof

    def plot_curtain_vector(
        self,
        polyline: np.ndarray,
        time: Union[str, pd.Timestamp, int] = 0,
        variables: Union[list, tuple] = None,
        ax: plt.Axes = None,
        tangential=True,
        **kwargs,
    ):
        """General 2D curtain vector plot method

        This method is designed to draw velocity vectors over a curtain. If `W` (vertical velocity) is available in the TUFLOW FV dataset, these vectors will be scaled to show vertical motion as well.
        To avoid vertical velocity scaling of the vectors, specify `tangential=False` as well.

        Note:
            This method accepts a `variables` kwarg so that custom variables can be supplied, which will be scaled with vertical velocity `W` if present.
            To avoid this behaviour, also specify `tangential=False`.

        This function is a general wrapper around the tfv.visual.CurtainVector method. kwargs will be supplied through to the underlying matplotlib function.

        A polyline (Nx2 `numpy.ndarray`) needs to be supplied containing the X and Y coordinates in columns 0 and 1 respectively.

        Args:
            polyline (np.ndarray): a Nx2 array containing the X and Y coordinates to extract the curtain over.
            time ([str, pd.Timestamp, int], optional): Timestep to plot, provided as str (e.g., '2010-01-01'), int, Timestamp object, etc. Defaults to 0.
            variables ([list, tuple], optional): Variables to create vector (X-comp, Y-comp). Defaults to None.
            ax (plt.Axes, optional): Matplotlib axis to draw on. Default will create a new figure and axis.
            tangential (bool, optional): Flag to scale vectors vertically using `W`, if present. Defaults to True.

        Returns:
            CurtainVector: `tfv.visual.CurtainVector` object.
        """
        if variables is None:
            variables = ["V_x", "V_y"]

        fig, ax, zoom = _prep_axis(ax, kwargs, equal=False)

        curtain = CurtainVector(
            ax,
            self.xtr,
            variables,
            polyline,
            zoom=zoom,
            tangential=tangential,
            **kwargs,
        )

        # Update to current time
        curtain.set_time_current(time)

        date_title = curtain.get_time_current().strftime("%Y-%m-%d %H:%M")
        ax.set_title(date_title)
        ax.set_ylabel("Elevation (m)")
        ax.set_xlabel("Chainage (m)")

        return curtain

    def plot_interactive(
        self,
        variable: str,
        ax: plt.Axes = None,
        vectors: Union[bool, list, tuple] = False,
        vector_kwargs={},
        widget=None,
        **kwargs,
    ):
        """2D interactive matplotlib plotting method for fast result viewing.

        This function wraps the `.plot` and `.plot_vector` methods, with kwargs passed directly through to these methods.
        (see `TfvDomain.plot` e.g., ds.tfv.plot and TfvDomain.plot_vector e.g., ds.tfv.plot_vector).

        This function requires matplotlib to be using an ipympl backend, typically in a Jupyter lab/notebook environment.
        Please first run `%matplotlib widget` before using this function.

        Args:
            variable (str): Variable to plot
            ax (plt.Axes, optional): Matplotlib axis to draw on. Default will create a new figure and axis.
            vectors ([bool, list, tuple], optional): Flag to draw vectors. If a boolean (True) is supplied, the vectors will be velocity (V_x, V_y).
                A list/tuple of variable names can be supplied as required (E.g., W10_x, W10_y). Defaults to False.
            vector_kwargs (dict, optional): a dictionary of kwargs that is passed directly through to the `TfvDomain.plot_vector` object.
            widget (tuple, optional): A pre-initalised ipympl widget box, generated using `TfvDomain.prep_interactive_slider`.
                This can be used to control multiple subplots using the single widget controller. Defaults to None.
            kwargs (dict, optional): Keyword arguments passed directly to `TfvDomain.plot`
        """
        # Setup simple interactive plot
        time_vec = pd.to_datetime(self["Time"].values)
        fmt = "%Y-%m-%d %H:%M"

        # Prepare a widget instance
        if widget is None:
            grid = self.prep_interactive_slider()
        else:
            grid = widget
        slider = grid[1, 0].children[0]

        prev_arrow = grid[0, 0].children[1]
        next_arrow = grid[0, 0].children[2]
        date_picker = grid[2, 0].children[0]
        date_submit = grid[2, 0].children[1]

        fig, ax, zoom = _prep_axis(ax, kwargs)

        shading = kwargs.pop("shading", "patch")
        depth_kwargs = dict(
            datum=kwargs.pop("datum", "sigma"),
            limits=kwargs.pop("limits", (0, 1)),
            agg=kwargs.pop("agg", "mean"),
        )

        sheet = self.plot(
            variable, 1, ax=ax, zoom=zoom, shading=shading, **depth_kwargs, **kwargs
        )
        if vectors is not None:
            if vectors == True:
                assert all(
                    ("V_x" in self.variables, "V_y" in self.variables)
                ), "Vector plot expected `V_x` & `V_y` in dataset, however these are not present. Please check, or supply a list [<Var_x>, <Var_y>]"
                vec = self.plot_vector(
                    ["V_x", "V_y"], 1, ax=ax, zoom=zoom, **depth_kwargs, **vector_kwargs
                )
            elif any([isinstance(vectors, x) for x in [list, tuple]]):
                vec = self.plot_vector(
                    vectors, 1, ax=ax, zoom=zoom, **depth_kwargs, **vector_kwargs
                )
                vectors = True
        ax.set_title("")

        xf = self.geo["cell_X"].flatten()
        yf = self.geo["cell_Y"].flatten()

        def update_time(change):
            date_picker.value = time_vec[change.new]

            # ax.set_title(f"{time_vec[change.new].strftime(fmt)}")

            sheet.set_time_current(change.new)
            if vectors == True:
                vec.set_time_current(change.new)

            # Update z-coordinate boilerplate
            if shading != "contour":
                zf = sheet.patch.get_array().flatten()

                def fmt_coord(x, y):
                    dist = np.linalg.norm(np.vstack([xf - x, yf - y]), axis=0)
                    idx = np.argmin(dist)
                    z = zf[idx]
                    return f"x={x:.5f}  y={y:.5f}  {variable}={z:.5f}"

                ax.format_coord = fmt_coord

            plt.draw()

        def submit_date(btn):
            c = np.argmin(np.abs(time_vec - date_picker.value))
            slider.value = c

        def next_ts(btn):
            slider.value += 1

        def prev_ts(btn):
            slider.value -= 1

        slider.observe(update_time, names="value")
        prev_arrow.on_click(prev_ts)
        next_arrow.on_click(next_ts)
        date_submit.on_click(submit_date)

        slider.value = 1
        if widget is None:
            from IPython.display import display

            return display(grid)

    def plot_curtain_interactive(
        self,
        polyline: np.ndarray,
        variable: str,
        ax: plt.Axes = None,
        vectors: bool = False,
        vector_kwargs={},
        widget=None,
        **kwargs,
    ):
        """2D interactive matplotlib method for fast curtain viewing.

        This function wraps the `.plot_curtain` and `.plot_curtain_vector` methods, with kwargs passed directly through to these methods.
        (see `TfvDomain.plot_curtain` e.g., ds.tfv.plot and TfvDomain.plot_curtain_vector e.g., ds.tfv.plot_curtain_vector).

        A polyline (Nx2 `numpy.ndarray`) needs to be supplied containing the X and Y coordinates in columns 0 and 1 respectively.

        This function requires matplotlib to be using an ipympl backend, typically in a Jupyter lab/notebook environment.
        Please first run `%matplotlib widget` before using this function.

        Args:
            polyline (np.ndarray): a Nx2 array containing the X and Y coordinates to extract the curtain over.
            variable (str): Variable to plot
            ax (plt.Axes, optional): Matplotlib axis to draw on. Default will create a new figure and axis.
            vectors ([bool, list, tuple], optional): Flag to draw vectors. If `True`, the vectors will represent projected velocity  (V_x, V_y projected to the curtain plane). Vertical velocity, W, will be included automatically if available in the model.
            vector_kwargs (dict, optional): a dictionary of kwargs that is passed directly through to the `TfvDomain.plot_curtain_vector` object.
            widget (tuple, optional): A pre-initalised ipympl widget box, generated using `TfvDomain.prep_interactive_slider`.
                This can be used to control multiple subplots using the single widget controller. Defaults to None.
            kwargs (dict, optional): Keyword arguments passed directly to `TfvDomain.plot_curtain`
        """
        # Setup simple interactive plot
        time_vec = pd.to_datetime(self["Time"].values)
        fmt = "%Y-%m-%d %H:%M"

        # Prepare a widget instance
        if widget is None:
            grid = self.prep_interactive_slider()
        else:
            grid = widget
        slider = grid[1, 0].children[0]

        prev_arrow = grid[0, 0].children[1]
        next_arrow = grid[0, 0].children[2]
        date_picker = grid[2, 0].children[0]
        date_submit = grid[2, 0].children[1]

        fig, ax, zoom = _prep_axis(ax, kwargs, equal=False)

        curtain = self.plot_curtain(polyline, variable, 1, ax=ax, **kwargs)
        if vectors == True:
            assert all(
                ("V_x" in self.variables, "V_y" in self.variables)
            ), "Curtain vectors requires `V_x` & `V_y` in dataset!"
            vec = self.plot_curtain_vector(polyline, time=1, ax=ax, **vector_kwargs)
        ax.set_title("")

        # xf = self.geo["cell_X"].flatten()
        # yf = self.geo["cell_Y"].flatten()

        def update_time(change):
            date_picker.value = time_vec[change.new]

            curtain.set_time_current(change.new)
            if vectors == True:
                vec.set_time_current(change.new)

            plt.draw()

        def submit_date(btn):
            c = np.argmin(np.abs(time_vec - date_picker.value))
            slider.value = c

        def next_ts(btn):
            slider.value += 1

        def prev_ts(btn):
            slider.value -= 1

        slider.observe(update_time, names="value")
        prev_arrow.on_click(prev_ts)
        next_arrow.on_click(next_ts)
        date_submit.on_click(submit_date)

        slider.value = 1
        if widget is None:
            from IPython.display import display

            return display(grid)

    def plot_profile_interactive(
        self,
        point: tuple,
        variable: str,
        ax: plt.Axes = None,
        widget=None,
        **kwargs,
    ):
        # Setup simple interactive plot
        time_vec = pd.to_datetime(self["Time"].values)
        fmt = "%Y-%m-%d %H:%M"

        # Prepare a widget instance
        if widget is None:
            grid = self.prep_interactive_slider()
        else:
            grid = widget
        slider = grid[1, 0].children[0]

        prev_arrow = grid[0, 0].children[1]
        next_arrow = grid[0, 0].children[2]
        date_picker = grid[2, 0].children[0]
        date_submit = grid[2, 0].children[1]

        kwargs["zoom"] = kwargs.pop("zoom", False)
        equal = False
        fig, ax, zoom = _prep_axis(ax, kwargs, equal=equal)

        prof = self.plot_profile(point, variable, 1, ax=ax, **kwargs)
        ax.set_title("")

        def update_time(change):
            date_picker.value = time_vec[change.new]
            prof.set_time_current(change.new)

        def submit_date(btn):
            c = np.argmin(np.abs(time_vec - date_picker.value))
            slider.value = c

        def next_ts(btn):
            slider.value += 1

        def prev_ts(btn):
            slider.value -= 1

        slider.observe(update_time, names="value")
        prev_arrow.on_click(prev_ts)
        next_arrow.on_click(next_ts)
        date_submit.on_click(submit_date)

        slider.value = 1
        if widget is None:
            from IPython.display import display

            return display(grid)

    def prep_interactive_slider(self):
        """Prepare an interactive ipympl widget box for controlling `TfvDomain.plot_interactive`

        This method pre-initialises a widget box that can be used to control the interactive jupyter plotting method, and is called by default from the `plot_interactive` method.

        To control multiple interactive plots using the one widget box, first call this method, e.g. `widget=ds.tfv.prep_interactive_slider()`, and then pass this widget through to the `plot_interactive` method.
        """
        try:
            import ipympl
            from ipywidgets import widgets, GridspecLayout, Layout
            import matplotlib
        except ImportError:
            print(
                "The interactive plot requries that `ipympl` and `ipywidgets` be installed"
            )

        assert (
            "ipympl" in matplotlib.get_backend()
        ), "Please run `%matplotlib widget` to enable interactive plotting in your Jupyter session!"

        nt = self.sizes["Time"]
        time_vec = pd.to_datetime(self["Time"].values)

        # Slider
        slider = widgets.IntSlider(
            value=0, min=0, max=nt, step=1, layout=Layout(width="50%", height="85%")
        )

        play = widgets.Play(
            value=0,
            min=0,
            max=nt,
            step=1,
            interval=500,
            description="Play",
            disabled=False,
            layout=Layout(width="15%", height="85%"),
        )

        widgets.jslink((play, "value"), (slider, "value"))
        play_slider = widgets.HBox([slider])

        # Date picker box
        date_picker = widgets.NaiveDatetimePicker(
            value=time_vec[0],
            min=time_vec[0],
            max=time_vec[-1],
            description="",
            style=dict(width="initial"),
            layout=Layout(width="260px", height="10px"),
        )

        date_submit = widgets.Button(
            description="Update",
            disabled=False,
            button_style="",  # 'success', 'info', 'warning', 'danger' or ''
            tooltip="Update",
            icon="arrow-turn-down-left",  # (FontAwesome names without the `fa-` prefix)
            style=dict(width="initial", height="20px"),
        )

        next_arrow = widgets.Button(
            description="",
            disabled=False,
            button_style="success",  # 'success', 'info', 'warning', 'danger' or ''
            tooltip="",
            icon="arrow-right",  # (FontAwesome names without the `fa-` prefix)
            layout=Layout(width="4%", height="85%"),
        )

        prev_arrow = widgets.Button(
            description="",
            disabled=False,
            button_style="danger",  # 'success', 'info', 'warning', 'danger' or ''
            tooltip="",
            icon="arrow-left",  # (FontAwesome names without the `fa-` prefix)
            layout=Layout(width="4%", height="85%"),
        )

        # date_box = widgets.HBox(
        #     [play, prev_arrow, next_arrow, date_picker, date_submit]
        # )

        # Prep gridbox
        grid = GridspecLayout(4, 1)
        grid[0, 0] = widgets.HBox([play, prev_arrow, next_arrow])
        grid[1, 0] = play_slider
        grid[2, 0] = widgets.HBox([date_picker, date_submit])

        return grid


class TfvTimeseries(TfvBase):
    """Xarray accessor object for working with TUFLOW FV timeseries profile netcdf files.

    Extends the functionality of native xarray to assist with navigating and extracting data from the grouped netcdf profile timeseries files.

    To use, call the `.tfv` method on an xarray dataset based on a TUFLOW FV timeseries file.
    """

    def __init__(self, xarray_obj):
        TfvBase.__init__(self, xarray_obj)
        self.ts = None
        self.__load_tfv_timeseries()

    def __repr__(self):
        if is_notebook is False:
            fmt = "%Y-%m-%d %H:%M:%S"
            # return self._obj.__repr__()
            print(" --- TUFLOW-FV Profile Output Dataset ---")
            print("")
            print(f"Num Timesteps: {self.nt}")
            print(f"Time start: {self.time_start.strftime(fmt)}")
            print(f"Time end: {self.time_end.strftime(fmt)}")
            if isinstance(self.time_step, int):
                print(f"Time step: {self.time_step} seconds")
            else:
                print(f"Time step: {self.time_step.mean().seconds} seconds")
            print("")
            print(f"Num Locations: {len(self.locations)}")
            print(f'Locations: {", ".join(self.locations.keys())}')
            print("")
            print(f'Variables in file: {", ".join(self.variables.keys())}')
            print("")
            print("Available methods: ")
            print("\t .get_timeseries(locations, variables, time, datum, limits, agg)")
            print("\t .get_location(location)")
            print("\t .plot(variable, location, time=None, ax=None)")
            return ""
        else:
            return "TUFLOW FV profile timeseries accessor object"

    def _repr_html_(self):
        """For now, this repr output is identical"""
        fmt = "%Y-%m-%d %H:%M:%S"
        # return self._obj.__repr__()
        print(" --- TUFLOW-FV Profile Output Dataset ---")
        print("")
        print(f"Num Timesteps: {self.nt}")
        print(f"Time start: {self.time_start.strftime(fmt)}")
        print(f"Time end: {self.time_end.strftime(fmt)}")
        if isinstance(self.time_step, int):
            print(f"Time step: {self.time_step} seconds")
        else:
            print(f"Time step: {self.time_step.mean().seconds} seconds")
        print("")
        print(f"Num Locations: {len(self.locations)}")
        print(f'Locations: {", ".join(self.locations.keys())}')
        print("")
        print(f'Variables in file: {", ".join(self.variables.keys())}')
        print("")
        print("Available methods: ")
        print("\t .get_timeseries(locations, variables, time, datum, limits, agg)")
        print("\t .get_location(location)")
        print("\t .plot(variable, location, time=None, ax=None)")
        return "TUFLOW FV profile timeseries accessor object"

    def __load_tfv_timeseries(self):
        if self.ts is None:
            try:
                self.ts = FvTimeSeries(self._obj)
                self.time = self.ts.time_vector
                self.locations = self.ts.locations
                self.nl = len(self.locations)
                self.nt = len(self.time)
                self.time_start = self.time[0]
                self.time_end = self.time[-1]
                self.time_duration = self.time[-1] - self.time[0]

                ts = pd.to_timedelta(np.diff(self.time).astype(float) / 10**9, unit="s")
                if len(set(ts)) == 1:
                    self.time_step = ts[0].seconds
                elif len(set(ts)) > 1:
                    self.time_step = ts
                else:
                    assert False, "No time data has been detected"

                # Override the original dataset with a more informative one.
                dsx = self._obj
                dsx = dsx.assign_coords(
                    Locations=(("Locations",), list(self.locations.keys()))
                )
                dsx = dsx.assign_coords(Time=(("Time",), self.time))
                coords = np.asarray(list(self.locations.values()))
                dsx = dsx.assign(X=(("Locations",), coords[:, 0]))
                dsx = dsx.assign(Y=(("Locations",), coords[:, 1]))
                dsx = dsx.assign(Variables=(("",), self.ts.variables))
                self._obj = dsx

            except TypeError:
                print(
                    "Data does not appear to be a valid TUFLOW-FV profile timeseries netcdf file"
                )

    @property
    def variables(self):
        grp = next(iter(self.locations.items()))[0]
        return {
            k: v.attrs
            for k, v in self.ds[grp].data_vars.items()
            if k not in ["X", "Y", "ResTime", "stat", "layerface_Z"]
            if "Time" not in v.attrs  # Check usual suspects, and Time
        }

    @property
    def ds(self):
        return self.ts.ds

    def get_location(self, location: str) -> xr.Dataset:
        """Get individual profile dataset

        Returns a native Xarray dataset for a single profile location.
        This can be alternatively accessed via a dictionary `.tfv.ds[location]`

        Args:
            locations (str): Location name to extract. (see `.locations` method for the list of stored locations)

        Returns:
            xr.Dataset: Individual profile dataset
        """

        assert (
            location in self.locations.keys()
        ), "Requested location not present in dataset"

        return self.ds[location]

    def get_timeseries(
        self,
        locations: Union[str, list] = None,
        variables: Union[str, list] = None,
        time: Union[str, int, pd.Timestamp, slice] = None,
        datum: Literal["sigma", "height", "depth", "elevation"] = "sigma",
        limits: tuple = (0, 1),
        agg: Literal["min", "mean", "max"] = "mean",
    ):
        """Extract 1D timeseries at location(s).

        Method to extract 1D timeseries at one, or several locations from the dataset.
        This method will handle dimension reduction, by default using depth-averaging.

        Note:
            This method can be slow for many locations and long-timeseries, as each profile location is effectively a standalone dataset.

        Args:
            locations (Union[str, list]): Location names to extract (see `.locations` method for the list of stored locations)
            variables ([str, list]): variables to extract. Defaults to all. ("V" or "VDir" may be requested if "V_x" and "V_y" are present).
            time ([str, pd.Timestamp, int, slice], optional): time indexer for extraction. Defaults to the entire dataset.
            datum (['sigma', 'height', 'depth', 'elevation'], optional): depth-averaging datum. Defaults to 'sigma'. Choose from `height`, `depth`, `elevation` or `sigma`.
            limits (tuple, optional): depth-averaging limits. Defaults to (0,1).
            agg (['min', 'mean', 'max'], optional): depth-averaging aggregation function. Defaults to 'mean'. Choose from `min`, `mean`, or `max`.

        Returns:
            xr.Dataset: A timeseries dataset in xarray format
        """

        if isinstance(variables, str):
            variables = [variables]

        # Get 2D cell index
        if isinstance(locations, str):
            locations = [locations]
        elif locations is None:
            locations = list(self.locations.keys())

        ds_set = []
        for l in locations:
            ds_set.append(
                self.ts.get_timeseries(
                    l,
                    variables=variables,
                    time=time,
                    datum=datum,
                    limits=limits,
                    agg=agg,
                )
            )
        ds = xr.concat(ds_set, dim="Location", combine_attrs="drop_conflicts")

        # Add coordinate locations
        ds = ds.assign_coords(
            dict(
                Location=(("Location"), locations),
                X=(("Location"), [self.locations[x][0] for x in locations]),
                Y=(("Location"), [self.locations[x][1] for x in locations]),
            )
        )
        return ds

    def plot(
        self,
        variable: str = None,
        location: str = None,
        time: Union[str, pd.Timestamp, int] = 0,
        ax=None,
        **kwargs,
    ):
        """Plots a profile at a single time

        Simple method to draw a profile through depth at a single timestep.
        The profile is shown on the layerfaces of the model (i.e., the vertical cell "edges")
        based on linear interpolation from the vertical cell centers.

        Args:
            variable (str, optional): variable to plot. Defaults to the first variable.
            location (str, optional): profile location to plot. Defaults to first location.
            time ([str, pd.Timestamp, int], optional): Time to plot. Defaults to 0.
            ax (plt.Axes, optional): Matplotlib axis to draw profile. Default is to create a new figure unless specified.
            kwargs (dict, optional): Keyword arguments passed to matplotlib's pyplot.plot method.

        Returns:
            np.ndarray: Array containing profile data, interpolated linearly to the layerfaces
        """

        variable, label = self._getvar_(variable, skip=["H"])
        if location is None:
            location = next(iter(self.locations.items()))[0]

        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = plt.gcf()

        # Get data
        lfz = self.ts.get_raw_data("layerface_Z", location, time)[::-1, 0]
        arr = self.ts.get_raw_data(variable, location, time)[::-1, 0]
        time = self.ts.get_raw_data("Time", location, time)[0]

        z_cell = np.mean((lfz[1:], lfz[:-1]), axis=0)

        if arr.sum() == 0:
            arr_lfz = np.zeros(lfz.shape)
        else:
            arr_lfz = np.interp(lfz, z_cell, arr)

        marker = kwargs.pop("marker", ".")
        color = kwargs.pop("color", "black")
        line = ax.plot(arr_lfz, lfz, "-", marker=marker, color=color, **kwargs)

        date_title = pd.to_datetime(time).strftime("%Y-%m-%d %H:%M")

        ax.grid(True)
        ax.set_ylabel("Elevation (m)")
        ax.set_xlabel(label)
        ax.set_title(date_title)
        ax.set_xlim([arr_lfz.min() * 0.975, arr_lfz.max() * 1.025])

        return arr_lfz


def _prep_axis(ax, kwargs, equal=True):
    """
    Utility to generate new mpl fig/ax if required,
    otherwise, check if the axis requires zooming
    """
    if ax is None:
        fig, ax = plt.subplots()

        # For domain plots, etc. Curtain plots don't want this.
        if equal == True:
            ax.axis("equal")

        zoom = kwargs.pop("zoom", True)
    else:
        fig = plt.gcf()
        # Logic
        if (ax.get_xlim() == (0, 1)) & (ax.get_ylim() == (0, 1)):
            zoom = kwargs.pop("zoom", True)
        else:
            zoom = kwargs.pop("zoom", False)

    return fig, ax, zoom


def is_notebook() -> bool:
    try:
        shell = get_ipython().__class__.__name__
        if shell == "ZMQInteractiveShell":
            return True  # Jupyter notebook or qtconsole
        elif shell == "TerminalInteractiveShell":
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False  # Probably standard Python interpreter


def convert_grid_to_tfv(
    ds,
    x="longitude",
    y="latitude",
    time="time",
    z="depth",
    flipz=True,
    spherical=True,
    use_tfv_naming=True,
):
    """Convert / cast an ordinary Xarray Model Dataset as a TfvDomain object

    Tool to cast an typical model xarray dataset, with at minimum time, x and y, coordinates,
    to a TfvDomain file.

    This function is dask enabled, and it is advisable to use this method with time chunked by 1 where possible.
    (E.g., chunks=dict(time=1))

    Args:
        ds (xr.Dataset): Xarray model dataset
        x (str, optional): Name of the x coordinate. Defaults to 'longitude'.
        y (str, optional): Name of the y coordinate. Defaults to 'latitude'.
        time (str, optional): Name of the time coordinate. Defaults to 'time'.
        z (str, optional): Name of the z coordinate, if available. Defaults to 'depth'.
        flipz (bool, optional): Flag to flip the z-coordinate (e.g., depth to elevation). Defaults to True.
        spherical (bool, optional): Flag for whether the x/y coords are in degrees. Defaults to True.
        use_tfv_naming (bool, optional): Flag to rename common variables to standard TUFLOW FV names. Defaults to True.
    """
    return grid_remap(
        ds,
        x=x,
        y=y,
        time=time,
        z=z,
        flipz=flipz,
        spherical=spherical,
        use_tfv_naming=use_tfv_naming,
    )


def _convert_polyline(polyline):
    if isinstance(polyline, list):
        polyline == np.asarray(polyline)
    elif isinstance(polyline, tuple):
        polyline == np.asarray(polyline)
    elif not isinstance(polyline, np.ndarray):
        try:
            from shapely.geometry import LineString

            if isinstance(polyline, LineString):
                polyline = np.stack(polyline.xy).T
        except:
            raise ValueError(
                "Polyline should be an Nx2 numpy array, or a list of coordinates [[x1,y1], [x2,y2], ..., [xn, yn]], or a Shapely `LineString`"
            )
    else:
        assert polyline.shape[1] == 2, "Polyline should be an Nx2 numpy array"
    return polyline
