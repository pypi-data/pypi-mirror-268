"""Undistort mono camera live"""
import argparse
import os
import cv2
import numpy as np

from ignutils.cam_utils.camera_reader import CameraReader
from ignutils.cam_utils.realsense_reader import RealSenseReader
from ignutils.json_utils import read_json


class Undistort:
    """Apply undistortion for image"""

    def __init__(self, cam_name="left", calib_id="CALIB_0_0", calib_settings="calibration_settings.json"):
        self.cam_name = cam_name
        self.settings = read_json(calib_settings)
        calib_json = cam_name + "_calib.json"
        self.result_path = os.path.join("data", calib_id, calib_json)

        if os.path.isfile(self.result_path):
            calibration_result = read_json(self.result_path)
            self.mtx = np.array(calibration_result["mtx"])
            self.dist = np.array(calibration_result["dist"])

            print(f"Calibration result file already exists {self.result_path}.")
            print("Camera matrix : \n")
            print(self.mtx)
            print("dist : \n")
            print(self.dist)
        else:
            raise FileNotFoundError("Calibration result files not found, please calibrate and try again")

    def undistortion(self, img, show=False):
        """Undistort given image using the mtx, dist"""

        dst = cv2.undistort(img, self.mtx, self.dist)
        if show:
            cv2.imshow("Original image", img)
            cv2.imshow("Undistorted Image", dst)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        return dst

    def undistortion_demo(self, realsense=False):
        """Live undistortion on video or cam

        Args:
            cam_id (int, str): cam id/path to video
        """
        cap, image, rs_cam_obj = None, None, None
        if realsense:
            rs_cam_obj = RealSenseReader()
        else:
            cam_id = self.settings["left_id"] if self.cam_name == "left" else self.settings["right_id"]
            cam_obj = CameraReader(cam_index=cam_id, ui_flag=True)
            cap = cam_obj.get_cap()

        cv2.namedWindow("Original image", cv2.WINDOW_GUI_NORMAL)
        cv2.namedWindow("Undistorted Image", cv2.WINDOW_GUI_NORMAL)
        while True:
            if realsense and rs_cam_obj is not None:
                _, left_img, right_img = rs_cam_obj.get_left_right()
                image = left_img if self.cam_name == "left" else right_img
            else:
                if cap is not None:
                    _, image = cap.read()

            if image is None:
                break

            undist_img = self.undistortion(image)
            cv2.imshow("Original image", image)
            cv2.imshow("Undistorted Image", undist_img)
            k = cv2.waitKey(30)
            if k == 27:
                break
        cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-cn", "--cam_name", default="left", type=str, help="Camera name left/right")
    parser.add_argument("-cid", "--calib_id", default="CALIB_0_0", help="camera calibration id for calibration params")
    parser.add_argument("-rs", "--realsense", default=False, nargs="?", const=True, help="To record from realsense camera")
    parser.add_argument("-cs", "--calib_settings", default="calibration_settings.json", help="path for calibration settings json")

    parser = parser.parse_args()
    cam_name_ = parser.cam_name
    calib_id_ = parser.calib_id
    realsense_ = parser.realsense
    calib_settings_ = parser.calib_settings

    undist_obj = Undistort(cam_name_, calib_id_, calib_settings_)
    undist_obj.undistortion_demo(realsense=realsense_)
