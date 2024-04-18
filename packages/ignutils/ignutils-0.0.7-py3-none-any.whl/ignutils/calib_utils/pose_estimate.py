"""To estimate the pose of a checkerboard image"""
import argparse
import os
import unittest
import cv2
import numpy as np

from ignutils.cam_utils.camera_reader import CameraReader
from ignutils.cam_utils.realsense_reader import RealSenseReader
from ignutils.draw_utils import put_text
from ignutils.json_utils import read_json
from ignutils.video_utils.folder_reader import FolderReader


class PoseEstimate:
    """Class to estimate pose for given checker board images"""

    def __init__(self, calib_settings="calibration_settings.json", calib_path="data/left_calib.json"):
        calib_settings = read_json(calib_settings)
        self.rows = calib_settings["rows"]
        self.cols = calib_settings["cols"]
        self.left_id = calib_settings["left_id"]
        self.right_id = calib_settings["right_id"]
        self.calib_path = calib_path
        self.square_size = calib_settings["square_size"]
        self.camera_position_list = []

        if os.path.isfile(self.calib_path):
            print(f"Using calib result from json {self.calib_path}")
            calibration_result = read_json(self.calib_path)
            self.mtx = np.array(calibration_result["mtx"])
            self.dist = np.array(calibration_result["dist"])

        else:
            print("Using default calibration values")
            self.mtx = np.array(
                [
                    [1000, 0.0, 640],
                    [0.0, 1006, 360],
                    [0.0, 0.0, 1.0],
                ]
            )
            self.dist = np.array([[0.0, 0.0, 0.0, 0.0, 0.0]])

    def checker_draw(self, image, corners, imgpts):
        """Given corners of checker board draw the axis

        Args:
            image (np.array): Input image
            corners (np.array): Corner points of checker board
            imgpts (np.array): Image points of checker board

        Returns:
            np.array: Image with xyz axis
        """
        corner = tuple(corners[0].ravel())
        corner = (int(corner[0]), int(corner[1]))
        imgpts1 = (int(imgpts[0].ravel()[0]), int(imgpts[0].ravel()[1]))
        imgpts2 = (int(imgpts[1].ravel()[0]), int(imgpts[1].ravel()[1]))
        imgpts3 = (int(imgpts[2].ravel()[0]), int(imgpts[2].ravel()[1]))
        image = cv2.line(image, corner, imgpts1, (255, 0, 0), 5)
        image = cv2.line(image, corner, imgpts2, (0, 255, 0), 5)
        image = cv2.line(image, corner, imgpts3, (0, 0, 255), 5)
        # corner_img = cv2.drawChessboardCorners(image, (self.cols, self.rows), imgpts, ret)
        return image

    def get_checker_corners(self, image, fast=False, gray=False):
        """Get checker board corners and object points

        Args:
            image (np.array): Input image to detect corners

        Returns:
            np.array: Corner points
            np.array: Object points
        """
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        objp = np.zeros((self.rows * self.cols, 3), np.float32)
        objp[:, :2] = np.mgrid[0 : self.rows, 0 : self.cols].T.reshape(-1, 2)
        size_of_chessboard_squares_mm = self.square_size
        objp = objp * size_of_chessboard_squares_mm
        gray = image if image.ndim == 2 else cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, (self.rows, self.cols), cv2.CALIB_CB_FAST_CHECK)
        corner_img = None
        if ret is True:
            if not fast:
                corners = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            corner_img = cv2.drawChessboardCorners(image, (self.rows, self.cols), corners, ret)
        else:
            corners = None
        return corners, objp, corner_img

    def get_checker_pose(self, image, show=False):
        """Get the checker board corner xyz position given an image
            refer: https://docs.opencv.org/4.x/d7/d53/tutorial_py_pose.html

        Args:
            image (np.array): Input image
            show (bool, optional): Show the output image. Defaults to False.

        Returns:
            np.array: Image points of corners
            np.array: Image with Checker pose
        """
        axis = np.array([[self.square_size, 0, 0], [0, self.square_size, 0], [0, 0, -self.square_size]], dtype=np.float32).reshape(-1, 3)

        # image1 = image.copy()
        corners, objp, _ = self.get_checker_corners(image)
        imgpts = None
        axis_image = None
        if corners is not None:
            # Find the rotation and translation vectors.
            _, rvecs, tvecs = cv2.solvePnP(objp, corners, self.mtx, self.dist)
            # project 3D points to image plane
            imgpts, _ = cv2.projectPoints(axis, rvecs, tvecs, self.mtx, self.dist)
            axis_image = self.checker_draw(image, corners, imgpts)

        if show:
            cv2.imshow("img", axis_image)
            k = cv2.waitKey(0) & 0xFF
            if k == ord("s"):
                cv2.imwrite("checker_pose.png", axis_image)

            cv2.destroyAllWindows()

        return imgpts, axis_image

    def add_cam_pos(self, camera_position):
        """Add current position to list of camera positions

        Args:
            camera_position (list): XYZ position
        """
        self.camera_position_list.append(camera_position)

    def calc_cam_pos(self, corners, obj_points):
        """Calculate the xyz position of camera wrt to checker board

        Args:
            corners (np.array): Corner points of checker/charuco
            obj_points (np.array): Object points or ids of corners

        Returns:
            np.array: XYZ camera position wrt to board
        """
        _, rvec, tvec = cv2.solvePnP(obj_points, corners, self.mtx, self.dist, flags=cv2.SOLVEPNP_EPNP)

        rot_m = cv2.Rodrigues(rvec)[0]
        camera_position = -np.matrix(rot_m).T * np.matrix(tvec)
        camera_position = [float(camera_position[0][0]), float(camera_position[1][0]), float(camera_position[2][0])]

        return camera_position, rvec, tvec

    def get_camera_position(self, image, fast=False):
        """Get the XYZ camera position given an image

        Args:
            img (np.array): Input image

        Returns:
            np.array: XYZ camera position
        """
        corners, objp, corner_image = self.get_checker_corners(image, fast)

        camera_position = None
        rvec = None
        tvec = None
        if corners is not None:
            camera_position, rvec, tvec = self.calc_cam_pos(corners, objp)

        return camera_position, rvec, tvec, corner_image

    # def plot_cam_positions(self):
    #     """Plot camera positions"""
    #     pcd_arr = np.array(self.camera_position_list)
    #     pcd = xyz_to_pcd(pcd_arr)

    def board_pose_demo(self, reader_obj):
        """Demo of checker/charuco board pose"""
        while True:
            image, _, _ = reader_obj.next_frame()
            board_pose, image = self.get_checker_pose(image)
            print("Checker Pose: ", board_pose)
            cv2.imshow("Checker Pose", image)
            k = cv2.waitKey(30)
            if k == 27:
                cv2.destroyAllWindows()
                break


def main(calib_settings, cam_name, calib_id="CALIB_0_0", realsense=False):
    """Calculate checker pose and camera position"""

    calib_path = f"data/{calib_id}/left_calib.json" if cam_name == "left" else f"data/{calib_id}/right_calib.json"
    checker_obj = PoseEstimate(calib_settings=calib_settings, calib_path=calib_path)

    if realsense:
        cam_obj = RealSenseReader()
    else:
        setting_path = "data/left_setting.json" if cam_name == "left" else "data/right_setting.json"
        cam_id = checker_obj.left_id if cam_name == "left" else checker_obj.right_id
        cam_obj = CameraReader(cam_index=cam_id, ui_flag=True, setting_path=setting_path)
        cap = cam_obj.get_cap()

    count = 0

    while True:
        if realsense:
            _, left_img, right_img = cam_obj.get_left_right()
            img = left_img if cam_name == "left" else right_img
        else:
            _, img = cap.read()

        if img is None:
            break

        img1 = img.copy()
        cam_pt, rvec, tvec, _ = checker_obj.get_camera_position(img)  # pylint: disable=W0612
        _, corner_img = checker_obj.get_checker_pose(img1)

        if cam_pt is not None:
            checker_obj.add_cam_pos(cam_pt)
            print(f"camera position x: {int(cam_pt[0])} y:{int(cam_pt[1])} z:{int(cam_pt[2])}")
            img = put_text(f"current X {int(cam_pt[0])} and Y {int(cam_pt[1])} and Z {int(cam_pt[2])}", corner_img, 50, 50, color=(255, 0, 0), thickness=3)
            count += 1

        cv2.namedWindow("Corners", cv2.WINDOW_GUI_NORMAL)
        cv2.imshow("Corners", img)
        k = cv2.waitKey(30)
        if k == 27:
            cv2.destroyAllWindows()
            break


class TestPoseEstimate(unittest.TestCase):
    """Pose estimate test"""

    def test_pose_estimate(self):
        """Pose estimation with sample images"""
        calib_settings = "calibration_settings.json"
        calib_id = "CALIB_0_0"
        calib_path = f"data/{calib_id}/left_calib.json"
        images_path = "data/depth_images/left"
        checker_obj = PoseEstimate(calib_settings=calib_settings, calib_path=calib_path)
        img_obj = FolderReader(folder_path=images_path)
        while True:
            img, _, _ = img_obj.next_frame()

            if img is None or isinstance(img, str):
                break

            cam_pt, rvec, tvec, _ = checker_obj.get_camera_position(img)  # pylint: disable=W0612
            assert cam_pt is not None and len(cam_pt) == 3, "Pose estimate test failed"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-cs", "--calib_settings", default="calibration_settings.json", help="path for calibration settings json")
    parser.add_argument("-id", "--cam_id", default=2, type=int, help="cam id/path for input video")
    parser.add_argument("-cn", "--cam_name", default="left", help="left or right camera")
    parser.add_argument("-rs", "--realsense", default=False, nargs="?", const=True, help="To record from realsense camera")
    parser.add_argument("-cid", "--calib_id", default="CALIB_0_0", help="camera calibration id for calibration params")

    parser = parser.parse_args()
    calib_settings_ = parser.calib_settings
    cam_name_ = parser.cam_name
    realsense_ = parser.realsense
    calib_id_ = parser.calib_id

    main(calib_settings_, cam_name_, calib_id_, realsense_)
