# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : stereo_calib.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""To calibrate stereo camera setup with checkerboard"""
import argparse
import unittest
import os
import sys
import cv2
import numpy as np

from ignutils.file_utils import get_all_files
from ignutils.json_utils import read_json, write_json
from ignutils.calib_utils.angle_utils import rotation_matrix_to_euler
from ignutils.video_utils.folder_reader import FolderReader


class StereoCalib:
    """Calibration class for stereo camera setup"""

    def __init__(self, calib_settings="calibration_settings.json", calib_id="CALIB_0_0", left_images="data/stereo_images/left", right_images="data/stereo_images/right", no_display=False, skip_write=False):
        calib_settings = read_json(calib_settings)
        self.rows = calib_settings["rows"]
        self.cols = calib_settings["cols"]
        self.left_images_path = left_images
        self.right_images_path = right_images
        calib_params_path = os.path.join("data", calib_id)
        self.stereo_result_path = os.path.join(calib_params_path, "stereo_result.json")
        self.left_calib_path = os.path.join(calib_params_path, "left_calib.json")
        self.right_calib_path = os.path.join(calib_params_path, "right_calib.json")
        self.square_size = calib_settings["square_size"]
        self.no_display = no_display
        self.skip_write = skip_write

        self.img_obj_l = FolderReader(folder_path=left_images)
        self.img_obj_r = FolderReader(folder_path=right_images)
        self.img_width = self.img_obj_l.frame_width
        self.img_height = self.img_obj_l.frame_height
        self.stereo_map_l_x = None
        self.stereo_map_l_y = None
        self.stereo_map_r_x = None
        self.stereo_map_r_y = None

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
            raise FileNotFoundError("Left/Right calibration jsons are not available, please mono calibrate and try again")

        if os.path.isfile(self.stereo_result_path):
            stereo_calib_result = read_json(self.stereo_result_path)
            self.rot = np.array(stereo_calib_result["rot"])
            self.trans = np.array(stereo_calib_result["trans"])
            self.proj_l = np.array(stereo_calib_result["proj_l"])
            self.proj_r = np.array(stereo_calib_result["proj_r"])
        else:
            self.rot = None
            self.trans = None
            self.proj_l = None
            self.proj_r = None

    def calibration(self):
        """Stereo calibration func using checkerboard images"""
        # termination criteria
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((self.rows * self.cols, 3), np.float32)
        objp[:, :2] = np.mgrid[0 : self.rows, 0 : self.cols].T.reshape(-1, 2)

        size_of_chessboard_squares_mm = self.square_size
        objp = objp * size_of_chessboard_squares_mm

        # Arrays to store object points and image points from all the images.
        objpoints = []
        imgpoints_l = []
        imgpoints_r = []
        img_l = None
        img_r = None
        count = 0
        total_files = get_all_files(self.left_images_path, exclude_extns=[".json"])
        calib_count = len(total_files)

        while count < calib_count:
            img_l, _, _ = self.img_obj_l.next_frame()
            img_r, _, _ = self.img_obj_r.next_frame()

            if img_l is None or img_r is None or isinstance(img_l, str) or isinstance(img_r, str):
                break

            gray_l = cv2.cvtColor(img_l, cv2.COLOR_BGR2GRAY)
            gray_r = cv2.cvtColor(img_r, cv2.COLOR_BGR2GRAY)

            # Find the chess board corners
            ret_l, corners_l = cv2.findChessboardCorners(gray_l, (self.rows, self.cols), None)
            ret_r, corners_r = cv2.findChessboardCorners(gray_r, (self.rows, self.cols), None)

            # If found, add object points, image points (after refining them)
            if ret_l is True and ret_r is True:
                corners_l = cv2.cornerSubPix(gray_l, corners_l, (11, 11), (-1, -1), criteria)
                corners_r = cv2.cornerSubPix(gray_r, corners_r, (11, 11), (-1, -1), criteria)

                if self.no_display is False:
                    cv2.drawChessboardCorners(img_l, (self.rows, self.cols), corners_l, ret_l)
                    cv2.namedWindow("img left", cv2.WINDOW_GUI_NORMAL)
                    cv2.imshow("img left", img_l)

                    cv2.drawChessboardCorners(img_r, (self.rows, self.cols), corners_r, ret_r)
                    cv2.namedWindow("img right", cv2.WINDOW_GUI_NORMAL)
                    cv2.imshow("img right", img_r)

                objpoints.append(objp)
                imgpoints_l.append(corners_l)
                imgpoints_r.append(corners_r)
                count += 1
                cv2.waitKey(50)

        cv2.destroyAllWindows()
        print("Performing Stereo calibration...")
        flags = cv2.CALIB_FIX_INTRINSIC
        # Here we fix the intrinsic camara matrixes so that only Rot, Trns, Emat and Fmat are calculated.
        # Hence intrinsic parameters are the same

        criteria_stereo = (
            cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
            30,
            0.001,
        )

        # This step is performed to transformation between the two cameras and calculate Essential and Fundamenatl matrix
        ret_stereo, new_mtx_l, dist_l, new_mtx_r, dist_r, self.rot, self.trans, essential_matrix, fundamental_matrix = cv2.stereoCalibrate(  # pylint: disable=W0612
            objpoints,
            imgpoints_l,
            imgpoints_r,
            self.mtx_l,
            self.dist_l,
            self.mtx_r,
            self.dist_r,
            (self.img_width, self.img_height),
            criteria_stereo,
            flags,
        )
        print("cv2 Stereo Calibration Error: ", ret_stereo)
        self.get_proj_matrix()

        rect_left, right_right = self.rectify_image(img_l, img_r)

        if self.no_display is False:
            cv2.namedWindow("Rectified Left", cv2.WINDOW_GUI_NORMAL)
            cv2.namedWindow("Rectified Right", cv2.WINDOW_GUI_NORMAL)
            cv2.imshow("Rectified Left", rect_left)
            cv2.imshow("Rectified Right", right_right)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        return ret_stereo

    def get_proj_matrix(self):
        """Get left and right projection matrix"""
        print("Calculating projection matrix and map values")

        if self.rot is not None and self.trans is not None:
            rectify_scale = 1
            rect_l, rect_r, self.proj_l, self.proj_r, q, roi_l, roi_r = cv2.stereoRectify(self.mtx_l, self.dist_l, self.mtx_r, self.dist_r, (self.img_width, self.img_height), self.rot, self.trans, rectify_scale, (0, 0))  # pylint: disable=W0612
            stereo_map_l = cv2.initUndistortRectifyMap(self.mtx_l, self.dist_l, rect_l, self.proj_l, (self.img_width, self.img_height), cv2.CV_16SC2)
            stereo_map_r = cv2.initUndistortRectifyMap(self.mtx_r, self.dist_r, rect_r, self.proj_r, (self.img_width, self.img_height), cv2.CV_16SC2)
            self.stereo_map_l_x = stereo_map_l[0]
            self.stereo_map_l_y = stereo_map_l[1]
            self.stereo_map_r_x = stereo_map_r[0]
            self.stereo_map_r_y = stereo_map_r[1]

            if self.skip_write is False:
                self.write_result()
        else:
            print("Rotation and translation values are not available, please calibrate")
            sys.exit()

    def write_result(self):
        """Saving stereo calibration and map results"""
        if self.rot is not None and self.trans is not None and self.proj_l is not None and self.proj_r is not None:
            print("Writing stereo result")
            rot_angle = rotation_matrix_to_euler(self.rot)
            stereo_result = {"rot": self.rot.tolist(), "rot_angle": rot_angle.tolist(), "trans": self.trans.tolist(), "proj_l": self.proj_l.tolist(), "proj_r": self.proj_r.tolist()}
            write_json(self.stereo_result_path, stereo_result)

    def rectify_image(self, left_img, right_img):
        """Rectify left and right images

        Args:
            left_img (np.ndarray): Input left image
            right_img (_type_): Input right image

        Returns:
            np.ndarray: left and right rectified images
        """
        undistorted_l = cv2.remap(
            left_img,
            self.stereo_map_l_x,
            self.stereo_map_l_y,
            cv2.INTER_LANCZOS4
        )

        undistorted_r = cv2.remap(
            right_img,
            self.stereo_map_r_x,
            self.stereo_map_r_y,
            cv2.INTER_LANCZOS4
        )

        return undistorted_l, undistorted_r

    def check_rectification(self, left_img, right_img):
        """Check if rectification is proper given left and right images

        Args:
            left_img (np.ndarray): Left input image
            right_img (np.ndarray): Right input image
        """
        left_rect, right_rect = self.rectify_image(left_img, right_img)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((self.rows * self.cols, 3), np.float32)
        objp[:, :2] = np.mgrid[0 : self.rows, 0 : self.cols].T.reshape(-1, 2)

        size_of_chessboard_squares_mm = self.square_size
        objp = objp * size_of_chessboard_squares_mm

        gray_l = cv2.cvtColor(left_rect, cv2.COLOR_BGR2GRAY)
        gray_r = cv2.cvtColor(right_rect, cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret_l, corners_l = cv2.findChessboardCorners(gray_l, (self.rows, self.cols), None)
        ret_r, corners_r = cv2.findChessboardCorners(gray_r, (self.rows, self.cols), None)

        # If found, add object points, image points (after refining them)
        if ret_l is True and ret_r is True:
            corners_l = cv2.cornerSubPix(gray_l, corners_l, (11, 11), (-1, -1), criteria)
            corners_r = cv2.cornerSubPix(gray_r, corners_r, (11, 11), (-1, -1), criteria)

            conc_img = np.concatenate((left_rect, right_rect), axis=1)

            img_width = left_img.shape[1]

            for cor_l, cor_r in zip(corners_l, corners_r):
                x = int(cor_l[0][0])
                y = int(cor_l[0][1])
                cv2.circle(conc_img, (x, y), 5, (255, 255, 0), -1)
                cv2.line(conc_img, (0, y), (conc_img.shape[1], y), (0, 0, 255), 1)

                x1 = int(cor_r[0][0]) + img_width
                y1 = int(cor_r[0][1])
                cv2.circle(conc_img, (x1, y1), 5, (255, 255, 0), -1)
                cv2.line(conc_img, (x, y), (x1, y1), (0, 255, 0), 1)

            cv2.namedWindow("check rect", cv2.WINDOW_GUI_NORMAL)
            cv2.imshow("check rect", conc_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


class TestStereoCalib(unittest.TestCase):
    """Stereo calib test"""

    def test_stereo_calib(self):
        """test calbration with sample images"""
        calib_settings = "calibration_settings.json"
        calib_id = "CALIB_0_0"
        left_images_path = "data/stereo_images/left"
        right_images_path = "data/stereo_images/right"
        no_display, skip_write = True, True
        calib_obj = StereoCalib(calib_settings, calib_id, left_images_path, right_images_path, no_display, skip_write)
        calib_error = calib_obj.calibration()
        assert calib_error < 10, "Stereo calibration test failed"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-cs", "--calib_settings", default="calibration_settings.json", help="path for calibration settings json")
    parser.add_argument("-li", "--left_images", default="data/stereo_images/left", help="left input images")
    parser.add_argument("-ri", "--right_images", default="data/stereo_images/right", help="right input images")
    parser.add_argument("-nd", "--no_display", default=False, nargs="?", const=True, help="Dont show calibration image output")
    parser.add_argument("-cb", "--calibration", default=False, nargs="?", const=True, help="Do Calibration for new set")
    parser.add_argument("-gp", "--get_projection", default=False, nargs="?", const=True, help="Update projection matrix")
    parser.add_argument("-sw", "--skip_write", default=False, nargs="?", const=True, help="To write result json")
    parser.add_argument("-cid", "--calib_id", default="CALIB_0_0", help="camera calibration id for calibration params")

    parser = parser.parse_args()
    calib_settings_ = parser.calib_settings
    left_images_ = parser.left_images
    right_images_ = parser.right_images
    no_display_ = parser.no_display
    calibration_ = parser.calibration
    get_projection_ = parser.get_projection
    skip_write_ = parser.skip_write
    calib_id_ = parser.calib_id

    calib_obj = StereoCalib(calib_settings_, calib_id_, left_images_, right_images_, no_display_, skip_write_)

    if calibration_:
        calib_obj.calibration()

    if get_projection_:
        calib_obj.get_proj_matrix()
