import configparser
import os

def get_version():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'setup.cfg'))
    return config['metadata']['version']

__version__ = get_version()
__author__ = "support@tulow.com"
__aus_date__ = "%d/%m/%Y %H:%M:%S"
