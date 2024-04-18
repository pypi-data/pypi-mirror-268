"""To calculate depth of a checkerboard corner based on Triangulation"""
import os
import argparse
import unittest
import cv2
import numpy as np
from scipy import linalg

from ignutils.cam_utils.camera_reader import CameraReader
from ignutils.cam_utils.realsense_reader import RealSenseReader
from ignutils.json_utils import read_json
from ignutils.video_utils.folder_reader import FolderReader


def get_imagepoints(left_image, right_image, rows=6, cols=9):
    """Generate object and image points for pair of left and right images

    Args:
        left_image (np.ndarray): Input left image
        right_image (np.ndarray): Input right image

    Returns:
        np.ndarray: object and image points of left and right images
    """
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    gray_l = left_image if left_image.ndim == 2 else cv2.cvtColor(left_image, cv2.COLOR_BGR2GRAY)
    gray_r = right_image if right_image.ndim == 2 else cv2.cvtColor(right_image, cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret_l, corners_l = cv2.findChessboardCorners(gray_l, (rows, cols), None)
    ret_r, corners_r = cv2.findChessboardCorners(gray_r, (rows, cols), None)

    # If found, add object points, image points (after refining them)
    if ret_l is True and ret_r is True:
        corners_l = cv2.cornerSubPix(gray_l, corners_l, (11, 11), (-1, -1), criteria)
        corners_r = cv2.cornerSubPix(gray_r, corners_r, (11, 11), (-1, -1), criteria)
        imgpoints_l = corners_l
        imgpoints_r = corners_r
    else:
        # objpoints = None
        imgpoints_l = None
        imgpoints_r = None
        print("Checker board not detected")

    return imgpoints_l, imgpoints_r


def triangulate(p1, p2, point1, point2, custom=True):
    """Traingulate image points to get depth

    Args:
        P1 (np.ndarray): left projection matrix
        P2 (np.ndarray): right projection matrix
        point1 (np.ndarray): left image point
        point2 (np.ndarray): right image point

    Returns:
        _type_: _description_
    """
    if custom is True:
        a_mat = [point1[1] * p1[2, :] - p1[1, :], p1[0, :] - point1[0] * p1[2, :], point2[1] * p2[2, :] - p2[1, :], p2[0, :] - point2[0] * p2[2, :]]
        a_mat = np.array(a_mat).reshape((4, 4))
        b_mat = a_mat.transpose() @ a_mat

        _, _, tri_point = linalg.svd(b_mat, full_matrices=False)
        print("Triangulated point: ")
        print(tri_point[3, 0:3] / tri_point[3, 3])
        return tri_point[3, 0:3] / tri_point[3, 3]

    points4d = cv2.triangulatePoints(p1, p2, point1, point2)
    points3d = (points4d[:3, :] / points4d[3, :]).T
    print("3D points: ", points3d)

    return points3d

def load_settings(calib_settings, calib_id):
    """Load result jsons and get projection matrices"""
    settings = read_json(calib_settings)
    left_id = settings["left_id"]
    right_id = settings["right_id"]
    rows = settings["rows"]
    cols = settings["cols"]
    calib_params_path = os.path.join("data", calib_id)
    print(f"Reading results from {calib_params_path}")
    stereo_result = read_json(os.path.join(calib_params_path, "stereo_result.json"))
    left_calib = read_json(os.path.join(calib_params_path, "left_calib.json"))
    right_calib = read_json(os.path.join(calib_params_path, "right_calib.json"))
    stereo_rot = np.array(stereo_result["rot"])
    stereo_trans = np.array(stereo_result["trans"])
    mtx_l = np.array(left_calib["mtx"])
    mtx_r = np.array(right_calib["mtx"])

    # projection matrix for C1
    rot_l = np.concatenate([np.eye(3), [[0], [0], [0]]], axis=-1)
    proj_l = mtx_l @ rot_l

    # RT matrix for C2 is the R and T obtained from stereo calibration.
    rot_r = np.concatenate([stereo_rot, stereo_trans], axis=-1)
    proj_r = mtx_r @ rot_r  # projection matrix for C2

    return left_id, right_id, rows, cols, proj_l, proj_r

def point_depth_live(calib_settings, calib_id="CALIB_0_0", realsense=False):
    """Find checker point depth live"""

    left_id, right_id, rows, cols, proj_l, proj_r = load_settings(calib_settings, calib_id)
    cam_obj, img_r, img_l, cap_l, cap_r = None, None, None, None, None
    if realsense:
        cam_obj = RealSenseReader()
    else:
        cam_obj_l = CameraReader(cam_index=left_id, ui_flag=True, setting_path="data/left_setting.json")
        cam_obj_r = CameraReader(cam_index=right_id, ui_flag=True, setting_path="data/right_setting.json")
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

        imgp_l, imgp_r = get_imagepoints(img_l, img_r, rows=rows, cols=cols)
        if imgp_l is not None and imgp_r is not None:
            # getting the origin point from both images
            imgp_l = imgp_l[0]
            imgp_r = imgp_r[0]

            # drawing the point
            img_l = cv2.circle(img_l, (int(imgp_l[0][0]), int(imgp_l[0][1])), 10, (0, 255, 0), -3)
            img_r = cv2.circle(img_r, (int(imgp_r[0][0]), int(imgp_r[0][1])), 10, (0, 255, 0), -3)
            _p3d = triangulate(proj_l, proj_r, imgp_l[0], imgp_r[0], custom=True)  # custom flag as false to use cv2.traingulatepoints

        cv2.namedWindow("left", cv2.WINDOW_GUI_NORMAL)
        cv2.namedWindow("right", cv2.WINDOW_GUI_NORMAL)
        cv2.imshow("left", img_l)
        cv2.imshow("right", img_r)
        k = cv2.waitKey(30)
        if k == 27:
            cv2.destroyAllWindows()
            break

class TestPointDepth(unittest.TestCase):
    """Point depth calculation test"""

    def test_point_depth(self):
        """Test point depth using checkerboard sample images"""
        calib_settings = "calibration_settings.json"
        calib_id = "CALIB_0_0"
        left_images_path = "data/depth_images/left"
        right_images_path = "data/depth_images/right"
        _, _, rows, cols, proj_l, proj_r = load_settings(calib_settings, calib_id)
        img_obj_l = FolderReader(folder_path=left_images_path)
        img_obj_r = FolderReader(folder_path=right_images_path)
        while True:
            img_l, _, _ = img_obj_l.next_frame()
            img_r, _, _ = img_obj_r.next_frame()
            if img_l is None or img_r is None or isinstance(img_l, str) or isinstance(img_r, str):
                break
            imgp_l, imgp_r = get_imagepoints(img_l, img_r, rows=rows, cols=cols)
            if imgp_l is not None and imgp_r is not None:
                # getting the origin point from both images
                imgp_l = imgp_l[0]
                imgp_r = imgp_r[0]
                _p3d = triangulate(proj_l, proj_r, imgp_l[0], imgp_r[0], custom=True)
                assert int(_p3d[2]) < 550, "Point depth test failed"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-li", "--left_images", default=None, help="left input images")
    parser.add_argument("-ri", "--right_images", default=None, help="right input images")
    parser.add_argument("-rs", "--realsense", default=False, nargs="?", const=True, help="To record from realsense camera")
    parser.add_argument("-cs", "--calib_settings", default="calibration_settings.json", help="path for calibration settings json")
    parser.add_argument("-cid", "--calib_id", default="CALIB_0_0", help="camera calibration id for calibration params")

    parser = parser.parse_args()
    calib_settings_ = parser.calib_settings
    left_images_ = parser.left_images
    right_images_ = parser.right_images
    realsense_ = parser.realsense
    calib_id_ = parser.calib_id

    point_depth_live(calib_settings_, calib_id_, realsense_)
