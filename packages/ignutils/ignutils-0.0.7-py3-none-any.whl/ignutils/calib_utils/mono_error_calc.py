"""To find error for mono calibration"""
import argparse
import os
import unittest
import cv2
import numpy as np

from ignutils.cam_utils.camera_reader import CameraReader
from ignutils.cam_utils.realsense_reader import RealSenseReader
from ignutils.json_utils import read_json
from ignutils.video_utils.folder_reader import FolderReader


class MonoErrorCalc:
    """For calculating mono calibration error"""

    def __init__(self, calib_settings="calibration_settings.json", calib_id="CALIB_O_O", cam_name="left"):
        calib_settings = read_json(calib_settings)
        self.rows = calib_settings["rows"]
        self.cols = calib_settings["cols"]
        self.left_id = calib_settings["left_id"]
        self.right_id = calib_settings["right_id"]
        self.cam_name = cam_name
        calib_path = os.path.join("data", calib_id)
        if os.path.isdir(calib_path) is False:
            os.makedirs(calib_path)
        self.calib_path = os.path.join(calib_path, f"{self.cam_name}_calib.json")
        self.square_size = calib_settings["square_size"]

        if os.path.isfile(self.calib_path):
            print(f"Reading calib json {self.calib_path}")
            calibration_result = read_json(self.calib_path)
            self.mtx = np.array(calibration_result["mtx"])
            self.dist = np.array(calibration_result["dist"])

        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        objp = np.zeros((self.rows * self.cols, 3), np.float32)
        objp[:, :2] = np.mgrid[0 : self.rows, 0 : self.cols].T.reshape(-1, 2)

        size_of_chessboard_squares_mm = self.square_size
        self.objp = objp * size_of_chessboard_squares_mm

    def get_obj_imgp(self, image):
        """Get object and image points for an image

        Args:
            image (np.ndarray): Input image

        Returns:
            np.ndarray: object and image points
        """
        objpoints = []
        imgpoints = []
        gray = image if image.ndim == 2 else cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, (self.rows, self.cols), cv2.CALIB_CB_FAST_CHECK)

        if ret is True:
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), self.criteria)
            cv2.drawChessboardCorners(image, (self.rows, self.cols), corners2, ret)
            objpoints = self.objp
            imgpoints = corners2
        else:
            objpoints = None
            imgpoints = None
            print("Checker board not detected")

        return objpoints, imgpoints

    def calc_rms_mono(self, objectpoints, imgpoints):
        """Re-projection error calc for mono calibration

        Args:
            objectpoints (np.ndarray): object points
            imgpoints (np.ndarray): image points

        Returns:
            float: Left and right reprojection error
        """
        _, rvecs, tvecs, _ = cv2.solvePnPRansac(objectpoints, imgpoints, self.mtx, self.dist)
        imgpoints2, _ = cv2.projectPoints(objectpoints, rvecs, tvecs, self.mtx, self.dist)
        error = cv2.norm(imgpoints, imgpoints2, cv2.NORM_L2) / len(imgpoints2)
        print(f"Reprojection error: {error}")

        return error, imgpoints2


def error_calc_demo(calib_settings, calib_id, cam_name, realsense=False):
    """Demo for calculating error on a live feed/video

    Args:
        cam_id (int): Camera index
    """
    err_obj = MonoErrorCalc(calib_settings, calib_id, cam_name)
    rs_cam_obj, cap, img = None, None, None
    if realsense:
        rs_cam_obj = RealSenseReader()
    else:
        setting_path = "data/left_setting.json" if err_obj.cam_name == "left" else "data/right_setting.json"
        cam_id = err_obj.left_id if err_obj.cam_name == "left" else err_obj.right_id
        cam_obj = CameraReader(cam_index=cam_id, ui_flag=True, setting_path=setting_path)
        cap = cam_obj.get_cap()

    while True:
        if realsense and rs_cam_obj is not None:
            _, left_img, right_img = rs_cam_obj.get_left_right()
            img = left_img if cam_name == "left" else right_img
        else:
            if cap is not None:
                _, img = cap.read()

        if img is None:
            break
        objp, imgp = err_obj.get_obj_imgp(img)
        imgp2 = None
        if objp is not None and imgp is not None:
            _, imgp2 = err_obj.calc_rms_mono(objp, imgp)

        if imgp2 is not None:
            cv2.drawChessboardCorners(img, (err_obj.rows, err_obj.cols), imgp2, True)
        cv2.namedWindow("Error calc", cv2.WINDOW_GUI_NORMAL)
        cv2.imshow("Error calc", img)
        k = cv2.waitKey(30)
        if k == 27:
            cv2.destroyAllWindows()
            break


class TestMonoErrorCalc(unittest.TestCase):
    """Mono error calculation test"""

    def test_mono_error_calc(self):
        """test mono error calculation with sample images"""
        calib_settings = "calibration_settings.json"
        calib_id = "CALIB_0_0"
        images_path = "data/stereo_images/left"
        test_obj = MonoErrorCalc(calib_settings, calib_id)
        img_obj = FolderReader(folder_path=images_path)
        while True:
            img, _, _ = img_obj.next_frame()
            if img is None or isinstance(img, str):
                break

            objp, imgp = test_obj.get_obj_imgp(img)
            if objp is not None and imgp is not None:
                total_error, _ =  test_obj.calc_rms_mono(objp, imgp)
                assert total_error < 15, "Stereo error calculation test failed"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-cs", "--calib_settings", default="calibration_settings.json", help="path for calibration settings json")
    parser.add_argument("-cid", "--calib_id", default="CALIB_0_0", help="Calibration id for the camera")
    parser.add_argument("-cn", "--cam_name", default="left", help="Camera name left/right")
    parser.add_argument("-rs", "--realsense", default=False, nargs="?", const=True, help="To record from realsense camera")

    parser = parser.parse_args()
    calib_settings_ = parser.calib_settings
    calib_id_ = parser.calib_id
    cam_name_ = parser.cam_name
    realsense_ = parser.realsense

    error_calc_demo(calib_settings_, calib_id_, cam_name_, realsense_)
