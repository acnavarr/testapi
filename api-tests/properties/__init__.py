import os

from properties import properties

if "LAB_CONFIG" not in os.environ:
    os.environ["LAB_CONFIG"] = "properties/config.ini"

CONFIG = {
    "api_host": properties.get_env_or_property("LAB_API_API_HOST", "api_host"),
    "api_key": properties.get_env_or_property("LAB_API_KEY", "api_key")
}
