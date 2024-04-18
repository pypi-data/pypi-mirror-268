# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : charuco_stereo_calib.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""To calibrate stereo camera setup with charucoboard"""
import argparse
import os
import unittest
import cv2
import numpy as np

from ignutils.file_utils import get_all_files
from ignutils.json_utils import read_json, write_json
from ignutils.video_utils.folder_reader import FolderReader


class CharucoStereoCalib:
    """Calibration class for stereo camera setup"""

    def __init__(self, calib_settings="calibration_settings.json", left_images="data/stereo_images/left", right_images="data/stereo_images/right", no_display=False):
        calib_settings = read_json(calib_settings)
        self.rows = calib_settings["rows"]
        self.cols = calib_settings["cols"]
        self.left_images_path = left_images
        self.right_images_path = right_images
        self.left_calib_path = calib_settings["left_calib_path"]
        self.right_calib_path = calib_settings["right_calib_path"]
        self.stereo_map_path = calib_settings["stereo_map_path"]
        self.stereo_result_path = calib_settings["stereo_result_path"]
        self.square_size = calib_settings["square_size"]
        self.marker_size = calib_settings["marker_size"]
        self.charuco_dict = calib_settings["charuco_dict"]
        self.no_display = no_display

        self.img_obj_l = FolderReader(folder_path=left_images)
        self.img_obj_r = FolderReader(folder_path=right_images)
        self.img_width = self.img_obj_l.frame_width
        self.img_height = self.img_obj_l.frame_height

        # define names of each possible ArUco tag OpenCV supports
        self.aruco_dict_types = {
            "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
            "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
            "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
            "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
            "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
            "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
            "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
            "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
            "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
            "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
            "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
            "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
            "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
            "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
            "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
            "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
            "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
            "DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
            "DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
            "DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
            "DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11,
        }

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

        if os.path.isfile(self.stereo_map_path) and os.path.isfile(self.stereo_result_path):
            print(f"Reading stereo calibration results {self.stereo_result_path}")
            stereo_map_result = np.load(self.stereo_map_path)
            self.stereo_map_l_x = stereo_map_result["stereoMapL_x"]
            self.stereo_map_l_y = stereo_map_result["stereoMapL_y"]
            self.stereo_map_r_x = stereo_map_result["stereoMapR_x"]
            self.stereo_map_r_y = stereo_map_result["stereoMapR_y"]

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
        aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_1000)
        # Note: Pattern generated using the following link
        # https://calib.io/pages/camera-calibration-pattern-generator
        board = cv2.aruco.CharucoBoard_create(self.rows, self.cols, self.square_size, self.marker_size, aruco_dict)
        aruco_params = cv2.aruco.DetectorParameters_create()
        charuco_chessboard_corners = board.chessboardCorners

        # Arrays to store object points and image points from all the images.
        objpoints = []
        imgpoints_l = []
        imgpoints_r = []
        imaxis_l = None
        img_l = None
        img_r = None
        count = 0
        total_files = get_all_files(self.left_images_path, exclude_extns=[".json"])
        calib_count = len(total_files)

        while count < calib_count:
            img_l, _, _ = self.img_obj_l.next_frame()
            img_r, _, _ = self.img_obj_r.next_frame()

            if img_l is None or isinstance(img_l, str) or img_r is None or isinstance(img_r, str):
                break

            gray_l = cv2.cvtColor(img_l, cv2.COLOR_BGR2GRAY)
            gray_r = cv2.cvtColor(img_r, cv2.COLOR_BGR2GRAY)

            # Find the chess board corners
            d_corners_l, d_ids_l, rejected_img_points_l = cv2.aruco.detectMarkers(gray_l, aruco_dict, parameters=aruco_params)
            d_corners_r, d_ids_r, rejected_img_points_r = cv2.aruco.detectMarkers(gray_r, aruco_dict, parameters=aruco_params)

            # If found, add object points, image points (after refining them)
            if len(d_corners_l) > 0 and len(d_corners_r) > 0:
                ret_l, corners_l, ids_l = cv2.aruco.interpolateCornersCharuco(d_corners_l, d_ids_l, gray_l, board)
                ret_r, corners_r, ids_r = cv2.aruco.interpolateCornersCharuco(d_corners_r, d_ids_r, gray_r, board)

                # if ret_l > 0 and ret_r > 0:
                #     obj_pts, img_pts_l = cv2.aruco.getBoardObjectAndImagePoints(board, corners_l, ids_l)
                #     obj_pts, img_pts_r = cv2.aruco.getBoardObjectAndImagePoints(board, corners_r, ids_r)

                if self.no_display is False:
                    imaxis_l = cv2.aruco.drawDetectedCornersCharuco(img_l.copy(), corners_l, ids_l)
                    cv2.namedWindow("img left", cv2.WINDOW_GUI_NORMAL)
                    cv2.imshow("img left", imaxis_l)

                    imaxis_r = cv2.aruco.drawDetectedCornersCharuco(img_r.copy(), corners_r, ids_r)
                    cv2.namedWindow("img right", cv2.WINDOW_GUI_NORMAL)
                    cv2.imshow("img right", imaxis_r)

                objpoints.append(charuco_chessboard_corners)
                imgpoints_l.append(corners_l.reshape(-1, 2))
                imgpoints_r.append(corners_r.reshape(-1, 2))
                count += 1
                cv2.waitKey(30)

        cv2.destroyAllWindows()

        print("Performing Stereo calibration...")
        flags = cv2.CALIB_FIX_INTRINSIC
        # Here we fix the intrinsic camara matrixes so that only Rot, Trns, Emat and Fmat are calculated.
        # Hence intrinsic parameters are the same

        criteria_stereo = (
            cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
            100,
            1e-5,
        )
        # This step is performed to transformation between the two cameras and calculate Essential and Fundamenatl matrix
        (ret_stereo, new_mtx_l, dist_l, new_mtx_r, dist_r, self.rot, self.trans, essential_matrix, fundamental_matrix, per_view_errors) = cv2.stereoCalibrateExtended(  # pylint: disable=W0612
            objpoints,
            imgpoints_l,
            imgpoints_r,
            self.mtx_l,
            self.dist_l,
            self.mtx_r,
            self.mtx_r,
            (self.img_width, self.img_height),
            criteria_stereo,
            flags,
        )
        print("Per view errors: ", per_view_errors)
        print("cv2 Stereo Calibration Error: ", ret_stereo)
        self.get_proj_matrix()

        if imaxis_l is not None and img_r is not None:
            rect_left, right_right = self.rectify_image(imaxis_l, img_r)

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

        if self.rot is not None and self.trans is not None and self.proj_l is not None and self.proj_r is not None:
            # rectify_scale = 1
            rect_l, rect_r, self.proj_l, self.proj_r, q, roi_l, roi_r = cv2.stereoRectify(self.mtx_l, self.dist_l, self.mtx_r, self.dist_r, (self.img_width, self.img_height), self.rot, self.trans)  # , rectify_scale, (0, 0))  # pylint: disable=W0612
            stereo_map_l = cv2.initUndistortRectifyMap(self.mtx_l, self.dist_l, rect_l, self.mtx_l, (self.img_width, self.img_height), cv2.CV_16SC2)
            stereo_map_r = cv2.initUndistortRectifyMap(self.mtx_r, self.dist_r, rect_r, self.mtx_r, (self.img_width, self.img_height), cv2.CV_16SC2)

            self.stereo_map_l_x = stereo_map_l[0]
            self.stereo_map_l_y = stereo_map_l[1]
            self.stereo_map_r_x = stereo_map_r[0]
            self.stereo_map_r_y = stereo_map_r[1]
            self.write_result()

        else:
            raise Exception("Rotation and translation values are not available, please calibrate") # pylint: disable=W0719

    def write_result(self):
        """Saving stereo calibration and map results"""
        if self.rot is not None and self.trans is not None and self.proj_l is not None and self.proj_r is not None:
            print("Writing stereo result")
            stereo_result = {"rot": self.rot.tolist(), "trans": self.trans.tolist(), "proj_l": self.proj_l.tolist(), "proj_r": self.proj_r.tolist()}
            write_json(self.stereo_result_path, stereo_result)
            np.savez(self.stereo_map_path, stereoMapL_x=self.stereo_map_l_x, stereoMapL_y=self.stereo_map_l_y, stereoMapR_x=self.stereo_map_r_x, stereoMapR_y=self.stereo_map_r_y)

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

        cv2.imwrite("rect_left.png", undistorted_l)
        cv2.imwrite("rect_right.png", undistorted_r)

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


class TestCharucoStereoCalib(unittest.TestCase):
    """Stereo calib test"""

    def test_charuco_stereo_calib(self):
        """test calbration with sample images"""
        calib_settings = "calibration_settings.json"
        left_images_path = "data/stereo_images/left"
        right_images_path = "data/stereo_images/right"
        no_display = True
        calib_obj = CharucoStereoCalib(calib_settings, left_images_path, right_images_path, no_display)
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

    parser = parser.parse_args()
    calib_settings_ = parser.calib_settings
    left_images_ = parser.left_images
    right_images_ = parser.right_images
    no_display_ = parser.no_display
    calibration_ = parser.calibration
    get_projection_ = parser.get_projection

    calib_obj = CharucoStereoCalib(calib_settings_, left_images_, right_images_, no_display_)

    if calibration_:
        calib_obj.calibration()
