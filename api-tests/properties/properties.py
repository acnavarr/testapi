import configparser
import os


def get_env_or_property(env_name, property_name):
    return os.environ.get(env_name, get_property(property_name))


def get_property(property_name):
    return _get_property_from_file("general", property_name)


def _get_property_from_file(context, property_name):
    config_file_path = os.environ.get("LAB_CONFIG", os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '../../config.ini'))
    _config_file = configparser.ConfigParser()
    _config_file.read(config_file_path)
    result = _config_file.get(context, property_name)
    return result
