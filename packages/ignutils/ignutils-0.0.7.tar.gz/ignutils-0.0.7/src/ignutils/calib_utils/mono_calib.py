"""Calibration for Mono camera"""
import argparse
import os
import unittest
import cv2
import numpy as np

from ignutils.file_utils import get_all_files
from ignutils.json_utils import read_json, write_json
from ignutils.video_utils.folder_reader import FolderReader


class MonoCalib: # pylint: disable=R0903
    """Mono calibration using checker images"""

    def __init__(self, calib_settings="calibration_settings.json", calib_id="CALIB_0_0", images_path="data/mono_images/left", no_display=False, skip_write=False):
        calib_settings = read_json(calib_settings)
        self.rows = calib_settings["rows"]
        self.cols = calib_settings["cols"]
        calib_path = os.path.join("data", calib_id)
        if os.path.isdir(calib_path) is False:
            os.makedirs(calib_path)
        self.images_path = images_path
        self.img_obj = FolderReader(folder_path=self.images_path)
        _, tail = os.path.split(self.images_path)
        self.result_path = os.path.join(calib_path, f"{tail}_calib.json")
        self.square_size = calib_settings["square_size"]
        self.no_display = no_display
        self.skip_write = skip_write

        if os.path.isfile(self.result_path):
            calibration_result = read_json(self.result_path)
            self.mtx = np.array(calibration_result["mtx"])
            self.dist = np.array(calibration_result["dist"])

        else:
            self.calibration()

    def calibration(self):
        """Calibrating using checker board"""
        # refer: https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html
        # termination criteria
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((self.rows * self.cols, 3), np.float32)
        objp[:, :2] = np.mgrid[0 : self.rows, 0 : self.cols].T.reshape(-1, 2)

        # Size of the checkerboard
        size_of_chessboard_squares_mm = self.square_size
        objp = objp * size_of_chessboard_squares_mm

        # Arrays to store object points and image points from all the images.
        objpoints = []  # 3d point in real world space
        imgpoints = []  # 2d points in image plane.
        count = 0
        gray = None
        total_files = get_all_files(self.images_path, exclude_extns=[".json"])
        calib_count = len(total_files)

        while count < (calib_count):
            img, _, _ = self.img_obj.next_frame()
            if img is None or isinstance(img, str):
                break
            # Find the chess board corners
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, corners = cv2.findChessboardCorners(gray, (self.rows, self.cols), cv2.CALIB_CB_FAST_CHECK)

            if ret is True:
                corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                cv2.drawChessboardCorners(img, (self.rows, self.cols), corners2, ret)
                objpoints.append(objp)
                imgpoints.append(corners2)
                print(f"Image added {count}", end="\r")
                if self.no_display is False:
                    cv2.namedWindow("Calibration", cv2.WINDOW_GUI_NORMAL)
                    cv2.imshow("Calibration", img)
                    cv2.waitKey(30)
                count += 1

            else:
                print("Checkerboard not detected")

        cv2.destroyAllWindows()
        print("\n Performing camera calibration...")
        img_shp = None
        if gray is not None:
            img_shp = gray.shape[::-1]
        retval, mtx, dist, rvecs, tvecs, std_deviations_intrinsics, std_deviations_extrinsics, per_view_errors = cv2.calibrateCameraExtended(objpoints, imgpoints, img_shp, None, None)  # pylint: disable=W0612

        print("Camera matrix : \n")
        print(mtx)
        print("dist : \n")
        print(dist)
        print("per view errors: \n")
        print(per_view_errors)
        print(f"Calibration error: {retval}")
        print("Writing the output...")

        if self.skip_write is False:
            calibration_result = {"mtx": mtx.tolist(), "dist": dist.tolist()}
            write_json(self.result_path, calibration_result)

        return retval


class TestStereoCalib(unittest.TestCase):
    """Stereo calib test"""

    def test_stereo_calib(self):
        """test calbration with sample images"""
        calib_settings = "calibration_settings.json"
        calib_id = "CALIB_0_0"
        images_path = "data/stereo_images/left"
        no_display, skip_write = True, True
        calib_obj = MonoCalib(calib_settings, calib_id, images_path, no_display, skip_write)
        calib_error = calib_obj.calibration()
        assert calib_error < 10, "Stereo calibration test failed"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-cs", "--calib_settings", default="calibration_settings.json", help="path for calibration settings json")
    parser.add_argument("-cid", "--calib_id", default="CALIB_0_0", help="Calibration id for the camera")
    parser.add_argument("-p", "--image_path", default="data/mono_images/left", help="path for calibration images")
    parser.add_argument("-nd", "--no_display", default=False, nargs="?", const=True, help="Dont show calibration image output")
    parser.add_argument("-cb", "--calibration", default=False, nargs="?", const=True, help="Do Calibration for new set")
    parser.add_argument("-sw", "--skip_write", default=False, nargs="?", const=True, help="To write result json")

    parser = parser.parse_args()
    calib_settings_ = parser.calib_settings
    calib_id_ = parser.calib_id
    image_path_ = parser.image_path
    no_display_ = parser.no_display
    calibration_ = parser.calibration
    skip_write_ = parser.skip_write

    calib_obj = MonoCalib(calib_settings_, calib_id_, image_path_, no_display_, skip_write_)

    if calibration_:
        calib_obj.calibration()
