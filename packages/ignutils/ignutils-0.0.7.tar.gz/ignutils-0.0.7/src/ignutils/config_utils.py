"""Abstract class for creating and updating module configuration"""

import os
import os.path as osp
import abc
from copy import deepcopy
# import unittest
from fabulous import color

from ignutils.yaml_utils import read_yaml, write_yaml


class ConfigAbstract(metaclass=abc.ABCMeta):
    """Config class for creating and updating configuration for modules"""

    def __init__(self, config_path):
        """Initialize the configuration settings.

        Args:
            module_name (str): Module name
            config_dir (str): configuration dictionary file path.
        """
        self.config_path = config_path
        self.main_config = self.get_main_config()
        self.child_configs = self.get_child_configs()
        self.config_data = self._make_config()

    @abc.abstractmethod
    def get_main_config(self):
        """Generate default config and write default yaml."""
        config = {
            "module_name": {"value": "module_name", "choices": None, "hint": "Module name"},
            "infer_filters": {"value": ["length_breadth_filter"], "choices": ["length_breadth_filter"], "hint": "Available filters for post inference", "child_config": "filter_config"},
        }

        return config

    @abc.abstractmethod
    def get_child_configs(self):
        """Create list of child config dicts"""
        child_configs = [
            {
                "filter_config": {
                    "length_breadth_filter": {
                        "enabled": {
                            "value": False,
                            "choices": [True, False],
                            "hint": "Enable/Disable",
                        },
                        "length_threshold": {
                            "value": 0,
                            "choices": None,
                            "hint": "Length threshold in percent for length breadth filter",
                        },
                        "breadth_threshold": {
                            "value": 0,
                            "choices": None,
                            "hint": "Breadth threshold in percent for length breadth filter",
                        },
                    }
                }
            }
        ]

        return child_configs

    def __call__(self, key):
        """Given key, the value information from the project configuration is returned."""
        return self.config_data[key]["value"]

    def config(self, key):
        """Get the value for the given key from config"""
        return self.config_data[key]["value"]

    def get_config(self):
        """Get config dictionary"""
        return self.config_data

    def edit_config(self, key, val, choices=None, hint=None):
        """Update a particular item in config."""
        new_dict = {"value": val, "choices": choices, "hint": hint}
        self.config_data[key] = new_dict

    def _update_config(self):
        """Get default config, update value from the config file and write the new yaml.

        Returns:
            dict: A python configuration dictionary.
        """
        self._get_new_config()
        new_config = deepcopy(self.main_config)
        yaml_config = read_yaml(self.config_path)
        print(color.green(f"Using config : {self.config_path}"))

        # Checking env variables for overriding threshold values
        env_dict = {}
        for name, value in os.environ.items():
            env_dict[name] = value
        # check for key in env list in the below for loop to add threshold values
        for key, value_dict in new_config.items():
            if env_dict.get(key):
                assert value_dict.get("child_config") is None, "Environment config value not updated, child config not expected"
                val = env_dict.get(key)
                if new_config[key]["choices"] in [[True, False], [False, True]]:
                    val = bool(val)
                new_config[key]["value"] = val
            elif yaml_config.get(key):
                new_config[key]["value"] = yaml_config[key]["value"]
        write_yaml(self.config_path, new_config)

        return new_config

    def _get_new_config(self):
        """Create new config based on main and child configs"""
        for _, fltr in enumerate(self.main_config.values()):
            if fltr.get("child_config") is not None:
                child_config = fltr["child_config"]
                for config in self.child_configs:
                    for cfg_name, cfg_val in config.items():
                        if cfg_name == child_config:
                            for i, val in enumerate(fltr["value"]):
                                fltr["value"][i] = {val: cfg_val[val]}

    def _make_config(self):
        """Creating configuration dict and updating with existing config yaml if available

        Returns:
            dict: A project configuration information in the form of dictionary.
        """
        if not osp.isfile(self.config_path):
            self._get_new_config()
            write_yaml(self.config_path, self.main_config)
            print(
                "\t",
                color.green(f"Please Check & update config {self.config_path} and run again "),
            )
            config = read_yaml(self.config_path)
        else:
            config = self._update_config()

        return config
