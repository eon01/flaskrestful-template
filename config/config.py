import configparser
import os

# current module folder path
dir_path = os.path.dirname(os.path.realpath(__file__))


DEFAULT_CONFIG_FILE = dir_path + "/" + 'default.conf'

if os.environ.get('ENV') == "dev":
    DEFAULT_CONFIG_FILE = dir_path + "/" + "dev.conf"
elif os.environ.get('ENV') == "prod":
    DEFAULT_CONFIG_FILE = dir_path + "/" + "prod.conf"

def get_config_file():
    return os.environ.get('CONFIG_FILE', DEFAULT_CONFIG_FILE)

CONFIG_FILE = get_config_file()

def create_config(config_file=None):
    parser = configparser.ConfigParser()
    parser.read(config_file or CONFIG_FILE)
    return parser

CONFIG = create_config()

def get_config():
    return CONFIG
    
     

