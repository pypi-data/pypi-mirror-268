# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : yaml_utils.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""To handle basic Yaml operations like, reading, writting etc,."""

from multiprocessing import Lock
import unittest
import yaml


mutex = Lock()


class MyDumper(yaml.SafeDumper):
    """insert blank lines between top-level objects"""

    def ignore_aliases(self, data):
        return True

    def write_line_break(self, data=None):
        super().write_line_break(data)
        if len(self.indents) == 1:
            super().write_line_break()


def write_yaml(filepath, config):
    """writes the input data and saves it as a yaml file"""
    with mutex:
        with open(filepath, "w", encoding="utf-8") as fp:
            yaml.dump(config, fp, default_flow_style=False, sort_keys=False, Dumper=MyDumper)


def read_yaml(yamlfile):
    """reads the yaml and returns the data in the file"""
    with mutex:
        with open(yamlfile, "r", encoding="utf-8") as config_yaml:
            config = yaml.load(config_yaml, Loader=yaml.FullLoader)
        return config


def yaml_format(input_file_path, output_file_path):
    """convert int and float list to single line string"""
    with open(input_file_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    def convert(obj):
        if isinstance(obj, list):
            if all(isinstance(x, (int, float)) for x in obj):
                return f'[{", ".join(str(x) for x in obj)}]'
            return obj
        return obj

    with open(output_file_path, "w", encoding="utf-8") as f:
        yaml.dump({key: {key2: convert(value2) for key2, value2 in value.items()} for key, value in data.items()}, f, default_flow_style=False, sort_keys=False, Dumper=MyDumper)


class TestYamlUtils(unittest.TestCase):
    """test_yaml utils"""

    @classmethod
    def setUpClass(cls):
        cls.yamlfile_ = "samples/sample1.yml"
        cls.write_folder_ = "samples/test_results/"

    def test_read_write_yaml(self):
        """test read write"""
        write_path = self.write_folder_ + "out1.yml"
        config1 = read_yaml(self.yamlfile_)
        write_yaml(write_path, config1)
        config2 = read_yaml(write_path)
        assert config1 == config2, "read write yaml not matching"

    def test_formatting_yaml(self):
        """test read write"""
        write_path = self.write_folder_ + "out2.yml"
        yaml_format(input_file_path=self.yamlfile_, output_file_path=write_path)
        config1 = read_yaml(yamlfile="samples/sample2.yml")
        config2 = read_yaml(write_path)
        assert config1 == config2, "yaml not matching"


if __name__ == "__main__":
    test_obj = TestYamlUtils()
    test_obj.setUpClass()
    test_obj.test_read_write_yaml()
    test_obj.test_formatting_yaml()
