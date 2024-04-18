# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : stereo_error_calc.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""To get live error calculation for stereo setup based on checkerboard"""
import argparse
import os
import cv2
import numpy as np

from ignutils.cam_utils.camera_reader import CameraReader
from ignutils.cam_utils.realsense_reader import RealSenseReader
from ignutils.json_utils import read_json
from ignutils.video_utils.folder_reader import FolderReader


class Stereo3dErrorCalc:
    """Stereo calibration error calculation"""

    def __init__(self, calib_settings="calibration_settings.json", calib_id="CALIB_0_0"):
        calib_settings = read_json(calib_settings)
        self.rows = calib_settings["rows"]
        self.cols = calib_settings["cols"]
        optim_params_path = os.path.join("data", calib_id)
        self.stereo_result_path = os.path.join(optim_params_path, "stereo_result.json")
        self.left_calib_path = os.path.join(optim_params_path, "left_calib.json")
        self.right_calib_path = os.path.join(optim_params_path, "right_calib.json")
        self.square_size = calib_settings["square_size"]
        self.left_id = calib_settings["left_id"]
        self.right_id = calib_settings["right_id"]
        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        objp = np.zeros((self.rows * self.cols, 3), np.float32)
        objp[:, :2] = np.mgrid[0 : self.rows, 0 : self.cols].T.reshape(-1, 2)
        size_of_chessboard_squares_mm = self.square_size
        self.objp = objp * size_of_chessboard_squares_mm
        self.load_params()

    def load_params(self):
        """Function for loading camera parameters

        Raises:
            Exception: If file is missing
        """
        if os.path.isfile(self.left_calib_path) and os.path.isfile(self.right_calib_path):
            print(f"Reading left calib json {self.left_calib_path}")
            print(f"Reading right calib json {self.right_calib_path}")
            left_calibration_result = read_json(self.left_calib_path)
            self.mtx_l = np.array(left_calibration_result["mtx"])
            self.dist_l = np.array(left_calibration_result["dist"])
            right_calibration_result = read_json(self.right_calib_path)
            self.mtx_r = np.array(right_calibration_result["mtx"])
            self.dist_r = np.array(right_calibration_result["dist"])
        else:
            raise FileNotFoundError("Mono calibration results not found, please calibrate and try again")

        if os.path.isfile(self.stereo_result_path):
            print("Reading stereo calibration results")
            stereo_calib_result = read_json(self.stereo_result_path)
            self.rot = np.array(stereo_calib_result["rot"])
            self.trans = np.array(stereo_calib_result["trans"])
        else:
            raise FileNotFoundError("Stereo calibration results not found, please calibrate and try again")

    def get_objp_imgp(self, left_image, right_image):
        """Generate object and image points for pair of left and right images

        Args:
            left_image (np.ndarray): Input left image
            right_image (np.ndarray): Input right image

        Returns:
            np.ndarray: object and image points of left and right images
        """
        gray_l = left_image if left_image.ndim == 2 else cv2.cvtColor(left_image, cv2.COLOR_BGR2GRAY)
        gray_r = right_image if right_image.ndim == 2 else cv2.cvtColor(right_image, cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret_l, corners_l = cv2.findChessboardCorners(gray_l, (self.rows, self.cols), None)
        ret_r, corners_r = cv2.findChessboardCorners(gray_r, (self.rows, self.cols), None)

        # If found, add object points, image points (after refining them)
        if ret_l is True and ret_r is True:
            corners_l = cv2.cornerSubPix(gray_l, corners_l, (11, 11), (-1, -1), self.criteria)
            corners_r = cv2.cornerSubPix(gray_r, corners_r, (11, 11), (-1, -1), self.criteria)
            objpoints = self.objp
            imgpoints_l = corners_l
            imgpoints_r = corners_r
        else:
            objpoints = None
            imgpoints_l = None
            imgpoints_r = None
            print("Checker board not detected")

        return objpoints, imgpoints_l, imgpoints_r

    def calc_cam_pos(self, corners, obj_points):
        """Calculate the xyz position of camera wrt to checker board

        Args:
            corners (np.array): Corner points of checker/charuco
            obj_points (np.array): Object points or ids of corners

        Returns:
            np.array: XYZ camera position wrt to board
        """
        _, rvec, tvec = cv2.solvePnP(obj_points, corners, self.mtx_l, self.dist_l, flags=cv2.SOLVEPNP_EPNP)
        rot_m, _ = cv2.Rodrigues(rvec)

        return rot_m, tvec

    def calc_proj_point(self, objp, imgp_l):
        """Calculate project points of checkerboard origin for left and right images

        Args:
            objp (np.ndarray): object points of checkerboard
            imgp_l (np.ndarray): Image points of checkerboard

        Returns:
            np.ndarray: pixel position of checkerboard origin of left and right checkerboard images
        """
        rot_m, tvec = self.calc_cam_pos(imgp_l, objp)
        unitv_points = 5 * np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype="float32").reshape((4, 1, 3))

        # project origin points to frame 0
        points, _ = cv2.projectPoints(unitv_points, rot_m, tvec, self.mtx_l, self.dist_l)
        pixel_points_left = points.reshape((4, 2)).astype(np.int32)

        # project origin points to frame1
        r_w1 = self.rot @ rot_m
        t_w1 = self.rot @ tvec + self.trans

        points, _ = cv2.projectPoints(unitv_points, r_w1, t_w1, self.mtx_r, self.dist_r)
        pixel_points_right = points.reshape((4, 2)).astype(np.int32)

        return pixel_points_left, pixel_points_right


def error_calc_demo(calib_settings, calib_id="CALIB_0_0", left_folder_path=None, right_folder_path=None, realsense=False):
    """Demo for calculating error on a live feed/video

    Args:
        cam_id (int): Camera index
    """
    err_calc_obj = Stereo3dErrorCalc(calib_settings, calib_id)
    cam_obj, img_r, img_l, cap_l, cap_r, img_obj_l, img_obj_r = None, None, None, None, None, None, None
    if left_folder_path is None and right_folder_path is None:
        if realsense:
            cam_obj = RealSenseReader()
        else:
            cam_obj_l = CameraReader(cam_index=err_calc_obj.left_id, ui_flag=True, setting_path="data/left_setting.json")
            cam_obj_r = CameraReader(cam_index=err_calc_obj.right_id, ui_flag=True, setting_path="data/right_setting.json")
            cap_l = cam_obj_l.get_cap()
            cap_r = cam_obj_r.get_cap()
    else:
        if left_folder_path is not None and right_folder_path is not None:
            img_obj_l = FolderReader(folder_path=left_folder_path)
            img_obj_r = FolderReader(folder_path=right_folder_path)

    while True:
        if left_folder_path is None and right_folder_path is None:
            if realsense and cam_obj is not None:
                _, img_l, img_r = cam_obj.get_left_right()
            else:
                if cap_l is not None and cap_r is not None:
                    _, img_l = cap_l.read()
                    _, img_r = cap_r.read()
        else:
            if img_obj_l is not None and img_obj_r is not None:
                img_l, _, _ = img_obj_l.next_frame()
                img_r, _, _ = img_obj_r.next_frame()

        if img_l is None or img_r is None or isinstance(img_l, str) or isinstance(img_r, str):
            break

        objp, imgp_l, imgp_r = err_calc_obj.get_objp_imgp(img_l, img_r)
        err_calc_obj.load_params()
        if objp is not None and imgp_l is not None and imgp_r is not None:
            pp_l, pp_r = err_calc_obj.calc_proj_point(objp, imgp_l)
        else:
            pp_l = None
            pp_r = None

        if pp_l is not None and pp_r is not None:
            # follow RGB colors to indicate XYZ axes respectively
            colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]
            # draw projections to camera0
            origin = tuple(pp_l[0].astype(np.int32))
            for col, _p in zip(colors, pp_l[1:]):
                _p = tuple(_p.astype(np.int32))
                cv2.line(img_l, origin, _p, col, 2)

            # draw projections to camera1
            origin = tuple(pp_r[0].astype(np.int32))
            for col, _p in zip(colors, pp_r[1:]):
                _p = tuple(_p.astype(np.int32))
                cv2.line(img_r, origin, _p, col, 2)

            cv2.namedWindow("Left error calc", cv2.WINDOW_GUI_NORMAL)
            cv2.imshow("Left error calc", img_l)
            cv2.namedWindow("Right error calc", cv2.WINDOW_GUI_NORMAL)
            cv2.imshow("Right error calc", img_r)
            k = cv2.waitKey(0)
            if k == 27:
                cv2.destroyAllWindows()
                break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-cs", "--calib_settings", default="calibration_settings.json", help="path for calibration settings json")
    parser.add_argument("-li", "--left_images", default=None, help="left input images")
    parser.add_argument("-ri", "--right_images", default=None, help="right input images")
    parser.add_argument("-rs", "--realsense", default=False, nargs="?", const=True, help="To record from realsense camera")
    parser.add_argument("-cid", "--calib_id", default="CALIB_0_0", help="camera calibration id for calibration params")

    parser = parser.parse_args()
    calib_settings_ = parser.calib_settings
    left_images_ = parser.left_images
    right_images_ = parser.right_images
    realsense_ = parser.realsense
    calib_id_ = parser.calib_id

    error_calc_demo(calib_settings_, calib_id_, left_images_, right_images_, realsense_)
