"""Filter Utils for workflow"""
import time
import os
import math
import cv2
import numpy as np
from ignutils.labelme_utils import get_label_contours, cleanup_json, create_shape_dict
from ignutils.contour_utils import check_contour_touches,\
get_overlap_area, merge_contours, subtract_contours
from ignutils.filter_utils import get_len_brd_filter_cntrs, get_max_area_cntr

class FIlterJson:
    """Filter labelme json"""
    def __init__(self, node_config):
        self.node_config = node_config
        self.classes = self.node_config("classes")
        self.filters = self.node_config("infer_filters")

    def apply_filter(self, crop_jsons):
        """Apply filters to crop jsons"""
        filtered_crop_jsons = []
        start = time.time()
        for crop_json in crop_jsons: # Loop thru each crops jsons
            for filter_ in self.filters: # Loop thru each filters
                filtername, filter_enabled = self.get_filter_info(filter_)
                fil_obj = FIlterJson(self.node_config)
                if filter_enabled: # call each filter function if its enabled
                    crop_json = getattr(fil_obj,filtername)(crop_json, filter_)
            filtered_crop_jsons.append(crop_json)
        end =time.time()
        print("*************filter time", end-start)
        return filtered_crop_jsons

    def get_class_labels(self, class_dict):
        """Return list of co labels in inp class dict"""
        labels = []
        for index, classname in enumerate(class_dict):
            labels.append(classname)
            labels.extend(class_dict[classname]["co_labels"])
        return labels

    def update_crop_json(self, crop_json, contours, labelname):
        """Update crop json with contrs"""
        shapes = crop_json['shapes']
        for cntr in contours:
            shape_dict = create_shape_dict()
            shape_dict['label'] = labelname
            shape_dict['points'] = cntr
            shapes.append(shape_dict)
        return crop_json

    def get_filter_info(self, filter_):
        """Check filter, if dictionary, get key as filter name"""

        if isinstance(filter_, dict):
            filtername = list(filter_.keys())[0]
            enabled = filter_[filtername]["enabled"]['value']
        else:
            print(filter_)
            raise TypeError("[Error!] filter should be a dictionary, found str!")
        return filtername, enabled

    def get_filter_inp(self, classname, crop_json):
        """Get contour of curr node and cleanup same in crop json"""
        class_co_labels = self.classes[classname]["co_labels"]
        class_co_labels.append(classname)
        curr_cntrs = get_label_contours(crop_json, class_co_labels)
        crop_json = cleanup_json(crop_json, class_co_labels)
        return curr_cntrs, crop_json

    def max_area_filter(self, crop_json, filter_info):
        """Return contour with maximum area"""
        for ind, classname in enumerate(self.classes):
            print(filter_info)
            curr_cntrs, crop_json = self.get_filter_inp(classname, crop_json)
            curr_cntrs = get_max_area_cntr(curr_cntrs)
            crop_json = self.update_crop_json(crop_json, curr_cntrs, classname)
        return crop_json

    def length_breadth_filter(self, crop_json, filter_info):
        """Filter contours based on cntr length breadth threshold"""
        if os.environ.get(f"{self.node_config('node_name')}_length_threshold") is not None:
            length_threshold = float(os.environ.get(f"{self.node_config('node_name')}_length_threshold"))
        else:  # Taking value from config
            length_threshold = filter_info["length_breadth_filter"]["length_threshold"]["value"]
        if os.environ.get(f"{self.node_config('node_name')}_breadth_threshold") is not None:
            breadth_threshold = float(os.environ.get(f"{self.node_config('node_name')}_breadth_threshold"))
        else:
            breadth_threshold = filter_info["length_breadth_filter"]["breadth_threshold"]["value"]
        for ind, classname in enumerate(self.classes):
            curr_cntrs, crop_json = self.get_filter_inp(classname, crop_json)
            parent_wd = crop_json["imageWidth"]
            curr_cntrs = get_len_brd_filter_cntrs(curr_cntrs, length_threshold, breadth_threshold, parent_wd)
            crop_json = self.update_crop_json(crop_json, curr_cntrs, classname)
        return crop_json

    def check_inside_parent(self, crop_json, filter_info):
        """Filter contours based on a parent contour"""
        parent_label = self.node_config("parent_contour")
        parent_contours = get_label_contours(crop_json, [parent_label])
        if not parent_contours:
            return crop_json
        parent_contour = parent_contours[0] # Expecting only one one parent cntr in crop json
        overlap_threshold = filter_info["check_inside_parent"]["overlap_threshold"]["value"]
        for ind, classname in enumerate(self.classes):
            curr_cntrs, crop_json = self.get_filter_inp(classname, crop_json)
            filtered_cntrs = []
            for cntr in curr_cntrs:
                if check_contour_touches(parent_contour, cntr):
                    intersection_area = get_overlap_area(np.array(parent_contour).squeeze(), np.array(cntr).squeeze())
                    curr_area = math.ceil(cv2.contourArea(np.array(cntr)))
                    if intersection_area == curr_area: #if child cntr is completely inside parent cntr append it
                        filtered_cntrs.append(cntr)
                    else:
                        if intersection_area > overlap_threshold:
                            filtered_cntrs.append(cntr)
            crop_json = self.update_crop_json(crop_json, filtered_cntrs, classname)
        return crop_json

    def check_inside_exclude_node(self, crop_json, filter_info):
        """Filter by removing  contours inside exclude node"""
        exclude_nodes = filter_info["check_inside_exclude_node"]["params"]["value"]
        exclude_label_cntrs = get_label_contours(crop_json, exclude_nodes)
        for ind, classname in enumerate(self.classes):
            curr_cntrs, crop_json = self.get_filter_inp(classname, crop_json)
            filtered_cntrs = []
            for exclude_cntr in exclude_label_cntrs:
                for cntr in curr_cntrs:
                    if not get_overlap_area(exclude_cntr, cntr):
                        filtered_cntrs.append(cntr)
            crop_json = self.update_crop_json(crop_json, filtered_cntrs, classname)
        return crop_json

    def get_merged_contours(self, crop_json, filter_info):
        """Loop throgh all contours, and merge if touching"""
        print(filter_info)
        for ind, classname in enumerate(self.classes):
            curr_cntrs, crop_json = self.get_filter_inp(classname, crop_json)
            merged_cntrs = merge_contours(curr_cntrs)
            crop_json = self.update_crop_json(crop_json, merged_cntrs, classname)
        return crop_json

    def subtract_exclude_node(self, crop_json, filter_info):
        """subtract exclude contour from current node and replace curr contour with subtracted contour"""
        exclude_nodes = filter_info["subtract_exclude_node"]["params"]["value"]
        exclude_label_cntrs = get_label_contours(crop_json, exclude_nodes)
        for ind, classname in enumerate(self.classes):
            curr_cntrs, crop_json = self.get_filter_inp(classname, crop_json)
            filtered_cntrs = []
            for exclude_cntr in exclude_label_cntrs:
                for cntr in curr_cntrs:
                    touch_flag = check_contour_touches(cntr, exclude_cntr)
                    if touch_flag:
                        subtracted_cntr = subtract_contours(exclude_cntr, cntr)
                        if len(subtracted_cntr) > 2:
                            filtered_cntrs.append(subtracted_cntr)
            crop_json = self.update_crop_json(crop_json, filtered_cntrs, classname)
        return crop_json
    