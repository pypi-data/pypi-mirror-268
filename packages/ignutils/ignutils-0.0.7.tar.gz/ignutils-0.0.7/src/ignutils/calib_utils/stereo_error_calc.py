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
"""To get live error calculation for stereo setup"""
import unittest
import argparse
import os
import cv2
import numpy as np

from ignutils.cam_utils.camera_reader import CameraReader
from ignutils.cam_utils.realsense_reader import RealSenseReader
from ignutils.json_utils import read_json
from ignutils.video_utils.folder_reader import FolderReader


class StereoErrorCalc:
    """Stereo calibration error calculation"""

    def __init__(self, calib_settings="calibration_settings.json", calib_id="CALIB_0_0"):
        calib_settings = read_json(calib_settings)
        self.rows = calib_settings["rows"]
        self.cols = calib_settings["cols"]
        calib_params_path = os.path.join("data", calib_id)
        self.stereo_result_path = os.path.join(calib_params_path, "stereo_result.json")
        self.left_calib_path = os.path.join(calib_params_path, "left_calib.json")
        self.right_calib_path = os.path.join(calib_params_path, "right_calib.json")
        self.square_size = calib_settings["square_size"]
        self.left_id = calib_settings["left_id"]
        self.right_id = calib_settings["right_id"]

        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
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

    def calc_rms_stereo(self, objectpoints, imgpoints_l, imgpoints_r):
        """Re-projection error calc for mono calibration

        Args:
            objectpoints (np.ndarray): object points
            imgpoints_l (np.ndarray): left image points
            imgpoints_r (np.ndarray): right image points

        Returns:
            float: total error
            np.ndarray: left and right image points
        """
        # calculate world <-> cam1 transformation
        _, rvec_l, tvec_l, _ = cv2.solvePnPRansac(objectpoints, imgpoints_l, self.mtx_l, self.dist_l)

        # compute reprojection error for cam1
        rp_l, _ = cv2.projectPoints(objectpoints, rvec_l, tvec_l, self.mtx_l, self.dist_l)
        tot_error = cv2.norm(imgpoints_l, rp_l, cv2.NORM_L2) / len(rp_l)

        # calculate world <-> cam2 transformation
        rvec_r, tvec_r = cv2.composeRT(rvec_l, tvec_l, cv2.Rodrigues(self.rot)[0], self.trans)[:2]

        # compute reprojection error for cam2
        rp_r, _ = cv2.projectPoints(objectpoints, rvec_r, tvec_r, self.mtx_r, self.dist_r)
        tot_error += cv2.norm(imgpoints_r, rp_r, cv2.NORM_L2) / len(rp_r)

        print("Stereo reprojection Error: ", tot_error)
        return tot_error, rp_l, rp_r

def error_calc_demo(calib_settings, calib_id="CALIB_0_0", realsense=False):
    """Demo for calculating error on a live feed/video

    Args:
        cam_id (int): Camera index
    """
    stereo_err_calc_obj = StereoErrorCalc(calib_settings, calib_id)
    cam_obj = None
    cap_l = None
    cap_r = None
    img_l = None
    img_r = None

    if realsense:
        cam_obj = RealSenseReader()
    else:
        cam_obj_l = CameraReader(cam_index=stereo_err_calc_obj.left_id, ui_flag=True, setting_path="data/left_setting.json")
        cam_obj_r = CameraReader(cam_index=stereo_err_calc_obj.right_id, ui_flag=True, setting_path="data/right_setting.json")
        cap_l = cam_obj_l.get_cap()
        cap_r = cam_obj_r.get_cap()

    while True:
        if realsense and cam_obj is not None:
            _, img_l, img_r = cam_obj.get_left_right()
        else:
            if cap_l is not None and cap_r is not None:
                _, img_l = cap_l.read()
                _, img_r = cap_r.read()

        if img_l is None or img_r is None:
            break

        objp, imgp_l, imgp_r = stereo_err_calc_obj.get_objp_imgp(img_l, img_r)
        if objp is not None and imgp_l is not None and imgp_r is not None:
            _, rp_l, rp_r = stereo_err_calc_obj.calc_rms_stereo(objp, imgp_l, imgp_r)
        else:
            rp_l = None
            rp_r = None

        if rp_l is not None and rp_r is not None:
            cv2.drawChessboardCorners(img_l, (stereo_err_calc_obj.rows, stereo_err_calc_obj.cols), imgp_l, True)
            cv2.drawChessboardCorners(img_r, (stereo_err_calc_obj.rows, stereo_err_calc_obj.cols), rp_r, True)
        cv2.namedWindow("Left error calc", cv2.WINDOW_GUI_NORMAL)
        cv2.imshow("Left error calc", img_l)
        cv2.namedWindow("Right error calc", cv2.WINDOW_GUI_NORMAL)
        cv2.imshow("Right error calc", img_r)
        k = cv2.waitKey(30)
        if k == 27:
            cv2.destroyAllWindows()
            break


class TestStereoErrorCalc(unittest.TestCase):
    """Stereo error calculation test"""

    def test_stereo_error_calc(self):
        """test error calculation with sample images"""
        calib_settings = "calibration_settings.json"
        calib_id = "CALIB_0_0"
        left_images_path = "data/stereo_images/left"
        right_images_path = "data/stereo_images/right"
        test_obj = StereoErrorCalc(calib_settings, calib_id)
        img_obj_l = FolderReader(folder_path=left_images_path)
        img_obj_r = FolderReader(folder_path=right_images_path)
        while True:
            img_l, _, _ = img_obj_l.next_frame()
            img_r, _, _ = img_obj_r.next_frame()

            if img_l is None or img_r is None or isinstance(img_l, str) or isinstance(img_r, str):
                break

            objp, imgp_l, imgp_r = test_obj.get_objp_imgp(img_l, img_r)
            if objp is not None and imgp_l is not None and imgp_r is not None:
                total_error, _, _ =  test_obj.calc_rms_stereo(objp, imgp_l, imgp_r)
                assert total_error < 15, "Stereo error calculation test failed"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-cs", "--calib_settings", default="calibration_settings.json", help="path for calibration settings json")
    parser.add_argument("-rs", "--realsense", default=False, nargs="?", const=True, help="To record from realsense camera")
    parser.add_argument("-cid", "--calib_id", default="CALIB_0_0", help="camera calibration id for calibration params")

    parser = parser.parse_args()
    calib_settings_ = parser.calib_settings
    realsense_ = parser.realsense
    calib_id_ = parser.calib_id

    error_calc_demo(calib_settings_, calib_id_, realsense_)
