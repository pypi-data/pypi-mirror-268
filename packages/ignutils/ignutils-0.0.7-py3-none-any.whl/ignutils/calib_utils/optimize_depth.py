"""Manual and auto optimization class for custom camera pair"""
import argparse
import os
import shutil
import sys

import cv2
import numpy as np
from scipy.optimize import minimize

from ignutils.cam_utils.camera_reader import CameraReader
from ignutils.cam_utils.realsense_reader import RealSenseReader
from ignutils.draw_utils import put_text
from ignutils.json_utils import read_json, write_json
from ignutils.mouse_utils import MousePts
from ignutils.show_utils import show
from ignutils.video_utils.folder_reader import FolderReader
from ignutils.calib_utils.infer_depth import DisparityCalc
from ignutils.calib_utils.rs_crop_dump import RoiAdjust


class MultiOpt:
    """Realsense based multi image optimization"""

    def __init__(self, calib_settings="calibration_settings.json", frame_width=1920, frame_height=1080, calib_id="CALIB_0_0", optim_id="OPTIM_0_0", rs_id="RS_0_0", no_display=False, write_result=False, max_iter=100):
        calib_settings = read_json(calib_settings)
        self.left_id = calib_settings["left_id"]
        self.right_id = calib_settings["right_id"]
        self.img_width = frame_width
        self.img_height = frame_height
        self.no_display = no_display
        self.write_result = write_result
        self.max_iter = max_iter
        self.calib_id = calib_id
        self.optim_id = optim_id
        self.minimize_method = "Nelder-Mead"
        self.internal_roi_list = []
        self.multi_optim_path = os.path.join("data", "multi_optim_data")
        if os.path.isdir(self.multi_optim_path) is False:
            os.makedirs(self.multi_optim_path)
        self.calib_params_path = os.path.join("data", self.calib_id)
        self.optim_params_path = os.path.join("data", self.optim_id)
        if os.path.isdir(self.optim_params_path) is False:
            shutil.copytree(self.calib_params_path, self.optim_params_path)
        self.rs_params_path = os.path.join("data", rs_id)
        self.mouse_obj = MousePts(windowname="Select ROI for optimization")
        self.custom_roi_path = os.path.join(self.optim_params_path, "custom_roi.json")
        self.rs_roi_path = os.path.join(self.rs_params_path, "rs_roi.json")
        if os.path.isfile(self.custom_roi_path) and os.path.isfile(self.rs_roi_path):
            custom_roi = read_json(self.custom_roi_path)
            rs_roi = read_json(self.rs_roi_path)
            self.custom_roi = custom_roi["custom_roi"]
            self.rs_roi = rs_roi["rs_roi"]
        else:
            self.custom_roi = []
            self.rs_roi = []
        self.result_path = os.path.join("data", "results")
        os.makedirs(self.result_path, exist_ok=True)
        self.rs_disp_obj = DisparityCalc(calib_settings="calibration_settings.json", frame_width=1280, frame_height=720, calib_id=self.calib_id, optim_id=self.optim_id, rs_id="RS_0_0", realsense=True)
        self.custom_disp_obj = DisparityCalc(calib_settings="calibration_settings.json", frame_width=self.img_width, frame_height=self.img_height, calib_id=calib_id, optim_id=self.optim_id, rs_id="RS_0_0", realsense=False)

        self.window_name = "params"
        self.track_dict = {
            "fx_l": {"max_val": 5000, "min_val": 0, "range": 2000, "value": 0},
            "fy_l": {"max_val": 5000, "min_val": 0, "range": 2000, "value": 0},
            "cx_l": {"max_val": 5000, "min_val": 0, "range": 2000, "value": 0},
            "cy_l": {"max_val": 5000, "min_val": 0, "range": 2000, "value": 0},
            "fx_r": {"max_val": 5000, "min_val": 0, "range": 2000, "value": 0},
            "fy_r": {"max_val": 5000, "min_val": 0, "range": 2000, "value": 0},
            "cx_r": {"max_val": 5000, "min_val": 0, "range": 2000, "value": 0},
            "cy_r": {"max_val": 5000, "min_val": 0, "range": 2000, "value": 0},
            "num_disparities": {"max_val": 17, "min_val": 1, "range": None, "value": 0},
            "block_size": {"max_val": 50, "min_val": 0, "range": None, "value": 0},
            "min_disparity": {"max_val": 25, "min_val": 0, "range": None, "value": 0},
            "pre_filter_type": {"max_val": 1, "min_val": 0, "range": None, "value": 0},
            "pre_filter_size": {"max_val": 25, "min_val": 0, "range": None, "value": 0},
            "pre_filter_cap": {"max_val": 62, "min_val": 1, "range": None, "value": 0},
            "texture_threshold": {"max_val": 100, "min_val": 0, "range": None, "value": 0},
            "uniqueness_ratio": {"max_val": 100, "min_val": 0, "range": None, "value": 0},
            "speckle_range": {"max_val": 100, "min_val": 0, "range": None, "value": 0},
            "speckle_window_size": {"max_val": 25, "min_val": 0, "range": None, "value": 0},
            "disp12_max_diff": {"max_val": 25, "min_val": 0, "range": None, "value": 0},
            "r_alpha": {"max_val": 0.1, "min_val": None, "range": 1000, "value": 0},
            "r_beta": {"max_val": 0.1, "min_val": None, "range": 1000, "value": 0},
            "r_gamma": {"max_val": 0.1, "min_val": None, "range": 1000, "value": 0},
            "tx": {"max_val": 20, "min_val": None, "range": 1000, "value": 0},
            "ty": {"max_val": 5, "min_val": None, "range": 1000, "value": 0},
            "tz": {"max_val": 5, "min_val": None, "range": 1000, "value": 0},
            "fi_bias": {"max_val": 20, "min_val": None, "range": 1000, "value": 0},
        }
        self.track_vars = list(self.track_dict.keys())

        self.x_dict = {
            "fx_l": False,
            "fy_l": False,
            "cx_l": False,
            "cy_l": False,
            "fx_r": False,
            "fy_r": False,
            "cx_r": False,
            "cy_r": False,
            "r_1": True,
            "r_2": True,
            "r_3": True,
            "t_1": True,
            "t_2": True,
            "t_3": True,
            "d_1": False,
            "d_2": False,
            "d_3": False,
            "d_4": False,
            "d_5": False,
            "d_6": False,
            "d_7": False,
            "d_8": False,
            "d_9": False,
            "d_10": False,
            "d_11": False,
            "fi_bias": True,
        }
        self.x_ind = list(self.x_dict.keys())
        self.custom_left_img_list = []
        self.custom_right_img_list = []
        self.rs_crop_list = []
        self.custom_crop_list = []
        self.rs_depth_list = []
        self.disp_roi_list = []
        self.x_full = []

    def set_default(self):
        """Load default mono and stereo calibration results"""
        left_default = os.path.join(self.calib_params_path, "left_calib.json")
        right_default = os.path.join(self.calib_params_path, "right_calib.json")
        stereo_default = os.path.join(self.calib_params_path, "stereo_result.json")
        disp_default = os.path.join(self.calib_params_path, "disp_params.json")
        if os.path.isfile(left_default) and os.path.isfile(right_default) and os.path.isfile(stereo_default) and os.path.isfile(disp_default):
            print("Setting default values for left calib")
            print("Setting default values for right calib")
            left_calibration_result = read_json(left_default)
            self.custom_disp_obj.mtx_l = np.array(left_calibration_result["mtx"])
            self.custom_disp_obj.dist_l = np.array(left_calibration_result["dist"])
            right_calibration_result = read_json(right_default)
            self.custom_disp_obj.mtx_r = np.array(right_calibration_result["mtx"])
            self.custom_disp_obj.dist_r = np.array(right_calibration_result["dist"])
            print("Setting default values for stereo")
            stereo_calib_result = read_json(stereo_default)
            self.custom_disp_obj.rot = np.array(stereo_calib_result["rot"])
            self.custom_disp_obj.trans = np.array(stereo_calib_result["trans"])
            self.custom_disp_obj.proj_l = np.array(stereo_calib_result["proj_l"])
            self.custom_disp_obj.proj_r = np.array(stereo_calib_result["proj_r"])
            self.custom_disp_obj.rot_angle = np.array(stereo_calib_result["rot_angle"])
            print("Setting default values for disparity")
            disparity_result = read_json(disp_default)
            self.custom_disp_obj.num_disparities = int(disparity_result["num_disparities"])
            self.custom_disp_obj.block_size = int(disparity_result["block_size"])
            self.custom_disp_obj.min_disparity = disparity_result["min_disparity"]
            self.custom_disp_obj.uniqueness_ratio = disparity_result["uniqueness_ratio"]
            self.custom_disp_obj.pre_filter_type = disparity_result["pre_filter_type"]
            self.custom_disp_obj.pre_filter_size = int(disparity_result["pre_filter_size"])
            self.custom_disp_obj.pre_filter_cap = disparity_result["pre_filter_cap"]
            self.custom_disp_obj.speckle_range = disparity_result["speckle_range"]
            self.custom_disp_obj.speckle_window_size = int(disparity_result["speckle_window_size"])
            self.custom_disp_obj.disp12_max_diff = disparity_result["disp12_max_diff"]
            self.custom_disp_obj.texture_threshold = disparity_result["texture_threshold"]
        else:
            raise FileNotFoundError("Default calibration files are missing")

    def save_params(self):
        """Save calibration parameters after tuning"""
        save_path = self.optim_params_path
        left_calib_path = os.path.join(save_path, "left_calib.json")
        right_calib_path = os.path.join(save_path, "right_calib.json")
        stereo_result_path = os.path.join(save_path, "stereo_result.json")
        disp_params_path = os.path.join(save_path, "disp_params.json")
        disp_roi_path = os.path.join(save_path, "disp_roi.json")
        print("Saving calibration parameters...")
        left_calibration_result = {"mtx": self.custom_disp_obj.mtx_l.tolist(), "dist": self.custom_disp_obj.dist_l.tolist()}
        write_json(left_calib_path, left_calibration_result)
        right_calibration_result = {"mtx": self.custom_disp_obj.mtx_r.tolist(), "dist": self.custom_disp_obj.dist_r.tolist()}
        write_json(right_calib_path, right_calibration_result)
        stereo_result = {
            "rot": self.custom_disp_obj.rot.tolist(),
            "rot_angle": self.custom_disp_obj.rot_angle.tolist(),
            "trans": self.custom_disp_obj.trans.tolist(),
            "proj_l": self.custom_disp_obj.proj_l.tolist(),
            "proj_r": self.custom_disp_obj.proj_r.tolist(),
        }
        write_json(stereo_result_path, stereo_result)
        print("Saving disparity parameters...")
        params_json = {}
        params_json["num_disparities"] = self.custom_disp_obj.num_disparities
        params_json["block_size"] = self.custom_disp_obj.block_size
        params_json["min_disparity"] = self.custom_disp_obj.min_disparity
        params_json["pre_filter_cap"] = self.custom_disp_obj.pre_filter_cap
        params_json["pre_filter_type"] = self.custom_disp_obj.pre_filter_type
        params_json["pre_filter_size"] = self.custom_disp_obj.pre_filter_size
        params_json["texture_threshold"] = self.custom_disp_obj.texture_threshold
        params_json["uniqueness_ratio"] = self.custom_disp_obj.uniqueness_ratio
        params_json["speckle_range"] = self.custom_disp_obj.speckle_range
        params_json["speckle_window_size"] = self.custom_disp_obj.speckle_window_size
        params_json["disp12_max_diff"] = self.custom_disp_obj.disp12_max_diff
        params_json["fi_bias"] = self.custom_disp_obj.fi_bias
        write_json(disp_params_path, params_json)
        roi_json = {}
        roi_json["roi"] = self.internal_roi_list
        write_json(disp_roi_path, roi_json)

    def create_trackbar(self):
        """Creating trackbar by given tracker variables"""
        track_window_name = self.window_name
        cv2.namedWindow(track_window_name, cv2.WINDOW_GUI_NORMAL)
        cv2.resizeWindow(track_window_name, 600, 600)
        track_vars_dict = {}

        def nothing(x): # pylint: disable=W0613
            pass

        track_vars_dict["num_disparities"] = int(self.custom_disp_obj.num_disparities / 16)
        track_vars_dict["block_size"] = int((self.custom_disp_obj.block_size - 5) / 2)
        track_vars_dict["min_disparity"] = self.custom_disp_obj.min_disparity
        track_vars_dict["uniqueness_ratio"] = self.custom_disp_obj.uniqueness_ratio
        track_vars_dict["pre_filter_type"] = self.custom_disp_obj.pre_filter_type
        track_vars_dict["pre_filter_size"] = int((self.custom_disp_obj.pre_filter_size - 5) / 2)
        track_vars_dict["pre_filter_cap"] = self.custom_disp_obj.pre_filter_cap
        track_vars_dict["speckle_range"] = self.custom_disp_obj.speckle_range
        track_vars_dict["speckle_window_size"] = int(self.custom_disp_obj.speckle_window_size / 2)
        track_vars_dict["disp12_max_diff"] = self.custom_disp_obj.disp12_max_diff
        track_vars_dict["texture_threshold"] = self.custom_disp_obj.texture_threshold
        track_vars_dict["fi_bias"] = self.custom_disp_obj.fi_bias

        [[track_vars_dict["fx_l"], a, track_vars_dict["cx_l"]], [a, track_vars_dict["fy_l"], track_vars_dict["cy_l"]], [a, a, a]] = self.custom_disp_obj.mtx_l

        [[track_vars_dict["fx_r"], a, track_vars_dict["cx_r"]], [a, track_vars_dict["fy_r"], track_vars_dict["cy_r"]], [a, a, a]] = self.custom_disp_obj.mtx_r

        [track_vars_dict["r_alpha"], track_vars_dict["r_beta"], track_vars_dict["r_gamma"]] = self.custom_disp_obj.rot_angle

        [[track_vars_dict["tx"]], [track_vars_dict["ty"]], [track_vars_dict["tz"]]] = self.custom_disp_obj.trans

        for var_name in self.track_vars:
            var_obj = self.track_dict[var_name]
            value = track_vars_dict.get(var_name)
            max_val = var_obj["max_val"]
            min_val = var_obj["min_val"]
            var_range = var_obj["range"]
            if var_range is not None:
                scale = var_obj["max_val"] / var_range
                value = int(int(var_range) + (value / scale))
                max_val = int(2 * var_range)
            cv2.createTrackbar(var_name, track_window_name, value, max_val, nothing)
            if min_val is not None:
                cv2.setTrackbarMin(var_name, track_window_name, min_val)

    def get_track_bar(self):
        """Get parameter values from trackbar"""
        for _, var_name in enumerate(self.track_vars):
            value = cv2.getTrackbarPos(var_name, self.window_name)
            var_obj = self.track_dict[var_name]
            var_range = var_obj["range"]
            if var_range is not None:
                scale = var_obj["max_val"] / var_obj["range"]
                value = (cv2.getTrackbarPos(var_name, self.window_name) - var_range) * scale
            self.track_dict[var_name]["value"] = value

        disp_values = {}
        disp_values["num_disparities"] = int(self.track_dict["num_disparities"]["value"] * 16)
        disp_values["block_size"] = int(self.track_dict["block_size"]["value"] * 2) + 5
        disp_values["min_disparity"] = self.track_dict["min_disparity"]["value"]
        disp_values["uniqueness_ratio"] = self.track_dict["uniqueness_ratio"]["value"]
        disp_values["pre_filter_type"] = self.track_dict["pre_filter_type"]["value"]
        disp_values["pre_filter_size"] = int(self.track_dict["pre_filter_size"]["value"] * 2) + 5
        disp_values["pre_filter_cap"] = self.track_dict["pre_filter_cap"]["value"]
        disp_values["speckle_range"] = self.track_dict["speckle_range"]["value"]
        disp_values["speckle_window_size"] = int(self.track_dict["speckle_window_size"]["value"] * 2)
        disp_values["disp12_max_diff"] = self.track_dict["disp12_max_diff"]["value"]
        disp_values["texture_threshold"] = self.track_dict["texture_threshold"]["value"]
        disp_values["fi_bias"] = self.track_dict["fi_bias"]["value"]

        mtx_l = np.array(
            [
                [self.track_dict["fx_l"]["value"], 0.0, self.track_dict["cx_l"]["value"]],
                [0.0, self.track_dict["fy_l"]["value"], self.track_dict["cy_l"]["value"]],
                [0.0, 0.0, 1.0],
            ]
        )

        mtx_r = np.array(
            [
                [self.track_dict["fx_r"]["value"], 0.0, self.track_dict["cx_r"]["value"]],
                [0.0, self.track_dict["fy_r"]["value"], self.track_dict["cy_r"]["value"]],
                [0.0, 0.0, 1.0],
            ]
        )

        rot_angle = np.array([self.track_dict["r_alpha"]["value"], self.track_dict["r_beta"]["value"], self.track_dict["r_gamma"]["value"]])

        trans = np.array([[self.track_dict["tx"]["value"]], [self.track_dict["ty"]["value"]], [self.track_dict["tz"]["value"]]])

        return mtx_l, mtx_r, disp_values, rot_angle, trans

    def set_trackbar(self):
        """To set trackbar position"""
        track_window_name = self.window_name
        track_vars_dict = {}
        track_vars_dict["num_disparities"] = int(self.custom_disp_obj.num_disparities / 16)
        track_vars_dict["block_size"] = int((self.custom_disp_obj.block_size - 5) / 2)
        track_vars_dict["min_disparity"] = self.custom_disp_obj.min_disparity
        track_vars_dict["uniqueness_ratio"] = self.custom_disp_obj.uniqueness_ratio
        track_vars_dict["pre_filter_type"] = self.custom_disp_obj.pre_filter_type
        track_vars_dict["pre_filter_size"] = int((self.custom_disp_obj.pre_filter_size - 5) / 2)
        track_vars_dict["pre_filter_cap"] = self.custom_disp_obj.pre_filter_cap
        track_vars_dict["speckle_range"] = self.custom_disp_obj.speckle_range
        track_vars_dict["speckle_window_size"] = int(self.custom_disp_obj.speckle_window_size / 2)
        track_vars_dict["disp12_max_diff"] = self.custom_disp_obj.disp12_max_diff
        track_vars_dict["texture_threshold"] = self.custom_disp_obj.texture_threshold
        track_vars_dict["fi_bias"] = self.custom_disp_obj.fi_bias

        [[track_vars_dict["fx_l"], a, track_vars_dict["cx_l"]], [a, track_vars_dict["fy_l"], track_vars_dict["cy_l"]], [a, a, a]] = self.custom_disp_obj.mtx_l

        [[track_vars_dict["fx_r"], a, track_vars_dict["cx_r"]], [a, track_vars_dict["fy_r"], track_vars_dict["cy_r"]], [a, a, a]] = self.custom_disp_obj.mtx_r

        [track_vars_dict["r_alpha"], track_vars_dict["r_beta"], track_vars_dict["r_gamma"]] = self.custom_disp_obj.rot_angle

        [[track_vars_dict["tx"]], [track_vars_dict["ty"]], [track_vars_dict["tz"]]] = self.custom_disp_obj.trans

        for _, var_name in enumerate(self.track_vars):
            value = track_vars_dict.get(var_name)
            var_obj = self.track_dict[var_name]
            var_range = var_obj["range"]
            if var_range is not None:
                scale = var_obj["max_val"] / var_range
                value = int(int(var_range) + (value / scale))
            cv2.setTrackbarPos(var_name, track_window_name, value)

    def update_from_trackbar(self):
        """Callback function for trackbar to update parameter values"""
        mtx_l, mtx_r, disp_values, rot_angle, trans = self.get_track_bar()

        self.custom_disp_obj.mtx_l[0][0] = mtx_l[0][0]
        self.custom_disp_obj.mtx_l[0][2] = mtx_l[0][2]
        self.custom_disp_obj.mtx_l[1][1] = mtx_l[1][1]
        self.custom_disp_obj.mtx_l[1][2] = mtx_l[1][2]
        self.custom_disp_obj.mtx_r[0][0] = mtx_r[0][0]
        self.custom_disp_obj.mtx_r[0][2] = mtx_r[0][2]
        self.custom_disp_obj.mtx_r[1][1] = mtx_r[1][1]
        self.custom_disp_obj.mtx_r[1][2] = mtx_r[1][2]
        self.custom_disp_obj.num_disparities = disp_values["num_disparities"]
        self.custom_disp_obj.block_size = disp_values["block_size"]
        self.custom_disp_obj.min_disparity = disp_values["min_disparity"]
        self.custom_disp_obj.uniqueness_ratio = disp_values["uniqueness_ratio"]
        self.custom_disp_obj.pre_filter_type = disp_values["pre_filter_type"]
        self.custom_disp_obj.pre_filter_size = disp_values["pre_filter_size"]
        self.custom_disp_obj.pre_filter_cap = disp_values["pre_filter_cap"]
        self.custom_disp_obj.speckle_range = disp_values["speckle_range"]
        self.custom_disp_obj.speckle_window_size = disp_values["speckle_window_size"]
        self.custom_disp_obj.disp12_max_diff = disp_values["disp12_max_diff"]
        self.custom_disp_obj.texture_threshold = disp_values["texture_threshold"]
        self.custom_disp_obj.fi_bias = disp_values["fi_bias"]
        self.custom_disp_obj.rot_angle[0] = rot_angle[0]
        self.custom_disp_obj.rot_angle[1] = rot_angle[1]
        self.custom_disp_obj.rot_angle[2] = rot_angle[2]
        self.custom_disp_obj.trans[0][0] = trans[0][0]
        self.custom_disp_obj.trans[1][0] = trans[1][0]
        self.custom_disp_obj.trans[2][0] = trans[2][0]

    def select_roi(self, disparity):
        """Select ROI on the dispariy image for optimization

        Args:
            disparity (np.ndarray): disparity image
        """
        roi = self.mouse_obj.select_rect(disparity)
        self.internal_roi_list.append(roi)

    def load_optim(self):
        """Load optim files"""
        optim_list = os.listdir(self.multi_optim_path)
        for optim in optim_list:
            custom_optim_path = os.path.join(self.multi_optim_path, optim, "custom")
            rs_optim_path = os.path.join(self.multi_optim_path, optim, "rs")
            rs_depth = np.load(os.path.join(rs_optim_path, "depth.npz"))
            self.rs_depth_list.append(rs_depth["depth"])
            custom_left_img = cv2.imread(os.path.join(custom_optim_path, "orig_left.png"))
            self.custom_left_img_list.append(custom_left_img)
            custom_right_img = cv2.imread(os.path.join(custom_optim_path, "orig_right.png"))
            self.custom_right_img_list.append(custom_right_img)
            custom_crop = read_json(os.path.join(custom_optim_path, "custom_roi.json"))
            self.custom_crop_list.append(custom_crop["custom_roi"])
            rs_crop = read_json(os.path.join(rs_optim_path, "rs_roi.json"))
            self.rs_crop_list.append(rs_crop["rs_roi"])
            disp_roi = read_json(os.path.join(custom_optim_path, "disp_roi.json"))
            self.disp_roi_list.append(disp_roi["roi"])

    def multi_loss_calc(self):
        """Calc loss for multiple images"""
        total_loss = 0

        i = 0
        for custom_left, custom_right, custom_crop, rs_crop, rs_depth, disp_roi in zip(self.custom_left_img_list, self.custom_right_img_list, self.custom_crop_list, self.rs_crop_list, self.rs_depth_list, self.disp_roi_list):
            left_rect, right_rect = self.custom_disp_obj.rectify_image(custom_left, custom_right)
            disparity, disparity_norm = self.custom_disp_obj.get_disparity(left_rect, right_rect)
            depth_map, depth_norm = self.custom_disp_obj.compute_depth_map(disparity)
            x1_, y1_ = custom_crop[0]
            x2_, y2_ = custom_crop[2]
            disparity_norm = disparity_norm[y1_:y2_, x1_:x2_]
            depth_norm = depth_norm[y1_:y2_, x1_:x2_]
            disparity = disparity[y1_:y2_, x1_:x2_]
            depth_map = depth_map[y1_:y2_, x1_:x2_]
            x1, y1 = rs_crop[0]
            x2, y2 = rs_crop[2]
            rs_depth_crop = cv2.resize(rs_depth[y1:y2, x1:x2], (disparity.shape[1], disparity.shape[0]), interpolation=cv2.INTER_AREA)
            self.internal_roi_list = disp_roi
            loss = self.calc_loss(disparity, disparity_norm, depth_map, depth_norm, rs_depth_crop)
            print(f"loss {i}", loss)
            total_loss += loss
            i += 1

        print("TOTAL LOSS :", total_loss)
        return total_loss

    def calc_error(self, rs_crop, custom_crop):
        """Calculate disp/depth error between realsense and custom

        Args:
            rs_crop (np.ndarray): realsense input crop
            custom_crop (np.ndarray): custom input crop
            text (str): print statement

        Returns:
            mean error: loss between rs and custom
        """
        img_diff = rs_crop - custom_crop
        print("actual diff", np.average(img_diff))
        diff_abs = np.absolute(img_diff)
        # For imshow with factor multiplied
        diff_fac = (diff_abs * 6).astype("uint8")
        # Masking the diff to avoid error values (> 500)
        _, err_mask = cv2.threshold(diff_abs, 500, 255, cv2.THRESH_TOZERO)
        diff_mask = diff_abs - err_mask
        mean_error = np.sum(diff_mask) / (rs_crop.shape[0] * rs_crop.shape[1])

        return mean_error, diff_fac, err_mask

    def calc_black_pixel_perc(self, disparity):
        """Calculate black pixel percentage in disparity image"""
        _, mask = cv2.threshold(disparity, 20, 255, cv2.THRESH_BINARY)
        crop_size = disparity.shape[0] * disparity.shape[1]
        black_count = crop_size - cv2.countNonZero(mask)
        black_perc = black_count / crop_size

        return black_perc, mask

    def calc_loss(self, disparity, disparity_norm, depth, depth_norm, rs_depth_crop=None):
        """Calculate loss for the minization func

        Args:
            disparity (np.ndarray): disparty image

        Returns:
            float: total loss
        """
        k = -1
        perc_loss = 0
        mean_loss = 0
        mean_loss_weighted = 0
        perc_loss_weighted = 0
        tex = "Depth loss: "

        full_crop_roi = [[0, 0], [disparity.shape[1], 0], [disparity.shape[1], disparity.shape[0]], [0, disparity.shape[0]]]
        if full_crop_roi not in self.internal_roi_list:
            self.internal_roi_list.insert(0, full_crop_roi)
        perc_wt_list = [0.5] + ([1] * (len(self.internal_roi_list) - 1))
        depth_wt_list = [0.05] + ([0.1] * (len(self.internal_roi_list) - 1))

        # Looping through roi list to calculate loss
        disparity_show = disparity_norm.copy()
        for i, roi in enumerate(self.internal_roi_list):
            x1, y1 = roi[0]
            x2, y2 = roi[2]
            disp_crop = disparity[y1:y2, x1:x2]
            black_perc, mask = self.calc_black_pixel_perc(disp_crop)
            perc_loss += black_perc
            perc_loss_weighted = perc_loss * perc_wt_list[i]
            cv2.rectangle(disparity_show, (x1, y1), (x2, y2), [0, 0, 0], 2)
            if self.no_display is False:
                k = show(mask, win=f"black pixel mask {i}", time=30, k=k, window_normal=True)
                k = show(disparity, win=f"actual disp {i}", time=30, k=k, window_normal=True, clip=True)

            # If realsense crop available, calc depth/disparity loss
            if rs_depth_crop is not None:
                # Using disparity instead of disparity norm for depth
                rs_crop = rs_depth_crop[y1:y2, x1:x2]
                custom_crop = depth[y1:y2, x1:x2]
                mean_error, diff_fac, err_mask = self.calc_error(rs_crop, custom_crop)
                mean_loss += mean_error
                mean_loss_weighted = mean_loss * depth_wt_list[i]
                cv2.putText(img=disparity_show, text=tex + str(round(mean_error, 3)), org=(int(x1), int(y1) + 50), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=[0, 0, 0], thickness=3, lineType=cv2.LINE_AA)

                if self.no_display is False:
                    k = show(diff_fac, win=f"crop difference {i}", time=30, k=k, window_normal=True)
                    k = show(err_mask, win=f"err mask {i}", time=30, k=k, window_normal=True)

        print("mean loss: ", mean_loss)
        print("black perc loss: ", perc_loss)
        print("mean loss weighted: ", mean_loss_weighted)
        print("black perc loss weighted: ", perc_loss_weighted)

        if self.no_display is False:
            k = show(disparity_show, win="optimization", time=30, k=k, window_normal=True)

        if k == ord("p"):
            print("Press 's' to save, 'Enter' to continue")
            k = cv2.waitKey(0)

        if k == ord("s"):
            self.save_params()

        if k == ord("d"):
            self.set_default()

        if k == 27:
            sys.exit()

        if self.write_result:
            cv2.imwrite(os.path.join(self.result_path, "depth.png"), depth_norm)

        final_loss = perc_loss + mean_loss
        print("Sum loss: ", final_loss)

        return final_loss

    def minimize_func(self, x):
        """Minimization func for optimization

        Args:
            X (list): List of values to optimize

        Returns:
            float: loss value
        """
        index = 0
        for key, value in self.x_dict.items():
            if value is True:
                self.x_full[self.x_ind.index(key)] = x[index]
                index += 1

        [fx_l, fy_l, cx_l, cy_l, fx_r, fy_r, cx_r, cy_r, r_1, r_2, r_3, t_1, t_2, t_3, d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10, d_11, fi_bias] = self.x_full # pylint: disable=W0632

        self.custom_disp_obj.mtx_l = np.array(
            [
                [fx_l, 0.0, cx_l],
                [0.0, fy_l, cy_l],
                [0.0, 0.0, 1.0],
            ]
        )
        self.custom_disp_obj.mtx_r = np.array(
            [
                [fx_r, 0.0, cx_r],
                [0.0, fy_r, cy_r],
                [0.0, 0.0, 1.0],
            ]
        )
        self.custom_disp_obj.rot_angle = np.array([r_1, r_2, r_3])
        self.custom_disp_obj.trans = np.array([[t_1], [t_2], [t_3]])
        if int(d_1) % 16 == 0:
            self.custom_disp_obj.num_disparities = int(d_1)
        if int(d_2) % 2 != 0:
            self.custom_disp_obj.block_size = int(d_2)
        self.custom_disp_obj.min_disparity = int(d_3)
        self.custom_disp_obj.uniqueness_ratio = int(d_4)
        self.custom_disp_obj.pre_filter_type = int(d_5)
        if int(d_6) % 2 != 0:
            self.custom_disp_obj.pre_filter_size = int(d_6)
        self.custom_disp_obj.pre_filter_cap = int(d_7)
        self.custom_disp_obj.speckle_range = int(d_8)
        if int(d_9) % 2 != 0:
            self.custom_disp_obj.speckle_window_size = int(d_9)
        self.custom_disp_obj.disp12_max_diff = int(d_10)
        self.custom_disp_obj.texture_threshold = int(d_11)
        self.custom_disp_obj.fi_bias = fi_bias

        if self.no_display is False:
            self.set_trackbar()
        loss = self.multi_loss_calc()
        return loss

    def optimise_params(self):
        """Optmization function for disparity"""
        [[fx_l, a, cx_l], [a, fy_l, cy_l], [a, a, a]] = self.custom_disp_obj.mtx_l
        [[fx_r, a, cx_r], [a, fy_r, cy_r], [a, a, a]] = self.custom_disp_obj.mtx_r

        [r_1, r_2, r_3] = self.custom_disp_obj.rot_angle
        [[t_1], [t_2], [t_3]] = self.custom_disp_obj.trans
        d_1 = self.custom_disp_obj.num_disparities
        d_2 = self.custom_disp_obj.block_size
        d_3 = self.custom_disp_obj.min_disparity
        d_4 = self.custom_disp_obj.uniqueness_ratio
        d_5 = self.custom_disp_obj.pre_filter_type
        d_6 = self.custom_disp_obj.pre_filter_size
        d_7 = self.custom_disp_obj.pre_filter_cap
        d_8 = self.custom_disp_obj.speckle_range
        d_9 = self.custom_disp_obj.speckle_window_size
        d_10 = self.custom_disp_obj.disp12_max_diff
        d_11 = self.custom_disp_obj.texture_threshold
        fi_bias = self.custom_disp_obj.fi_bias

        self.x_full = [fx_l, fy_l, cx_l, cy_l, fx_r, fy_r, cx_r, cy_r, r_1, r_2, r_3, t_1, t_2, t_3, d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10, d_11, fi_bias]
        bounds_full = [
            (1200, 1400),
            (1200, 1400),
            (900, 1000),
            (500, 600),
            (1200, 1400),
            (1200, 1400),
            (900, 1000),
            (500, 600),
            (-0.1, 0.1),
            (-0.1, 0.1),
            (-0.1, 0.1),
            (-20, 20),
            (-5, 5),
            (-5, 5),
            (16, 272),
            (7, 105),
            (0, 25),
            (0, 100),
            (0, 1),
            (7, 55),
            (1, 62),
            (1, 100),
            (2, 50),
            (1, 25),
            (1, 100),
            (-20, 20),
        ]

        x = []
        bounds = []
        for key, value in self.x_dict.items():
            if value is True:
                x.append(self.x_full[self.x_ind.index(key)])
                bounds.append(bounds_full[self.x_ind.index(key)])
        bounds = tuple(bounds)

        # upper and lower limits for variables
        result = minimize(
            self.minimize_func,
            x,
            method=self.minimize_method,
            bounds=bounds,
            options={
                "adaptive": True,
                "maxiter": self.max_iter,
                "maxfev": None,
                "xatol": 0.01,
                "fatol": 0.1,
            },
        )

    def depth_value(self, event, x, y, flags, param): # pylint: disable=W0613
        """mouse event to get depth value"""
        if event == cv2.EVENT_MOUSEMOVE:
            param["x1"] = x
            param["y1"] = y

    def optimize(self, custom_left_folder_path=None, custom_right_folder_path=None, rs_left_folder_path=None, rs_right_folder_path=None): # pylint: disable=R0914, R0915
        """Save disparity, depth for optimization"""
        if custom_left_folder_path is not None and custom_right_folder_path is not None and rs_left_folder_path is not None and rs_right_folder_path is not None:
            custom_img_obj_l = FolderReader(folder_path=custom_left_folder_path)
            custom_img_obj_r = FolderReader(folder_path=custom_right_folder_path)
            rs_img_obj_l = FolderReader(folder_path=rs_left_folder_path)
            rs_img_obj_r = FolderReader(folder_path=rs_right_folder_path)
            custom_x1 = int(custom_img_obj_l.frame_width / 2)
            custom_y1 = int(custom_img_obj_r.frame_height / 2)
            rs_x1 = int(custom_img_obj_l.frame_width / 2)
            rs_y1 = int(custom_img_obj_r.frame_height / 2)
            custom_left_img, _, _ = custom_img_obj_l.next_frame()
            custom_right_img, _, _ = custom_img_obj_r.next_frame()
            rs_left_img, _, _ = rs_img_obj_l.next_frame()
            rs_right_img, _, _ = rs_img_obj_r.next_frame()
        else:
            # Reading from realsense
            rs_cam_obj = RealSenseReader()
            rs_x1 = int(rs_cam_obj.cam_width / 2)
            rs_y1 = int(rs_cam_obj.cam_height / 2)

            # Reading from custom set
            custom_cam_obj_l = CameraReader(cam_index=self.left_id, ui_flag=False, setting_path="data/left_setting.json")
            custom_cam_obj_r = CameraReader(cam_index=self.right_id, ui_flag=False, setting_path="data/right_setting.json")
            cap_l = custom_cam_obj_l.get_cap()
            cap_r = custom_cam_obj_r.get_cap()
            cam_width = custom_cam_obj_l.cam_width
            cam_height = custom_cam_obj_r.cam_height
            custom_x1 = 0
            custom_y1 = 0
            if cam_width is not None and cam_height is not None:
                custom_x1 = int(cam_width / 2)
                custom_y1 = int(cam_height / 2)

        cv2.namedWindow("rs disparity", cv2.WINDOW_GUI_NORMAL)
        cv2.namedWindow("rs depth", cv2.WINDOW_GUI_NORMAL)
        cv2.namedWindow("rs left rectified", cv2.WINDOW_GUI_NORMAL)
        cv2.namedWindow("custom disparity", cv2.WINDOW_GUI_NORMAL)
        cv2.namedWindow("custom depth", cv2.WINDOW_GUI_NORMAL)
        cv2.namedWindow("custom left rectified", cv2.WINDOW_GUI_NORMAL)
        custom_param = {"x1": custom_x1, "y1": custom_y1}
        cv2.setMouseCallback("custom depth", self.depth_value, custom_param)
        rs_param = {"x1": rs_x1, "y1": rs_y1}
        cv2.setMouseCallback("rs depth", self.depth_value, rs_param)
        self.create_trackbar()

        avl_optim = os.listdir(self.multi_optim_path)
        if len(avl_optim) == 0:
            folder_ind = 0
        else:
            folder_ind = int(sorted(avl_optim)[-1].split("_")[-1])

        rs_cam_obj, cap_l, cap_r, custom_left_img, custom_right_img, rs_left_img, rs_right_img = None, None, None, None, None, None, None
        while True:
            if custom_left_folder_path is None and custom_right_folder_path is None and rs_left_folder_path is None and rs_right_folder_path is None:
                if rs_cam_obj is not None and cap_l is not None and cap_r is not None:
                    _, rs_left_img, rs_right_img = rs_cam_obj.get_left_right()
                    _, custom_left_img = cap_l.read()
                    _, custom_right_img = cap_r.read()

            # Getting disparity and depth images from RS and custom
            self.update_from_trackbar()
            custom_left_rect, custom_right_rect = self.custom_disp_obj.rectify_image(custom_left_img, custom_right_img)
            custom_disparity, custom_disparity_norm = self.custom_disp_obj.get_disparity(custom_left_rect, custom_right_rect)
            custom_depth, custom_depth_norm = self.custom_disp_obj.compute_depth_map(custom_disparity)

            rs_left_rect, rs_right_rect = self.rs_disp_obj.rectify_image(rs_left_img, rs_right_img)
            rs_disparity, rs_disparity_norm = self.rs_disp_obj.get_disparity(rs_left_rect, rs_right_rect)
            rs_depth, rs_depth_norm = self.rs_disp_obj.compute_depth_map(rs_disparity)

            custom_x1 = custom_param["x1"]
            custom_y1 = custom_param["y1"]
            depth = custom_depth[custom_y1, custom_x1]
            cv2.circle(custom_depth_norm, (custom_x1, custom_y1), 5, (255, 255, 255), -3)
            put_text(f"Depth: {depth}", custom_depth_norm, (20), (50), color=(255, 255, 255), thickness=3, font=cv2.QT_FONT_NORMAL, draw_bg=False)

            rs_x1 = rs_param["x1"]
            rs_y1 = rs_param["y1"]
            depth = rs_depth[rs_y1, rs_x1]
            cv2.circle(rs_depth_norm, (rs_x1, rs_y1), 5, (255, 255, 255), -3)
            put_text(f"Depth: {depth}", rs_depth_norm, (20), (50), color=(255, 255, 255), thickness=3, font=cv2.QT_FONT_NORMAL, draw_bg=False)

            cv2.imshow("rs disparity", rs_disparity_norm)
            cv2.imshow("rs depth", rs_depth_norm)
            cv2.imshow("rs left rectified", rs_left_rect)
            cv2.imshow("custom disparity", custom_disparity_norm)
            cv2.imshow("custom depth", custom_depth_norm)
            cv2.imshow("custom left rectified", custom_left_rect)

            k = cv2.waitKey(10)

            if k == ord("l"):
                self.calc_loss(custom_disparity, custom_disparity_norm, custom_depth, custom_depth_norm)

            if k == ord("r"):
                roi_obj = RoiAdjust(custom_left_rect, custom_disparity_norm, custom_depth_norm, rs_left_rect, rs_disparity_norm, rs_depth_norm, rs_disparity, rs_depth, optim_id=self.optim_id, rs_id="RS_0_0")
                self.rs_roi, self.custom_roi = roi_obj.adjust_roi()

            if k == ord("i"):
                if self.custom_roi is not None:
                    x1, y1 = self.custom_roi[0]
                    x2, y2 = self.custom_roi[2]
                    custom_disparity_norm = custom_disparity_norm[y1:y2, x1:x2]
                self.select_roi(custom_disparity_norm)
                print("Selected ROI: ", self.internal_roi_list)
                self.save_params()

            if k == ord("s"):
                folder_path = os.path.join(self.multi_optim_path, f"optim_{str(folder_ind).zfill(3)}")
                custom_path = os.path.join(folder_path, "custom")
                rs_path = os.path.join(folder_path, "rs")
                if os.path.isdir(custom_path) is False and os.path.isdir(rs_path) is False:
                    os.makedirs(custom_path)
                    os.makedirs(rs_path)
                np.savez(os.path.join(rs_path, "disparity.npz"), disp=rs_disparity)
                np.savez(os.path.join(rs_path, "depth.npz"), depth=rs_depth)
                cv2.imwrite(os.path.join(rs_path, "disparity.png"), rs_disparity_norm * 255)
                cv2.imwrite(os.path.join(rs_path, "depth.png"), rs_depth_norm)
                np.savez(os.path.join(custom_path, "disparity.npz"), disp=custom_disparity)
                np.savez(os.path.join(custom_path, "depth.npz"), depth=custom_depth)
                if rs_left_img is not None and rs_right_img is not None and custom_left_img is not None and custom_right_img is not None:
                    cv2.imwrite(os.path.join(rs_path, "orig_left.png"), rs_left_img)
                    cv2.imwrite(os.path.join(rs_path, "orig_right.png"), rs_right_img)
                    cv2.imwrite(os.path.join(custom_path, "orig_left.png"), custom_left_img)
                    cv2.imwrite(os.path.join(custom_path, "orig_right.png"), custom_right_img)
                cv2.imwrite(os.path.join(custom_path, "disparity.png"), custom_disparity_norm * 255)
                cv2.imwrite(os.path.join(custom_path, "depth.png"), custom_depth_norm)
                roi_json = {"roi": self.internal_roi_list}
                write_json(os.path.join(custom_path, "disp_roi.json"), roi_json)
                custom_roi = {"custom_roi": self.custom_roi}
                write_json(os.path.join(custom_path, "custom_roi.json"), custom_roi)
                rs_roi = {"rs_roi": self.rs_roi}
                write_json(os.path.join(rs_path, "rs_roi.json"), rs_roi)
                self.save_params()
                folder_ind += 1

            if k == ord("o"):
                self.load_optim()
                self.optimise_params()
                self.save_params()

            if k == 27:
                break

        cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-cs", "--calib_settings", default="calibration_settings.json", help="path for calibration settings json")
    parser.add_argument("-nd", "--no_display", default=False, nargs="?", const=True, help="Dont show calibration image output")
    parser.add_argument("-cli", "--custom_left_images", default=None, help="left input images")
    parser.add_argument("-cri", "--custom_right_images", default=None, help="right input images")
    parser.add_argument("-rli", "--rs_left_images", default=None, help="left input images")
    parser.add_argument("-rri", "--rs_right_images", default=None, help="right input images")
    parser.add_argument("-o", "--optimize", default=False, nargs="?", const=True, help="To enable auto optimization")
    parser.add_argument("-wr", "--write_results", default=False, nargs="?", const=True, help="To write the output result")
    parser.add_argument("-mi", "--max_iters", default=200, type=int, help="No of iterations for optimization")
    parser.add_argument("-fw", "--frame_width", default=1920, type=int, help="Frame width")
    parser.add_argument("-fh", "--frame_height", default=1080, type=int, help="Frame height")
    parser.add_argument("-cid", "--calib_id", default="CALIB_0_0", help="camera calibration id for calibration params")
    parser.add_argument("-oid", "--optim_id", default="OPTIM_0_0", help="camera optimization id for optimized params")
    parser.add_argument("-rid", "--rs_id", default="RS_0_0", help="Realsense camera id for calibrated params")

    parser = parser.parse_args()
    calib_settings_ = parser.calib_settings
    no_display_ = parser.no_display
    custom_left_images_ = parser.custom_left_images
    custom_right_images_ = parser.custom_right_images
    rs_left_images_ = parser.rs_left_images
    rs_right_images_ = parser.rs_right_images
    optimize_ = parser.optimize
    write_result_ = parser.write_results
    max_iters_ = parser.max_iters
    frame_width_ = parser.frame_width
    frame_height_ = parser.frame_height
    calib_id_ = parser.calib_id
    optim_id_ = parser.optim_id
    rs_id_ = parser.rs_id

    multi_opt_obj = MultiOpt(calib_settings_, frame_width_, frame_height_, calib_id_, optim_id_, rs_id_, no_display_, write_result_, max_iters_)
    if optimize_:
        multi_opt_obj.load_optim()
        multi_opt_obj.optimise_params()
    else:
        multi_opt_obj.optimize(custom_left_images_, custom_right_images_, rs_left_images_, rs_right_images_)
