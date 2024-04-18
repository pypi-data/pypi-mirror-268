"""Charuco based mono camera calibration"""
import os
import unittest
import argparse
import numpy as np
import cv2

from ignutils.file_utils import get_all_files
from ignutils.json_utils import read_json, write_json
from ignutils.video_utils.folder_reader import FolderReader


class CharucoMonoCalib:
    """Mono calibration using charuco images"""

    def __init__(self, calib_settings="calibration_settings.json", images_path="data/mono_images/left", no_display=False):
        calib_settings = read_json(calib_settings)
        self.rows = calib_settings["rows"]
        self.cols = calib_settings["cols"]
        self.images_path = images_path
        self.img_obj = FolderReader(folder_path=self.images_path)
        _, tail = os.path.split(self.images_path)
        self.result_path = f"data/{tail}_calib.json"
        self.square_size = calib_settings["square_size"]
        self.marker_size = calib_settings["marker_size"]
        self.charuco_dict = calib_settings["charuco_dict"]
        self.img_width = calib_settings["frame_width"]
        self.img_height = calib_settings["frame_height"]
        self.no_display = no_display

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
            self.calibration()

    def calibration(self):
        """Calibrating using charuco board"""
        aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
        # Note: Pattern generated using the following link
        # https://calib.io/pages/camera-calibration-pattern-generator
        board = cv2.aruco.CharucoBoard_create(self.rows, self.cols, self.square_size, self.marker_size, aruco_dict)

        all_corners = []
        all_ids = []
        count = 0
        total_files = get_all_files(self.images_path, exclude_extns=[".json"])
        calib_count = len(total_files)

        cv2.namedWindow("calib", cv2.WINDOW_GUI_NORMAL)
        while count < (calib_count):
            img, _, _ = self.img_obj.next_frame()
            if img is None or isinstance(img, str):
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            corners, ids, rejected_img_points = cv2.aruco.detectMarkers(gray, aruco_dict)

            if len(corners) > 0:
                ret, c_corners, c_ids = cv2.aruco.interpolateCornersCharuco(corners, ids, gray, board)
                imaxis = cv2.aruco.drawDetectedCornersCharuco(img.copy(), c_corners, c_ids)

                # ret is the number of detected corners
                if ret > 0:
                    all_corners.append(c_corners)
                    all_ids.append(c_ids)
                    print(f"Image added {count}", end="\r")

                if self.no_display is False:
                    cv2.imshow("calib", imaxis)
                    cv2.waitKey(0)

                count += 1

            else:
                print("Charuco board not detected")

        cv2.destroyAllWindows()
        print("\n Performing camera calibration...")
        ret, mtx, dist, rvec, tvec, _, _, per_view_errors = cv2.aruco.calibrateCameraCharucoExtended(all_corners, all_ids, board, (self.img_width, self.img_height), None, None)

        print("Camera matrix : \n")
        print(mtx)
        print("dist : \n")
        print(dist)
        print("per view errors: \n")
        print(per_view_errors)
        print(f"Calibration error: {ret}")
        print("Writing the output...")

        calibration_result = {"mtx": mtx.tolist(), "dist": dist.tolist()}
        write_json(self.result_path, calibration_result)
        return ret

class TestStereoCalib(unittest.TestCase):
    """Stereo calib test"""

    def test_stereo_calib(self):
        """test calbration with sample images"""
        calib_settings = "calibration_settings.json"
        calib_id = "CALIB_0_0"
        images_path = "data/stereo_images/left"
        no_display, skip_write = True, True
        calib_obj = CharucoMonoCalib(calib_settings, images_path, no_display)
        calib_error = calib_obj.calibration()
        assert calib_error < 10, "Stereo calibration test failed"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-cs", "--calib_settings", default="calibration_settings.json", help="path for calibration settings json")
    parser.add_argument("-p", "--image_path", default="data/mono_images/left", help="path for calibration images")
    parser.add_argument("-nd", "--no_display", default=False, nargs="?", const=True, help="Dont show calibration image output")

    parser = parser.parse_args()
    calib_settings_ = parser.calib_settings
    image_path_ = parser.image_path
    no_display_ = parser.no_display

    calib_obj = CharucoMonoCalib(calib_settings_, image_path_, no_display_)
