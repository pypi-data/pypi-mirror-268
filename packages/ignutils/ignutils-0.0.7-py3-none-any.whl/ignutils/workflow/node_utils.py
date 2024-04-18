""" for node util functions"""
import os
import random
from ignutils.json_utils import check_label_json
from ignutils.file_utils import change_extn
from ignutils.img_utils import do_sometimes
from ignutils.active_augmentation import ActiveAug


def get_labels(node_config_obj):
    """To get all the classes and colabels"""
    labels = []
    classes = node_config_obj("classes")
    for index, classname in enumerate(classes):
        labels.append(classname)
        labels.extend(classes[classname]["co_labels"])
    return list(set(labels))

def check_active_aug_enabled(node_config_obj):
    """To check whether foreground or background augmentation is enabled"""
    for aug_info in node_config_obj("active_augmentation"):
        aug_name = list(aug_info.keys())[0]
        if aug_info[aug_name]["enabled"]:
            return True
    return False

def get_bg_aug_labels(node_config_obj):
    """To check whether background augmentation is enabled"""
    aug_labels = []
    for aug_info in node_config_obj("active_augmentation"):
        aug_name = list(aug_info.keys())[0]
        if aug_name == 'Background' and aug_info[aug_name]["enabled"]:
            aug_labels = aug_info[aug_name]["bg_aug_labelnames"]["value"]
    return aug_labels


def get_active_aug(img, json_dict, dump_path, node_config_obj, fulldb_path):
    """do active augmentation"""
    # add bg or fg active augmentation
    for aug_info in node_config_obj("active_augmentation"):
        aug_name = list(aug_info.keys())[0]
        aug_enabled = aug_info[aug_name]["enabled"]
        if aug_enabled and dump_path is not None:
            aug_probability = aug_info[aug_name]["aug_probability"]["value"]
            if do_sometimes(aug_probability):
                mode = aug_name
                active_aug_obj = ActiveAug(node_config_obj, dump_path, fulldb_path)
                img, json_dict = active_aug_obj.active_augmentation(img, json_dict, mode)
    return img, json_dict


def get_tiling_info(node_config):
    """Get tiling related fileds as a dict"""
    tiling_info_dict = {}
    tiling_info_dict['tiling_mode'] = node_config('tiling_mode')
    tiling_info_dict['tile_x_split'] = node_config('tile_x_split')
    tiling_info_dict['tile_y_split'] = node_config('tile_y_split')
    tiling_info_dict['tile_h'] = node_config('tile_h')
    tiling_info_dict['tile_w'] = node_config('tile_w')
    tiling_info_dict['overlap_x'] = node_config('overlap_x')
    tiling_info_dict['overlap_y'] = node_config('overlap_y')
    tiling_info_dict['vertical_first'] = node_config('vertical_first_flag')
    tiling_info_dict['model_input_HW'] = node_config('model_input_HW')
    return tiling_info_dict

def get_files(files_list, folder):
    """Returns updated files list with files in given folder"""
    updated_files_list = []
    for file in files_list:
        file_dirname = os.path.dirname(file)
        if folder in file_dirname.split('/'):
            updated_files_list.append(file)
    return updated_files_list

def get_positive_negative_files(files_list, node_obj): #rename
    """filter inp files list based on positive and negative classes"""
    train_split_list = ['train', 'val', 'test'] #Rename
    final_list = []
    for ind,split_folder in enumerate(train_split_list):
        pos_list = [] #files with positiv colabels
        neg_list = [] #files with neg co labels
        empty_list = [] # files with no positive or neg co labels
        split_files = get_files(files_list, split_folder)
        for img_file in split_files:
            json_file = change_extn(img_file, extn=".json")
            pos_labels = get_labels(node_obj)
            neg_labels = node_obj("negative_co_labels")
            if check_label_json(json_file, pos_labels):
                pos_list.append(img_file)
            elif check_label_json(json_file, neg_labels):
                neg_list.append(img_file)
            else:
                empty_list.append(img_file)

        #check no of files meets the neg dump criteria
        empty_percent = node_obj("neg_dump_criteria").get("empty_percentage")[ind]/100
        neg_percent = node_obj("neg_dump_criteria").get("neg_co_label_percentage")[ind]/100
        pos_count = len(pos_list)
        available_neg_count = len(neg_list)
        availabe_empty_count = len(empty_list)
        required_neg_count = int(neg_percent * pos_count)
        required_empty_count = int(empty_percent * pos_count)
        if available_neg_count > 0:
            neg_list = random.sample(neg_list, min(available_neg_count, required_neg_count))
        if availabe_empty_count > 0:
            empty_list = random.sample(empty_list, min(availabe_empty_count, required_empty_count))
        split_file_list = pos_list + neg_list + empty_list
        final_list.extend(split_file_list)
    return final_list
