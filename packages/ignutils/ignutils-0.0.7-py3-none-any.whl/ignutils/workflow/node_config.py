"""To set project configuration."""

import sys
import unittest
import numpy as np
from fabulous import color

from ignutils.config_utils import ConfigAbstract
from ignutils.yaml_utils import read_yaml, write_yaml


class NodeConfig(ConfigAbstract):
    """Object representing the configuration settings."""

    def __init__(self, node_name, config_path):
        """Initialize the configuration settings.

        Args:
            node_name (str): Node name
            config_path (str): configuration yaml file path.
        """
        self.node_name = node_name
        super().__init__(config_path=config_path)

        if self.__call__("db_branch_full") is None:
            print(color.green(f"Please update db_branch in config: {self.config_path}"))
            sys.exit()

        elif self.__call__("classes") is None:
            print(color.green(f"Please update classes in config: {self.config_path}"))
            sys.exit()

        class_dict = self.get_class_dict(self.__call__("classes"))
        self.edit_config("class_dict", class_dict)

    def get_data(self):
        """Get config dictionary"""
        return self.config_data

    def get_main_config(self):
        """Generate default config and write default yaml."""
        config = {
            "node_name": {
                "value": self.node_name,
                "choices": None,
                "hint": "current node name",
            },
            "db_branch_full": {
                "value": None,
                "choices": None,
                "hint": "DB branch name list to enable this use -f true while training",
            },
            "db_branch_dummy": {
                "value": None,
                "choices": None,
                "hint": "DB dummy branch list. By default dummy is used for training",
            },
            "model_input_HW": {
                "value": [224, 224],
                "choices": None,
                "hint": "model input height and width",
            },
            "model_output_HW": {
                "value": [112, 112],
                "choices": None,
                "hint": "model output height and width",
            },
            "classes": {
                "value": {self.node_name: {"color": [255, 0, 0], "co_labels": [self.node_name]}},
                "choices": None,
                "hint": "labels and color associated with each class",
            },
            "train_val_split": {
                "value": [0.8, 0.2],
                "choices": None,
                "hint": "train_val_split",
            },
            "parent_contour": {
                "value": None,
                "choices": None,
                "hint": "Parent contour label name",
            },
            "train_dump_extension": {
                "value": ".png",
                "choices": [".png", ".jpg"],
                "hint": "train image dumping extension",
            },
            "shape_type": {
                "value": "polygon",
                "choices": ["polygon", "line_strip"],
                "hint": "Crop type",
            },
            "masking": {
                "value": False,
                "choices": [True, False],
                "hint": "Enable/Disable masking",
            },
            "vertical_first_flag": {
                "value": False,
                "choices": [True, False],
                "hint": "Crop orientation preference",
            },
            "unit_vec": {
                "value": None,
                "choices": [[0, 1], [1, 0], None],
                "hint": "Unit vector direction from bottom to top",
            },
            "inference_expansion": {
                "value": [0, 0],
                "choices": None,
                "hint": "height and width for inference/test/val. During training/inference, if crop dimension is smaller than model dimension, then crop will be expanded till model dimension. else it will be expanded till infer_expansion dimension.",
            },
            "train_extra_expansion": {
                "value": [-1, -1],
                "choices": None,
                "hint": "Do extra padding during data dump. Values are in order [height and width] values. This extra expansion is used for random crop during training. New width will become old_width + 2 * train_extra_expansion[1]",
            },
            "crop_type": {
                "value": "fitbox",
                "choices": ["bbox", "fitbox", "trapezoid", "aspect_width_first", "aspect_height_first"],
                "hint": "Crop type",
            },
            "dynamic_padding": {"value": True, "choices": [True, False], "hint": "Enable/Disable dynamic padding"},
            "autocrop": {
                "value": False,
                "choices": [True, False],
                "hint": "Enable/Disable autocrop feature",
            },
            "tiling_mode": {
                "value": None,
                "choices": ["fixed_size_tiling", "fixed_count_tiling", "aspect_ratio_based_tiling"],
                "hint": "Tiling modes",
            },
            "tile_x_split": {
                "value": 1,
                "choices": None,
                "hint": "Split count on column",
            },
            "tile_y_split": {"value": 1, "choices": None, "hint": "Split count on row"},
            "tile_h": {"value": None, "choices": None, "hint": "tile fixed height"},
            "tile_w": {"value": None, "choices": None, "hint": "tile fixed width"},
            "overlap_x": {"value": 0, "choices": [0,10,20], "hint": "Pixel Overlap along  x in tiling"},
            "overlap_y": {"value": 0, "choices":[ 0,10,20], "hint": "Pixel Overlap along y in tiling"},
            "DataGenerator": {
                "value": "yield_generator",
                "choices": ["yield_generator"],
                "hint": "Data Generator to use",
            },
            "batch_size": {
                "value": 5,
                "choices": None,
                "hint": "Batch size for training",
            },
            "val_batch_size": {
                "value": 5,
                "choices": None,
                "hint": "Val Batch size for training",
            },
            "augment": {
                "value": False,
                "choices": [True, False],
                "hint": "Enable/Disable augmentation",
            },
            "passive_aug_name": {
                "value": "aug_all",
                "choices": ["aug_all", "aug_damage"],
                "hint": "Select passive augmentation type",
            },
            "active_augmentation": {"value": ["foreground", "background"], "choices": ["foreground", "background"], "hint": "Enable/Disable augmentation", "child_config": "aug_config"},
            "segmentation_modelname": {
                "value": "mobilenet_unet",
                "choices": [
                    "mobilenet_unet",
                    "resnet50_unet",
                    "vgg_unet",
                    "unet",
                    "unet_mini",
                    "pspnet_101",
                    "pspnet_50",
                    "resnet50_pspnet",
                    "vgg_pspnet",
                ],
                "hint": "Model name",
            },
            "classifier_modelname": {
                "value": "resnet18",
                "choices": [
                    "alexnet",
                    "convnext_tiny",
                    "convnext_small",
                    "convnext_large",
                    "densenet121",
                    "densenet161",
                    "densenet169",
                    "densenet201",
                    "efficientnet_b0",
                    "efficientnet_b1",
                    "efficientnet_b2",
                    "efficientnet_b3",
                    "efficientnet_b4",
                    "efficientnet_b5",
                    "efficientnet_b6",
                    "efficientnet_b7",
                    "efficientnet_v2_s",
                    "efficientnet_v2_m",
                    "efficientnet_v2_l",
                    "inception_v3",
                    "maxvit_t",
                    "mnasnet0_5",
                    "mnasnet0_75",
                    "mnasnet1_0",
                    "mnasnet1_3",
                    "mobilenet_v2",
                    "mobilenet_v3_large",
                    "mobilenet_v3_small",
                    "resnet18",
                    "resnet34",
                    "resnet50",
                    "resnet101",
                    "resnet152",
                    "resnext50_32x4d",
                    "resnext101_32x8d",
                    "resnext101_64x4d",
                    "shufflenet_v2_x0_5",
                    "shufflenet_v2_x1_0",
                    "shufflenet_v2_x1_5",
                    "shufflenet_v2_x2_0",
                    "squeezenet1_0",
                    "squeezenet1_1",
                    "vgg16",
                    "vgg19",
                ],
                "hint": "Classification Model name",
            },
            "test_img_count_threshold": {
                "value": 100,
                "choices": None,
                "hint": "Minimum number of images in test folder while training",
            },
            "morphology_op": {
                "value": None,
                "choices": ["MORPH_CLOSE", "MORPH_OPEN", "MORPH_DILATE", None],
                "hint": "Apply morphology op",
            },
            "morphology_kernel_HW": {
                "value": None,
                "choices": None,
                "hint": "H W kernel size for morphology op, Ex: [50, 1]",
            },
            "hull": {
                "value": False,
                "choices": [True, False],
                "hint": "Enable/Disable hull",
            },
            "fused_dump": {
                "value": True,
                "choices": [True, False],
                "hint": "Enable/Disable Fused dumping",
            },
            "overlay_mode": {
                "value": "outerline",
                "choices": ["outerline", "fill", "fitbbox", "bbox"],
                "hint": "Overlay modes",
            },
            "infer_filters": {
                "value": ["check_inside_parent", "max_area", "length_breadth_filter", "check_inside_exclude_node", "subtract_exclude_node", "get_merged_contours"],
                "choices": ["max_area", "check_inside_parent", "length_breadth_filter", "check_inside_exclude_node", "subtract_exclude_node", "get_merged_contours"],
                "hint": "Available filters for post inference",
                "child_config": "filter_config",
            },
            "train_filters": {
                "value": ["max_area", "length_breadth_filter", "check_inside_exclude_node", "subtract_exclude_node", "get_merged_contours"],
                "choices": ["max_area", "check_inside_parent", "length_breadth_filter", "check_inside_exclude_node", "subtract_exclude_node", "get_merged_contours"],
                "hint": "Available filters prior to training, refer infer_filters for filters structure",
                "child_config": "filter_config",
            },
            "neg_dump_criteria": {
                "value": {"empty_probability": [0.0, 0.0, 0.0], "neg_co_label_probability": [0.0, 0.0, 0.0], "empty_percentage": [0, 0, 0], "neg_co_label_percentage": [0, 0, 0]},
                "choices": {"empty_probability": [0.1, 0.1, 0.1], "neg_co_label_probability": [0.5, 0.5, 0.5], "empty_percentage": [2, 2, 2], "neg_co_label_percentage": [10, 10, 10]},
                "hint": "fraction wrt positive samples, for adding negative images into train val test  dump folder respectively",
            },
            "negative_co_labels": {
                "value": [],
                "choices": None,
                "hint": "Additional co-labels (effect only on training)",
            },
            "merge_train_val_test": {
                "value": True,
                "choices": [True, False],
                "hint": "Merge train, val and test, Enable for quick demos",
            },
            "resize_factor": {
                "value": 2,
                "choices": None,
                "hint": "For dumping images with dimension (rescale_fasctor*model input dim), Provide null for dumping with full resolution",
            },
            "test_overlap_threshold": {
                "value": 1,
                "choices": None,
                "hint": "overlap threshold in pixels between ground truth and predicted contour",
            },
            "small_fraction": {
                "value": 0.01,
                "choices": None,
                "hint": "fraction wrt max parent min width|height, if less than this considered as small.",
            },
            "ignore_fraction": {
                "value": 0.001,
                "choices": None,
                "hint": "fraction wrt max parent min width|height, contours less than this  will be ignored.",
            },
            "line_thickness": {
                "value": 1,
                "choices": None,
                "hint": "Thickness for line strip labels",
            },
            "infer_dump_mask": {
                "value": False,
                "choices": [True, False],
                "hint": "Dump node level predicted masks",
            },
            "triton_serve": {
                "value": False,
                "choices": [True, False],
                "hint": "Enable/Disable Triton serve",
            },
            "ray_serve": {
                "value": False,
                "choices": [True, False],
                "hint": "Enable/Disable Ray serve",
            },
            "roi_label": {
                "value": None,
                "choices": None,
                "hint": "Labelname for ROI in labelled json",
            },
            "dump_from_generator": {
                "value": True,
                "choices": [True, False],
                "hint": "Whether to dump (img, mask, json) pair in datagenerator for checking in labelme",
            },
        }

        return config

    def get_child_configs(self):
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
                    },
                    "check_inside_parent": {
                        "enabled": {
                            "value": False,
                            "choices": [True, False],
                            "hint": "Enable/Disable",
                        },
                        "overlap_threshold": {
                            "value": 0,
                            "choices": None,
                            "hint": "Threshold in pixel count for overlap with parent canvas",
                        },
                    },
                    "check_inside_exclude_node": {
                        "enabled": {
                            "value": False,
                            "choices": [True, False],
                            "hint": "Enable/Disable",
                        },
                        "params": {
                            "value": [],
                            "choices": None,
                            "hint": "Any contours falls under listed exclude nodes will be removed",
                        },
                    },
                    "max_area": {
                        "enabled": {
                            "value": False,
                            "choices": [True, False],
                            "hint": "Enable/Disable",
                        },
                        "params": {
                            "value": None,
                            "choices": None,
                            "hint": "Retain only maximum area contour",
                        },
                    },
                    "subtract_exclude_node": {
                        "enabled": {
                            "value": False,
                            "choices": [True, False],
                            "hint": "Enable/Disable",
                        },
                        "params": {"value": [], "choices": None, "hint": "Subtract exclude contour from current node"},
                    },
                    "get_merged_contours": {
                        "enabled": {
                            "value": False,
                            "choices": [True, False],
                            "hint": "Enable/Disable",
                        },
                        "params": {"value": None, "choices": None, "hint": "Loop throgh all current contours, and merge if touching"},
                    },
                },
                "aug_config": {
                    "foreground": {
                        "enabled": {
                            "value": False,
                            "choices": [True, False],
                            "hint": "Enable/Disable",
                        },
                        "dump_positive_aug_crops": {
                            "value": False,
                            "choices": [True, False],
                            "hint": "Enable/Disable positive crops for augmentation",
                        },
                        "dump_negative_aug_crops": {
                            "value": False,
                            "choices": [True, False],
                            "hint": "Enable/Disable negative crops for augmentation",
                        },
                        "activeaug_node_crop_branchname": {
                            "value": None,
                            "choices": None,
                            "hint": "current node based image crops branch name for active augmentation. Ex: scopito_damage_crops for Scopito.",
                        },
                        "activeaug_non_node_crop_branchname": {
                            "value": None,
                            "choices": None,
                            "hint": "image crops branch name for active augmentation from other project db repos. Ex: wall_crack for Scopito.",
                        },
                        "activeaug_non_node_fulldb_branchname": {
                            "value": None,
                            "choices": None,
                            "hint": "full db  branch name for active augmentation from other project db repos. Ex: wall_crack for Scopito.",
                        },
                        "activeaug_non_node_crop_labelnames": {
                            "value": [],
                            "choices": None,
                            "hint": "labelname for non node crop using in active augmentation.Ex: A2_concrete_wall_crack for wall crack for Scopito.",
                        },
                        "activeaug_node_vs_non_node_percent": {
                            "value": None,
                            "choices": None,
                            "hint": "Percentage to control addition of node crops Vs non node crops in active augmentation.",
                        },
                        "aug_probability": {
                            "value": 0,
                            "choices": None,
                            "hint": "probability to add fg augmentation",
                        },
                        "activeaug_negative_crop_branchname": {
                            "value": None,
                            "choices": None,
                            "hint": "Negative image crops branch name for active augemntation. Ex: scopito_text_crops for Scopito.",
                        },
                        "activeaug_negative_crop_labelnames": {
                            "value": [],
                            "choices": None,
                            "hint": "labelname for neg crop using in active augmentation.Ex: scopito_text for Scopito.",
                        },
                        "activeaug_negative_crop_add_mode": {
                            "value": "inside",
                            "choices": ["inside", "outside", "anywhere"],
                            "hint": "if inside neg crops can come inside the parent contour, if outside crops cane be placed outside otherwise anywhere in the image.",
                        },
                        "activeaug_positive_crop_labelnames": {
                            "value": [self.node_name],
                            "choices": None,
                            "hint": "labelnames for childnodes need to be added in image",
                        },
                    },
                    "background": {
                        "enabled": {
                            "value": False,
                            "choices": [True, False],
                            "hint": "Enable/Disable",
                        },
                        "bg_db_branch_name": {
                            "value": "background_images",
                            "choices": ["background_images"],
                            "hint": "db branch with random bg Images from internet",
                        },
                        "aug_probability": {
                            "value": 0,
                            "choices": None,
                            "hint": "probability to add bg augmentation",
                        },
                        "bg_aug_labelnames": {
                            "value": [self.node_name],
                            "choices": None,
                            "hint": "labelnames that must be retained while changing background",
                        },
                    },
                },
            }
        ]

        return child_configs

    def get_class_dict(self, class_list):
        """To get the classname and color for a given class and color list, format: {'1':{'classname': 'A6_scopito_erosion','color': [255, 0, 0]}}.
        Args:
            class_list (list): List of the labels or classes.
            colorlist (list): Corresponding labels or classes color values list.
        Returns:
            dict: classname and color in the form of a dictionary.
        """
        class_dict = {}
        for index, classname in enumerate(class_list):
            color_ = class_list[classname]["color"]
            temp_dict = {}
            temp_dict["classname"] = classname
            temp_dict["color"] = color_
            class_dict[str(index + 1)] = temp_dict
        class_dict[str(0)] = {"classname": "background", "color": [0, 0, 0]}
        return class_dict

    def encode_labeldict(self, labelmap_dict):
        """Given labelmap_dict , will return encoded labeldict format: {'1': {'classname': 'A6_scopito_erosion','color': [255, 0, 0]}}.
        Args:
            labelmap_dict (_type_): _description_
        Returns:
            dict: Encoded labeldict.
        """
        new_dict = {}
        label_list = sorted(list(labelmap_dict.keys()))

        for index, label in enumerate(label_list):
            templist = labelmap_dict[label]
            templist = np.array(templist).astype(int).tolist()
            new_dict[str(index + 1)] = templist
        new_dict[str(0)] = [0, 0, 0]

        return new_dict


class TestNodeConfig(unittest.TestCase):
    """Test methods"""

    def test_child_config_update(self):
        """Testing config creation based on updating child config value"""
        # setting default values
        module_name = "dummy_node"
        test_config_path = "samples/test_node_config.yaml"
        config_path = "samples/dummy_node_config.yaml"

        # reading test config from sample
        test_config = read_yaml(test_config_path)
        # updating one of the main config value
        test_config["infer_filters"]["value"][1]["length_breadth_filter"]["length_threshold"]["value"] = 24
        # writing updated yaml to samples folder
        write_yaml(test_config_path, test_config)
        # writing updated yaml to test results folder for loading to config class
        write_yaml(config_path, test_config)
        # creating config object and writing the updating config
        NodeConfig(module_name, config_path)
        # asserting if updated config is same as test config
        test_config = read_yaml(test_config_path)
        updated_config = read_yaml(config_path)
        assert test_config == updated_config, "Updated config is not equal to test config"


if __name__ == "__main__":
    test_obj = TestNodeConfig()
