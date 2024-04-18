""" Active augmenation related functions"""
import os
import os.path as osp
import random
import unittest
from copy import deepcopy
import glob
import tqdm

import cv2
import imutils
import numpy as np
from shapely.geometry import Polygon

from ignutils.clone_utils import CloneRepo
from ignutils.file_utils import get_all_files, check_folder_exists, create_directory_safe
from ignutils.json_utils import read_json, write_json
from ignutils.img_utils import find_cv_contours, rotate_bound, do_sometimes
from ignutils.draw_utils import draw_polylines
from ignutils.contour_utils import rescale_json, rotate_json, bbox_crop_json, lab2cv
import ignutils as icv
from ignutils.workflow.node_config import NodeConfig
from ignutils.labelme_utils import upgrade_label_json, create_labelme_json, create_shape_dict


class ActiveAug:
    """Class for generating augmented images"""

    # config alone in input
    def __init__(self, config, workspace, full_db_path):
        self.workspace = workspace
        self.full_db_path = full_db_path
        self.config = config
        for aug_info in config("active_augmentation"):
            aug_name = list(aug_info.keys())[0]
            if aug_name == "Foreground":
                self.node_vs_non_node_aug_percent = aug_info[aug_name]["activeaug_node_vs_non_node_percent"]["value"]
                self.aug_neg_crop_label = aug_info[aug_name]["activeaug_negative_crop_labelnames"]["value"]
                self.aug_non_node_crop_label = aug_info[aug_name]["activeaug_non_node_crop_labelnames"]["value"]
                self.parent_node = config("parent_contour")
                self.training_node = config("node_name")
                self.aug_negative_crop_add_mode = aug_info[aug_name]["activeaug_negative_crop_add_mode"]["value"]  # to add negative crop inside or outside the parent contour
                self.activeaug_non_node_crop_branchname = aug_info[aug_name]["activeaug_non_node_crop_branchname"]["value"]
                self.activeaug_node_crop_branchname = aug_info[aug_name]["activeaug_node_crop_branchname"]["value"]
                self.aug_neg_crop_branchname = aug_info[aug_name]["activeaug_negative_crop_branchname"]["value"]
            if aug_name == "Background":
                self.bg_aug_branchname = aug_info[aug_name]["bg_db_branch_name"]["value"]
                self.bg_aug_labels = aug_info[aug_name]["bg_aug_labelnames"]["value"]
        self.positive_data_counter = random.randint(1, 2)
        self.negative_data_counter = random.randint(1, 2)
        self.aug_nodes_list = []
        for index, classname in enumerate(self.config("classes")):
            self.aug_nodes_list.extend(self.config("classes")[classname]["co_labels"])
            if self.aug_neg_crop_label is not None:
                self.aug_nodes_list.extend(self.aug_neg_crop_label)
            if self.aug_non_node_crop_label is not None:
                self.aug_nodes_list.extend(self.aug_non_node_crop_label)
        self.clone_aug_defects()

    def dump_aug_node_crops(self, node_names_list, inp_folderpath, result_folderpath):
        """Dump image crops for augmentation from inp folderpath based on node_names_list.

        Args:
            node_names_list (list): list of labelnames used for dumping image crops.
            inp_folderpath (str): input folder path for full images and labels.
            result_folderpath (_type_): output folderpath where crops and labels are being dumped
        """
        for root, _, files in os.walk(inp_folderpath):
            for json_index, f in enumerate(tqdm.tqdm(files)):
                json_file = os.path.join(root, f)
                if not json_file.endswith(".json") or osp.isfile(json_file) is False:
                    continue
                json_dict = read_json(json_file)

                image_file_name = osp.basename(json_dict.get("imagePath"))
                image_path = osp.join(root, image_file_name)

                if not osp.isfile(image_path):
                    continue
                image = cv2.imread(image_path)
                mask = np.zeros_like(image)
                mask_copy = mask.copy()

                for i, cntr_dict in enumerate(json_dict["shapes"]):
                    label = cntr_dict["label"]
                    json_dict_crop = create_labelme_json()
                    if label in node_names_list:
                        shape_contours = cntr_dict["points"]
                        mask = draw_polylines(mask_copy.copy(), shape_contours, color=[255,255,255])
                        org_contours = find_cv_contours(mask)
                        org_contours = lab2cv(org_contours[0])
                        x1, y1, w1, h1 = cv2.boundingRect(org_contours)
                        if w1 < 50 or h1 < 50:
                            continue
                        org_mask = mask.copy()
                        kernel = np.ones([100, 100], np.uint8)
                        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)
                        expanded_contours = find_cv_contours(mask)
                        expanded_contours = lab2cv(expanded_contours[0])
                        mask = cv2.fillPoly(mask_copy.copy(), expanded_contours, [255, 255, 255])
                        x, y, w, h = cv2.boundingRect(expanded_contours)
                        image_crop = image[y : y + h, x : x + w]
                        mask_crop = org_mask[y : y + h, x : x + w]

                        expanded_crop_contours = find_cv_contours(mask_crop)
                        new_dict = create_shape_dict(label=label, points=expanded_crop_contours[0], fill_color=[0, 255, 0], overlay_mode="outerline")
                        name = os.path.splitext(image_file_name)[0]
                        image_crop_filename = os.path.join(result_folderpath, f"{name}_{i}.jpg")
                        cv2.imwrite(image_crop_filename, image_crop)
                        json_file_name = os.path.join(result_folderpath, f"{name}_{i}.json")
                        json_dict_crop["imagePath"] = os.path.basename(image_crop_filename)
                        json_dict_crop["imageHeight"] = image_crop.shape[0]
                        json_dict_crop["imageWidth"] = image_crop.shape[1]
                        json_dict_crop["shapes"].append(new_dict)
                        write_json(json_file_name, json_dict_crop)

    def clone_aug_defects(self):
        """Clone node, non-node and negative child crops if available else dump."""

        for aug_info in self.config("active_augmentation"):
            aug_name = list(aug_info.keys())[0]
            if aug_name == "Foreground" and aug_info[aug_name]["enabled"]:
                activeaug_non_node_crop_branchname = aug_info[aug_name]["activeaug_non_node_crop_branchname"]["value"]
                activeaug_node_crop_branchname = aug_info[aug_name]["activeaug_node_crop_branchname"]["value"]
                activeaug_neg_crop_branchname = aug_info[aug_name]["activeaug_negative_crop_branchname"]["value"]
                activeaug_non_node_full_db_branchname = aug_info[aug_name]["activeaug_non_node_fulldb_branchname"]["value"]

                if not activeaug_non_node_crop_branchname and not activeaug_node_crop_branchname and not activeaug_neg_crop_branchname:
                    return
                if activeaug_non_node_crop_branchname is not None:
                    activeaug_non_node_crop_folder = os.path.join(self.workspace, activeaug_non_node_crop_branchname)
                    if check_folder_exists(activeaug_non_node_crop_folder) is False:
                        CloneRepo("https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db/", activeaug_non_node_crop_branchname, activeaug_non_node_crop_folder, access_token_name="DB_CLONE_TOKEN")
                    if aug_info[aug_name]["dump_positive_aug_crops"]["value"]:
                        CloneRepo(
                            "https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db/",
                            activeaug_non_node_full_db_branchname,
                            os.path.join(self.workspace, "non_node_full_db"),
                        )
                        non_node_labels = aug_info[aug_name]["activeaug_non_node_crop_labelnames"]
                        self.dump_aug_node_crops(non_node_labels, os.path.join(self.workspace, "non_node_full_db"), activeaug_non_node_crop_folder)

                if activeaug_node_crop_branchname is not None:
                    activeaug_node_crop_folder = os.path.join(self.workspace, activeaug_node_crop_branchname)
                    if check_folder_exists(activeaug_node_crop_folder) is False:
                        CloneRepo(
                            "https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db/",
                            activeaug_node_crop_branchname,
                            activeaug_node_crop_folder,
                        )
                    if aug_info[aug_name]["dump_positive_aug_crops"]["value"]:
                        aug_classes = self.config("classes")
                        aug_labels = icv.workflow.node_utils.get_labels(self.config)
                        aug_labels.extend(x for x in aug_info[aug_name]["activeaug_positive_crop_labelnames"]["value"] if x not in aug_labels)
                        self.dump_aug_node_crops(aug_labels, self.full_db_path, activeaug_node_crop_folder)

                if activeaug_neg_crop_branchname is not None:
                    neg_aug_folder = os.path.join(self.workspace, activeaug_neg_crop_branchname)
                    if check_folder_exists(neg_aug_folder) is False:
                        CloneRepo(
                            "https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db/",
                            activeaug_neg_crop_branchname,
                            neg_aug_folder,
                        )
                    if aug_info[aug_name]["dump_negative_aug_crops"]["value"]:
                        self.dump_aug_node_crops(aug_info[aug_name]["activeaug_negative_crop_labelnames"]["value"], self.full_db_path, neg_aug_folder)

            if aug_name == "Background" and aug_info[aug_name]["enabled"]:
                bg_aug_branchname = aug_info[aug_name]["bg_db_branch_name"]["value"]
                bg_aug_folder = os.path.join(self.workspace, bg_aug_branchname)
                if check_folder_exists(bg_aug_folder) is False:
                    CloneRepo(
                        "https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db/",
                        bg_aug_branchname,
                        bg_aug_folder,
                    )



    def active_augmentation(self, bg_img, bg_json_dict, mode):
        """Given an input image and json function returns a new image and json with foreground 
        crop added on it, foreground crops may be from positive (node crops and non node crops)
        and negative folders given, No. of crops added is based on the positive and negative counter.
        Returns:
            bg_img: input image
            bg_json_dict: json dict of bg_img
        """
        if mode == "Foreground":
            data_added_flag = False
            for _ in range(10):  #  try 10 times to add crops
                # import pdb;pdb.set_trace()
                if self.positive_data_counter != 0:
                    if self.activeaug_non_node_crop_branchname is not None or self.activeaug_node_crop_branchname is not None:
                        fg_img, fg_pos_dict = self.get_random_positive_img()
                        bg_img, bg_json_dict, data_added_flag = self.add_aug_img(bg_img, bg_json_dict, fg_img, fg_pos_dict)
                    if data_added_flag:
                        self.positive_data_counter -= 1
                if self.negative_data_counter != 0:
                    if self.aug_neg_crop_branchname is not None:
                        fg_img, fg_neg_dict = self.get_random_negative_img()
                        bg_img, bg_json_dict, data_added_flag = self.add_aug_img(bg_img, bg_json_dict, fg_img, fg_neg_dict)
                    if data_added_flag:
                        self.negative_data_counter -= 1
                if (self.positive_data_counter == 0) and (self.negative_data_counter == 0):  # if positive and negativecrops added break
                    break
        if mode == "Background":
            bg_img, bg_json_dict = self.background_augmentation(bg_img, json_dict=bg_json_dict)

        return bg_img, bg_json_dict

    def get_random_positive_img(self):
        """Get a random img/json from node crop folder or non node crop folder
        positive_node_crop_folder: folderpath of node crop
        positive_non_node_crop_folder: folderpath of non node crop
        Returns:
            image, fg_pos_dict: positive image, its json file
        """
        image = None
        fg_pos_dict = None
        positive_node_crop_files = []
        positive_non_node_crop_files = []

        if self.activeaug_node_crop_branchname is not None:
            aug_node_crop_folder = os.path.join(self.workspace, self.activeaug_node_crop_branchname)
            if check_folder_exists(aug_node_crop_folder) is False:
                CloneRepo(
                    "https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db/",
                    self.activeaug_node_crop_branchname,
                    aug_node_crop_folder,
                )

            positive_node_crop_files = get_all_files(
                aug_node_crop_folder,
                include_extns=[".json"],
            )
            random_file = random.choice(positive_node_crop_files)
        if self.activeaug_non_node_crop_branchname is not None:
            aug_non_node_crop_folder = os.path.join(self.workspace, self.activeaug_non_node_crop_branchname)
            if check_folder_exists(aug_non_node_crop_folder) is False:
                CloneRepo(
                    "https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db/",
                    self.activeaug_non_node_crop_branchname,
                    aug_non_node_crop_folder,
                )
            positive_non_node_crop_files = get_all_files(
                aug_non_node_crop_folder,
                include_extns=[".json"],
            )
            random_file = random.choice(positive_non_node_crop_files)
        random_num = random.randint(0, 100)
        if self.activeaug_non_node_crop_branchname is not None and self.activeaug_node_crop_branchname is not None:
            # random percent to switch between  real defects (from parent  itself) and other defects based on threshold percent from config
            if random_num <= self.node_vs_non_node_aug_percent:
                random_file = random.choice(positive_node_crop_files)
            else:
                random_file = random.choice(positive_non_node_crop_files)

        file = os.path.basename(random_file)
        if random_file in positive_node_crop_files:
            json_file = os.path.join(aug_node_crop_folder, file)
            json_folder = aug_node_crop_folder
        elif random_file in positive_non_node_crop_files:
            json_file = os.path.join(aug_non_node_crop_folder, file)
            json_folder = aug_non_node_crop_folder

        if json_file.endswith(".json") and osp.isfile(json_file) is True:
            json_dict = read_json(json_file)
            image_file_name = osp.basename(json_dict.get("imagePath"))
            image_path = osp.join(json_folder, image_file_name)
        image = cv2.imread(image_path)
        for shapes in json_dict["shapes"]:
            if shapes["label"] in self.aug_nodes_list:
                fg_pos_dict = shapes
                return image, fg_pos_dict
        return image, fg_pos_dict

    def get_random_negative_img(self):
        """Get random negative img/json
        negative_crop_folder: folderpath of negative image crops
        Returns:
            image, fg_neg_dict: negative image, its json file
        """
        image = None
        fg_neg_dict = None
        aug_neg_crop_folder = os.path.join(self.workspace, self.aug_neg_crop_branchname)
        if check_folder_exists(aug_neg_crop_folder) is False:
            CloneRepo(
                "https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db/",
                self.aug_neg_crop_branchname,
                aug_neg_crop_folder,
            )
        total_neg_files = get_all_files(
            aug_neg_crop_folder,
            include_extns=[".json"],
        )
        random_file = random.choice(total_neg_files)
        file = os.path.basename(random_file)
        json_file = os.path.join(aug_neg_crop_folder, file)
        json_dict = read_json(json_file)
        image_file_name = osp.basename(json_dict.get("imagePath"))
        image_path = osp.join(aug_neg_crop_folder, image_file_name)
        image = cv2.imread(image_path)
        for shapes in json_dict["shapes"]:
            if shapes["label"] in self.aug_nodes_list:
                fg_neg_dict = shapes
                return image, fg_neg_dict
        return image, fg_neg_dict

    def add_aug_img(self, bg_img, bg_json_dict, fg_img, fg_cntr_dict):
        """Generate result image and json with fg_image added on bg_image using seamless clone
        Args:
            bg_img: background image
            bg_json_dict: json info of bg_image
            fg_img: foregroung image crop to be placed on bg_img
            fg_cntr_dict: contour info from fg_img
        Results:
            bg_img, result_json, aug_img_added_flag: result aug image, its json, flag indicating if aug is done or not
        """
        img_copy = bg_img.copy()
        i = 0
        result_json = bg_json_dict
        aug_img_added_flag = False

        for shapes in bg_json_dict["shapes"]:  # taking parent info
            if self.parent_node is not None:
                if shapes["label"] == self.parent_node:
                    parent_contour = shapes["points"]

        if self.parent_node is None:
            parent_contour = [[0, 0], [0, bg_img.shape[1]], [bg_img.shape[1], bg_img.shape[0]], [0, bg_img.shape[0]]]

        mask = np.zeros_like(fg_img)
        mask_copy = deepcopy(mask)
        H = bg_img.shape[0]
        W = bg_img.shape[1]
        parent_contour_ = np.array(parent_contour).reshape((-1, 1, 2)).astype(np.int32)
        rect = cv2.minAreaRect(parent_contour_)
        parent_length = max(rect[1])
        parent_breadth = min(rect[1])
        if fg_cntr_dict is None or fg_img is None:
            return bg_img, result_json, aug_img_added_flag
        m = 0
        while m <= 5:
            angle = random.randint(0, 360)
            # defect_label = fg_cntr_dict["label"]
            shape_contours = fg_cntr_dict["points"]
            shape_contours = np.array(shape_contours)
            shape_contours_ = shape_contours.reshape((-1, 1, 2)).astype(np.int32)
            rect = cv2.minAreaRect(shape_contours_)
            contour_area = cv2.contourArea(shape_contours_)
            length = max(rect[1])
            breadth = contour_area / length

            mask = cv2.fillPoly(
                mask_copy.copy(),
                [shape_contours.astype(int)],
                [255, 255, 255],
            )
            org_mask = deepcopy(mask)
            kernel = np.ones([15, 15], np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)
            expanded_contours = find_cv_contours(mask)
            expanded_contours = [lab2cv(cnt) for cnt in expanded_contours]
            mask = cv2.fillPoly(
                mask_copy.copy(),
                [expanded_contours[0].astype(int)],
                [255, 255, 255],
            )
            x, y, w, h = cv2.boundingRect(np.array(expanded_contours[0]).astype(np.int))
            if w < 50 or h < 50:
                # print("not enough big ")
                return bg_img, result_json, aug_img_added_flag
            mask_crop = mask[y : y + h, x : x + w]
            image_crop = fg_img[y : y + h, x : x + w]
            org_mask_crop = org_mask[y : y + h, x : x + w]

            # apply random rotation
            image_crop = imutils.rotate_bound(image_crop, angle)
            mask_crop = imutils.rotate_bound(mask_crop, angle)
            org_mask_crop = imutils.rotate_bound(org_mask_crop, angle)
            mask_h, mask_w = mask_crop.shape[:2]
            random_scale_ratio = random.uniform(parent_breadth * 0.1, parent_breadth * 0.3)

            scale = random_scale_ratio / mask_w
            if mask_w > parent_breadth * 0.2:
                scale = 0.75
            elif mask_w < 50:
                scale = 1
            # apply random scaling
            image_crop = cv2.resize(image_crop, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
            mask_crop = cv2.resize(mask_crop, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
            org_mask_crop = cv2.resize(org_mask_crop, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
            target_point = self.get_random_point_from_parent(image_crop, fg_cntr_dict, bg_img, parent_contour)
            if target_point is None:
                return bg_img, result_json, aug_img_added_flag
            kernel1 = np.ones([3, 3], np.uint8)
            # org_mask_crop = cv2.morphologyEx(org_mask_crop, cv2.MORPH_DILATE, kernel1)
            mono_mask_image = cv2.split(mask_crop)[0]  # reducing the mask to a monochrome
            br = cv2.boundingRect(mono_mask_image)  # bounding rect (x,y,width,height)
            image_crop = image_crop[br[1] : br[1] + br[3], br[0] : br[0] + br[2]]
            mask_crop = mask_crop[br[1] : br[1] + br[3], br[0] : br[0] + br[2]]
            org_mask_crop = org_mask_crop[br[1] : br[1] + br[3], br[0] : br[0] + br[2]]
            overlap_flag, aug_cntr = self.check_overlap(org_mask_crop, fg_cntr_dict["label"], bg_img, bg_json_dict, target_point)
            if overlap_flag:
                m += 1
            else:
                aug_img_added_flag = True
                break
        if overlap_flag:
            return bg_img, result_json, aug_img_added_flag

        bg_img = cv2.seamlessClone(image_crop, img_copy, mask_crop, target_point, cv2.NORMAL_CLONE)
        label = fg_cntr_dict["label"]
        # result_json = self.dump_json_dict(
        #     bg_json_dict,
        #     bg_img,
        #     label,
        #     aug_cntr,
        # )
        result_json = self.dump_json_dict(bg_json_dict,label,aug_cntr,)
        return bg_img, result_json, aug_img_added_flag

    def get_random_point_from_parent(self, fg_img_crop, fg_cntr_dict, bg_img, parent_contour):
        """Get random point from parent contour to place positive or negative aug crop.
        If positive place inside parent else depends on aug_negative_crop_add_mode to place 
        the neg crop.
        Args:
            fg_img_crop (img): foreground image crop to be placed
            fg_cntr_dict (dict): foreground contour info
            bg_img (img): background image
            parent_contour (numpy array): parent contour
        Returns:
            point: random point inside the parent contour
        """
        max_x = bg_img.shape[1] - fg_img_crop.shape[1] // 2
        max_y = bg_img.shape[0] - fg_img_crop.shape[0] // 2
        i = 0
        while i < 5:  # if no position found try sometimes else continue
            try:
                x = np.random.randint(fg_img_crop.shape[1] // 2, max_x)
                y = np.random.randint(fg_img_crop.shape[0] // 2, max_y)
            except:
                return None
            target_point = x, y
            end_y = y + fg_img_crop.shape[0] // 2
            start_y = y - fg_img_crop.shape[0] // 2
            start_x = x - fg_img_crop.shape[1] // 2
            end_x = x + fg_img_crop.shape[1] // 2
            target_polygon = Polygon([[start_x, start_y], [end_x, start_y], [end_x, end_y], [start_x, end_y]])
            parent_polygon = Polygon(parent_contour)
            target_polygon = target_polygon.buffer(0)
            parent_polygon = parent_polygon.buffer(0)
            if self.parent_node is None and fg_cntr_dict["label"] not in self.aug_neg_crop_label:
                # return target_point
                break
            if fg_cntr_dict["label"] not in self.aug_neg_crop_label:
                if parent_polygon.contains(target_polygon):
                    # return target_point
                    break
                i += 1
            elif fg_cntr_dict["label"] in self.aug_neg_crop_label:
                if self.aug_negative_crop_add_mode == "outside":
                    if (not parent_polygon.contains(target_polygon)) and (not target_polygon.overlaps(parent_polygon)):
                        # return target_point
                        break
                    i += 1
                elif self.aug_negative_crop_add_mode == "inside":
                    if parent_polygon.contains(target_polygon):
                        # return target_point
                        break
                    i += 1
                elif self.aug_negative_crop_add_mode == "anywhere":
                    if parent_polygon.contains(target_polygon) or not parent_polygon.intersects(target_polygon):
                        # return target_point
                        break
                    i += 1
            if fg_cntr_dict["label"] not in self.aug_neg_crop_label and not parent_polygon.contains(target_polygon):
                return None
            if fg_cntr_dict["label"] in self.aug_neg_crop_label and self.aug_negative_crop_add_mode == "inside" and not parent_polygon.contains(target_polygon):
                return None
            if fg_cntr_dict["label"] in self.aug_neg_crop_label and self.aug_negative_crop_add_mode == "outside" and parent_polygon.contains(target_polygon):
                return None
            if fg_cntr_dict["label"] in self.aug_neg_crop_label and self.aug_negative_crop_add_mode == "anywhere" and (not parent_polygon.contains(target_polygon) and parent_polygon.intersects(target_polygon)):
                return None
        return target_point

    def scale_contour(self, cnt, scale):
        """Scale the input contour to the scale provided
        Returns:
            cnt_scaled: Scaled contour
        """
        cnt = np.array(cnt)
        m = cv2.moments(cnt)
        cx = int(m["m10"] / m["m00"])
        cy = int(m["m01"] / m["m00"])
        cnt_norm = cnt - [cx, cy]
        cnt_scaled = cnt_norm * scale
        cnt_scaled = cnt_scaled + [cx, cy]
        cnt_scaled = cnt_scaled.astype(np.int32)
        return cnt_scaled

    def scale_json_cntrs(self, json_dict, scale, labels):
        """Scale contours in cntours list and create a scaled 
        json dict contours with label in labels.
        Returns:
            rescaled_contour_list, json_dict:  Scaled contour list, json file
        """
        shapes = json_dict["shapes"]
        shapes_copy = deepcopy(json_dict)
        new_json_dict = upgrade_label_json(json_dict)
        rescaled_contour_list = []
        for shape in shapes_copy:
            if shape["label"] in labels:
                cntr = shape["points"]
                rescaled_cntr = self.scale_contour(cntr, scale)
                shape["points"] = rescaled_cntr
                new_json_dict["shapes"].append(shape)
                rescaled_contour_list.append(rescaled_cntr)
        return rescaled_contour_list, json_dict

    def background_augmentation(
        self,
        image,
        json_dict=None,
    ):
        """Generate background changed image"""

        new_bg_image = image
        bg_aug_folder = os.path.join(self.workspace, self.bg_aug_branchname)
        org_dim = image.shape[:2]
        if check_folder_exists(bg_aug_folder) is False:
            CloneRepo(
                "https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db/",
                self.bg_aug_branchname,
                bg_aug_folder,
            )
        bg_img_list = get_all_files(bg_aug_folder, include_type="image")
        bg_img_ = random.choice(bg_img_list)
        bg_img = cv2.imread(bg_img_)

        parent_list = [self.parent_node]
        req_labels = self.aug_nodes_list + parent_list + self.bg_aug_labels + self.aug_nodes_list
        new_bg_image, json_dict = self.create_bg_aug(bg_img, image, json_dict, req_labels, preserve_boundary_touch=True)

        return new_bg_image, json_dict


    def make_bg_image_ready(self, bg_img, fg_img):
        """Return bg img dim same as fg image"""
        bg_img_h, bg_img_w = bg_img.shape[:2]
        fg_img_h, fg_img_w = fg_img.shape[:2]
        if bg_img_h > fg_img_h and bg_img_w > fg_img_w:
            x_diff = bg_img_w - fg_img_w
            y_diff = bg_img_h - fg_img_h
            x1 = random.randint(0, x_diff)
            y1 = random.randint(0, y_diff)
            bg_img = bg_img[y1:y1+fg_img_h, x1:x1+fg_img_w]
        else:
            bg_img = cv2.resize(bg_img, (fg_img_w, fg_img_h), interpolation=cv2.INTER_AREA)
        return bg_img

    def change_background(self, bg_img, fg_img, fg_json, labels):
        """change fg img background with bg img, preserving contours with req labels"""
        shapes = fg_json["shapes"]
        drawing = np.zeros((fg_img.shape[0], fg_img.shape[1], 3), np.uint8)
        for shape in shapes:
            if shape["label"] in labels:
                contourpts = shape["points"]
                drawing = draw_polylines(drawing, contourpts, fill=True, color=[255, 255, 255])
        bg_img = self.make_bg_image_ready(bg_img, fg_img)
        drawing_not = cv2.bitwise_not(drawing)
        im_ = cv2.bitwise_and(bg_img, drawing_not)
        im1 = cv2.bitwise_and(fg_img, drawing)
        new_bg_image = cv2.add(im1, im_)
        return new_bg_image, fg_json

    def rescale_img_json(self, img, json, scale, max_dim):
        """Rescale image and json, not exceeding max limit"""
        rescaled_img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
        max_wd, max_ht = max_dim
        rescaled_ht, rescaled_wd = rescaled_img.shape[:2]
        if rescaled_ht > max_ht:
            rescaled_img = cv2.resize(img, (rescaled_wd, max_ht), interpolation=cv2.INTER_NEAREST)
        if rescaled_wd > max_wd:
            rescaled_img = cv2.resize(img, (max_wd, rescaled_ht), interpolation=cv2.INTER_NEAREST)
        if rescaled_ht > max_ht and rescaled_wd > max_wd:
            rescaled_img = cv2.resize(img, (max_wd, max_ht), interpolation=cv2.INTER_NEAREST)
        org_ht, org_wd = img.shape[:2]
        rescaled_ht, rescaled_wd = rescaled_img.shape[:2]
        rescaled_json = rescale_json(json, org_ht, org_wd, rescaled_ht, rescaled_wd)
        return rescaled_img, rescaled_json

    def crop_rescale_img_json(self, img, json_dict, scale, max_dim, left_touch, right_touch, top_touch, bottom_touch):
        """crop and scale image / json

        Args:
            img : inp img
            json : inp json
            scale : rescale factor
            max_dim : max allowed dim to rescale
            left_touch : if true, crop from left
            right_rouch : if true, crop from right
            top_touch : if true crop from top
            bottom_touch : if true, crop from bottom
        """
        rescaled_img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
        max_wd, max_ht = max_dim
        img_ht, img_wd = img.shape[:2]
        rescaled_ht, rescaled_wd = rescaled_img.shape[:2]
        crop_fraction = random.uniform(0.1, 0.4)
        crop_prob = random.uniform(0, 1)
        img_crop = img.copy()
        if rescaled_ht > max_ht:
            crop_y = int(min(img_ht * crop_fraction, 50))
            if top_touch:
                img_crop = img[crop_y:img_ht, :]
            if bottom_touch:
                img_crop = img[0 : img_ht - crop_y, :]
            if top_touch and bottom_touch:
                if do_sometimes(crop_prob):
                    img_crop = img[crop_y:img_ht, :]
                else:
                    img_crop = img[0 : img_ht - crop_y, :]
        if rescaled_wd > max_wd:
            crop_x = min(img_wd * crop_fraction, 50)
            if left_touch:
                img_crop = img[:, crop_x:img_wd]
            if right_touch:
                img_crop = img[:, 0 : img_wd - crop_x]
            if left_touch and right_touch:
                if do_sometimes(crop_prob):
                    img_crop = img[:, crop_x:img_wd]
                else:
                    img_crop = img[:, 0 : img_wd - crop_x]

        crop_json = bbox_crop_json(json_dict, ((0, 0), (img_crop.shape[1], img_crop.shape[0])))
        if "checksum" in json_dict.keys():
            crop_json["checksum"] = json_dict["checksum"]
        if "org_dim" in json_dict.keys():
            crop_json["org_dim"] = json_dict["org_dim"]
        rescaled_img, rescaled_json = self.rescale_img_json(img_crop, crop_json, scale, max_dim=max_dim)
        return rescaled_img, rescaled_json

    def get_node_area(self, img, json_dict, labels):
        """Find area of contours having label in labels list"""
        shapes = json_dict["shapes"]
        mask = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
        for shape in shapes:
            if shape["label"] in labels:
                contourpts = shape["points"]
                mask = draw_polylines(mask, contourpts, fill=True, color=[255, 255, 255])
        contours = find_cv_contours(mask)
        area = [cv2.contourArea(np.array(contour)) for contour in contours]
        return max(area)

    def create_bg_aug(self, bg_img, fg_img, json_dict, labels, preserve_boundary_touch=False):
        """change background of image while keeping contours in fg_cntrs_list"""
        ht, wd = fg_img.shape[:2]
        bg_img = self.make_bg_image_ready(bg_img, fg_img)

        scale = random.uniform(0.7, 1.2)
        angle = random.randint(0, 100)
        left_touch, right_touch, top_touch, bottom_touch = False, False, False, False

        # crop based on min max xy
        min_x, min_y, max_x, max_y = self.get_min_max(json_dict, labels)
        if min_x is None:
            return fg_img, json_dict
        original_node_area = self.get_node_area(fg_img, json_dict, labels)
        crop_fg_img = fg_img[min_y:max_y, min_x:max_x]
        crop_fg_json = bbox_crop_json(json_dict, ((min_x, min_y), (max_x, max_y)))
        if "checksum" in json_dict.keys():
            crop_fg_json["checksum"] = json_dict["checksum"]
        if "org_dim" in json_dict.keys():
            crop_fg_json["org_dim"] = json_dict["org_dim"]

        if self.parent_node is not None:  # if parent node is there just chnage background
            new_bg_image, json_dict = self.change_background(bg_img, fg_img, json_dict, labels)
            return new_bg_image, json_dict

        if not preserve_boundary_touch:
            # Rotate crop Image and json
            rotated_image, rot_matrix = rotate_bound(crop_fg_img, angle)
            rotated_json = rotate_json(crop_fg_json, rot_matrix)

            # resize Image and json
            rescaled_fg_img, rescaled_json = self.rescale_img_json(rotated_image, rotated_json, scale, max_dim=(wd, ht))

            # Place fg crop on bg image
            new_bg_image, json_dict = self.place_fgimg(bg_img, rescaled_fg_img, rescaled_json, labels)
        else:
            ##check if crop is top bottom left right touching
            if min_x is None:
                return fg_img, json_dict
            if min_x == 0:
                left_touch = True
            if max_x == wd:
                right_touch = True
            if min_y == 0:
                top_touch = True
            if max_y == ht:
                bottom_touch = True

            if (top_touch and bottom_touch) or (left_touch and right_touch):
                scale = random.uniform(1, 1.2)

            target_x, target_y = None, None
            rescaled_fg_img, rescaled_json = self.rescale_img_json(crop_fg_img, crop_fg_json, scale, max_dim=(wd, ht))
            # rescaled_fg_img, rescaled_json = self.crop_rescale_img_json(crop_fg_img, crop_fg_json, scale, max_dim=(wd, ht), left_touch=left_touch, right_touch=right_touch, top_touch=top_touch, bottom_touch=bottom_touch)
            rescaled_ht, rescaled_wd = rescaled_fg_img.shape[:2]

            # Choose target x, y and crop from top/bottom or left/right based on touch
            if left_touch:
                target_x = 0
            elif right_touch:
                target_x = bg_img.shape[1] - rescaled_wd
            elif top_touch:
                target_y = 0
            elif bottom_touch:
                target_y = bg_img.shape[0] - rescaled_ht

            # place fg crop on bg image
            new_bg_image, json_dict = self.place_fgimg(bg_img, rescaled_fg_img, rescaled_json, labels, target_x=target_x, target_y=target_y)
        final_node_area = self.get_node_area(new_bg_image, json_dict, labels)
        assert final_node_area > 0.2 * original_node_area, "Foreground area of curr node is very small"
        return new_bg_image, json_dict

    def get_min_max(self, json_dict, labels):
        """Loop thru json dict shapes and find min x miny and max x max y of all contour"""
        min_x_list = []
        max_x_list = []
        min_y_list = []
        max_y_list = []
        shapes = json_dict["shapes"]
        for shape in shapes:
            if shape["label"] in labels:
                contourpts = shape["points"]
                contourpts = lab2cv(contourpts)
                x, y, w, h = cv2.boundingRect(contourpts)
                min_x = x
                min_y = y
                max_x = x + w
                max_y = y + h
                min_x_list.append(min_x)
                max_x_list.append(max_x)
                min_y_list.append(min_y)
                max_y_list.append(max_y)
        if not min_x_list:
            return None, None, None, None
        min_x = min(min_x_list)
        max_x = max(max_x_list)
        min_y = min(min_y_list)
        max_y = max(max_y_list)
        return min_x, min_y, max_x, max_y

    def place_fgimg(self, bg_img, fg_img, fg_json, labels, target_x=None, target_y=None):
        """place foreground img on  background img, preserving contours with req labels"""
        shapes = fg_json["shapes"]
        fg_img_mask = np.zeros((fg_img.shape[0], fg_img.shape[1], 3), np.uint8)
        bg_mask = np.zeros((bg_img.shape[0], bg_img.shape[1], 3), np.uint8)
        bg_mask_copy = bg_mask.copy()

        for shape in shapes:
            if shape["label"] in labels:
                contourpts = shape["points"]
                fg_img_mask = draw_polylines(fg_img_mask, contourpts, fill=True, color=[255, 255, 255])

        if target_x is None:
            x_diff = bg_mask.shape[1] - fg_img.shape[1]
            x = random.randint(0, x_diff)
        else:
            x = target_x
        if target_y is None:
            y_diff = bg_mask.shape[0] - fg_img.shape[0]
            y = random.randint(0, y_diff)
        else:
            y = target_y

        bg_mask[y : y + fg_img_mask.shape[0], x : x + fg_img_mask.shape[1]] = fg_img_mask
        bg_mask_copy[y : y + fg_img_mask.shape[0], x : x + fg_img_mask.shape[1]] = fg_img
        bg_mask_inv = cv2.bitwise_not(bg_mask)
        im_ = cv2.bitwise_and(bg_img, bg_mask_inv)
        im1 = cv2.bitwise_and(bg_mask, bg_mask_copy)
        new_bg_image = cv2.add(im1, im_)

        for shape in shapes:  # shift contours in json based on x y and update fg json
            # if shape['label'] in labels:
            contourpts = shape["points"]
            cntr = np.array(contourpts)
            cntr[:, 0] += x
            cntr[:, 1] += y
            contr = cntr.tolist()
            shape["points"] = contr

        return new_bg_image, fg_json


    def check_overlap(self, fg_crop_mask, fg_cntr_label, bg_img, bg_json_dict, target_point):
        """checks overlap between new contour(fg contour) and existing contours in bg_json_dict
        Args:
            fg_crop_mask (img): forground crop mask
            fg_cntr_label (str): labelname of aug contour
            bg_img (img): background image
            bg_json_dict (dict): bg json info
            target_point (int): target point to place fg crop in bg img
        Returns:
            overlap_flag: flag true if overlaps else false
            aug_cntr : new aug contour from fg crop mask
        """
        overlap_flag = False
        img_mask = np.zeros_like(bg_img)
        x, y = target_point
        end_y = y + fg_crop_mask.shape[0] // 2
        start_y = y - fg_crop_mask.shape[0] // 2
        start_x = x - fg_crop_mask.shape[1] // 2
        end_x = x + fg_crop_mask.shape[1] // 2
        if end_x - start_x != fg_crop_mask.shape[1]:
            end_x += 1
        if end_y - start_y != fg_crop_mask.shape[0]:
            end_y += 1
        img_mask[start_y:end_y, start_x:end_x] = fg_crop_mask
        aug_contour = find_cv_contours(img_mask)[0]
        if len(aug_contour) > 2:
            aug_cntr_polygon = Polygon(aug_contour)
            aug_cntr_polygon = aug_cntr_polygon.buffer(0)
            # contours_drw = np.array(aug_contour).reshape((-1,1,2)).astype(np.int32)
            # draw_image = draw_polylines(bg_img.copy(),contours_drw, color=[255, 0, 0], fill=False)
            # image_new = cv2.addWeighted(draw_image, 0.1, bg_img, 1 - 0.3, 0)
            # cv2.imwrite('blend.jpg', draw_image)
            check_dict = deepcopy(bg_json_dict)
            if self.parent_node is None:
                parent_node = self.training_node
            else:
                parent_node = self.parent_node
            for shapes in bg_json_dict["shapes"]:
                cntr = shapes["points"]
                if len(cntr) >= 4:
                    cntr_polygon = Polygon(cntr)
                    cntr_polygon = cntr_polygon.buffer(0)
                    if self.parent_node is not None:
                        if shapes["label"] == parent_node:
                            continue
                    else:
                        if shapes["label"] == parent_node and fg_cntr_label in self.aug_neg_crop_label:
                            continue
                    if cntr_polygon.intersects(aug_cntr_polygon):
                        overlap_flag = True
                        return overlap_flag, aug_contour
        return overlap_flag, aug_contour

    def dump_json_dict(self, img_json_dict, defect_label, aug_cntr):
        """update json dict with new aug contour info added
        Returns:
            img_json_dict: updated json file
        """
        new_dict = {
            "label": defect_label,
            "points": [],
            "shape_type": "polygon",
            "line_thickness": 1,
            "flags": {},
            "color": [0, 255, 0],
            "overlay_mode": "outerline",
            "fill": False,
            "node_name": defect_label,
        }
        if aug_cntr is not None:
            new_dict["points"] = aug_cntr
        img_json_dict["shapes"].append(new_dict)
        return img_json_dict

class TestActiveAugmentation(unittest.TestCase):
    """Test methods"""
    def test_active_augmentation(self):
        """Demo of augmentation"""
        projectname = "Scopito"
        workspace = "Projects/Scopito/workspace"
        fulldb =  "Projects/Scopito/workspace/DB/git_DB_dummy"
        result_path = os.path.join("samples", "test_results", "active_aug_unittest")
        if not check_folder_exists(result_path):
            create_directory_safe(result_path)
        project_config_path = projectname + ".yaml"
        node_name = "A1_scopito_wt"
        model_dir = os.path.join(workspace, "Weights", node_name)
        model_config_path = os.path.join(model_dir, "config.yaml")
        if not check_folder_exists(model_dir):
            CloneRepo("https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/weights", node_name, model_dir)
        project_config_path = os.path.join("Projects", projectname, project_config_path)
        config_fg = NodeConfig(node_name, model_config_path)
        active_aug_obj_fg = ActiveAug(config_fg, workspace, fulldb)
        sample_folder = "samples"
        img_list = glob.glob(sample_folder + "/*.JPG")
        for index, im in enumerate(img_list):
            img = cv2.imread(im)
            json_file = os.path.splitext(os.path.basename(im))[0] + ".json"
            json_dict = read_json(os.path.join(sample_folder, json_file))
            # Fg aug
            result_img, json_dict = active_aug_obj_fg.active_augmentation(img, json_dict, mode="Foreground")
            # bg aug
            result_img, json_dict = active_aug_obj_fg.active_augmentation(result_img, json_dict, mode="Background")
            cv2.imwrite(os.path.join(result_path, f"im_result_{index}.jpg"), result_img)
            json_dict["imagePath"] = f"im_result_{index}.jpg"
            json_name = os.path.join(result_path, f"im_result_{index}.json")
            write_json(json_name, json_dict)
            assert result_img.shape == img.shape

if __name__ == "__main__":
    test_obj = TestActiveAugmentation()
    test_obj.test_active_augmentation()
