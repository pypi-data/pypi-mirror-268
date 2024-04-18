"""To calculate disparity and depth for stereo setup based on SGBM/BM method"""
import argparse
import os
import cv2
from ignutils.draw_utils import put_text
import numpy as np

from ignutils.cam_utils.camera_reader import CameraReader
from ignutils.cam_utils.realsense_reader import RealSenseReader
from ignutils.video_utils.folder_reader import FolderReader
from ignutils.calib_utils.angle_utils import euler_angles_to_rotation_matrix
from ignutils.json_utils import read_json


class DisparityCalc:
    """To calcualte SGBM and BM based disparity and depth"""

    def __init__(self, calib_settings="calibration_settings.json", frame_width=1920, frame_height=1080, calib_id="CALIB_0_0", optim_id="OPTIM_0_0", rs_id="RS_0_0", realsense=False):
        calib_settings = read_json(calib_settings)
        self.realsense = realsense
        self.left_id = calib_settings["left_id"]
        self.right_id = calib_settings["right_id"]
        self.img_width = frame_width
        self.img_height = frame_height
        self.calib_params_path = os.path.join("data", calib_id)
        self.optim_params_path = os.path.join("data", optim_id)
        self.rs_params_path = os.path.join("data", rs_id)
        self.left_img = None
        self.right_img = None
        self.stereo = cv2.StereoBM_create()
        self.load_calib()
        self.update_stereo_map()

    def load_calib(self):
        """Load mono and stereo calibration results"""
        if self.realsense:
            params_path = self.rs_params_path
        else:
            params_path = self.optim_params_path
        left_calib_path = os.path.join(params_path, "left_calib.json")
        right_calib_path = os.path.join(params_path, "right_calib.json")
        stereo_result_path = os.path.join(params_path, "stereo_result.json")
        disp_params_path = os.path.join(params_path, "disp_params.json")
        disp_roi_path = os.path.join(params_path, "disp_roi.json")
        if os.path.isfile(left_calib_path) and os.path.isfile(right_calib_path):
            print(f"Reading left calib json {left_calib_path}")
            print(f"Reading right calib json {right_calib_path}")
            left_calibration_result = read_json(left_calib_path)
            self.mtx_l = np.array(left_calibration_result["mtx"])
            self.dist_l = np.array(left_calibration_result["dist"])
            right_calibration_result = read_json(right_calib_path)
            self.mtx_r = np.array(right_calibration_result["mtx"])
            self.dist_r = np.array(right_calibration_result["dist"])
        else:
            raise FileNotFoundError("Left/Right calibration jsons are not available, please mono calibrate and try again")

        if os.path.isfile(stereo_result_path):
            print(f"Reading stereo result json {stereo_result_path}")
            stereo_calib_result = read_json(stereo_result_path)
            self.rot = np.array(stereo_calib_result["rot"])
            self.trans = np.array(stereo_calib_result["trans"])
            self.proj_l = np.array(stereo_calib_result["proj_l"])
            self.proj_r = np.array(stereo_calib_result["proj_r"])
            self.rot_angle = np.array(stereo_calib_result["rot_angle"])

        else:
            raise FileNotFoundError("Stereo calibration results are not available, please stereo calibrate and try again")

        if os.path.isfile(disp_params_path):
            print(f"Reading disparity result json {disp_params_path}")
            disparity_result = read_json(disp_params_path)
            self.num_disparities = int(disparity_result["num_disparities"])
            self.block_size = int(disparity_result["block_size"])
            self.min_disparity = disparity_result["min_disparity"]
            self.uniqueness_ratio = disparity_result["uniqueness_ratio"]
            self.pre_filter_type = disparity_result["pre_filter_type"]
            self.pre_filter_size = int(disparity_result["pre_filter_size"])
            self.pre_filter_cap = disparity_result["pre_filter_cap"]
            self.speckle_range = disparity_result["speckle_range"]
            self.speckle_window_size = int(disparity_result["speckle_window_size"])
            self.disp12_max_diff = disparity_result["disp12_max_diff"]
            self.texture_threshold = disparity_result["texture_threshold"]
            self.fi_bias = disparity_result["fi_bias"]
        else:
            print("Using default values for disparity")
            self.num_disparities = 10
            self.block_size = 43
            self.min_disparity = 11
            self.uniqueness_ratio = 0
            self.pre_filter_type = 0
            self.pre_filter_size = 19
            self.pre_filter_cap = 62
            self.speckle_range = 30
            self.speckle_window_size = 5
            self.disp12_max_diff = 19
            self.texture_threshold = 20
            self.fi_bias = 10

        if os.path.isfile(disp_roi_path):
            print(f"Reading disparity roi json {disp_roi_path}")
            roi_json = read_json(disp_roi_path)
            self.roi_list = roi_json["roi"]

    def rectify_image(self, left_img, right_img):
        """Rectify left and right images

        Args:
            left_img (np.ndarray): Input left image
            right_img (_type_): Input right image

        Returns:
            np.ndarray: left and right rectified images
        """
        self.update_stereo_map()
        left_img = left_img if left_img.ndim == 2 else cv2.cvtColor(left_img, cv2.COLOR_BGR2GRAY)
        right_img = right_img if right_img.ndim == 2 else cv2.cvtColor(right_img, cv2.COLOR_BGR2GRAY)
        rectified_left = cv2.remap(
            left_img,
            self.stereo_map_l_x,
            self.stereo_map_l_y,
            cv2.INTER_LANCZOS4,
            cv2.BORDER_CONSTANT,  # type: ignore
            0,
        )

        rectified_right = cv2.remap(
            right_img,
            self.stereo_map_r_x,
            self.stereo_map_r_y,
            cv2.INTER_LANCZOS4,
            cv2.BORDER_CONSTANT,  # type: ignore
            0,
        )

        return rectified_left, rectified_right

    def update_stereo_map(self):
        """Update stereo map values"""

        if self.rot_angle is not None and self.trans is not None:
            self.rot = euler_angles_to_rotation_matrix(self.rot_angle)
            rectify_scale = 1
            rect_l, rect_r, self.proj_l, self.proj_r, q, roi_l, roi_r = cv2.stereoRectify(self.mtx_l, self.dist_l, self.mtx_r, self.dist_r, (self.img_width, self.img_height), self.rot, self.trans, rectify_scale, (0, 0))  # pylint: disable=W0612
        else:
            raise Exception("Rotation and translation values are not available, please calibrate") # pylint: disble=W0719

        stereo_map_l = cv2.initUndistortRectifyMap(self.mtx_l, self.dist_l, rect_l, self.proj_l, (self.img_width, self.img_height), cv2.CV_16SC2)
        stereo_map_r = cv2.initUndistortRectifyMap(self.mtx_r, self.dist_r, rect_r, self.proj_r, (self.img_width, self.img_height), cv2.CV_16SC2)

        self.stereo_map_l_x = stereo_map_l[0]
        self.stereo_map_l_y = stereo_map_l[1]
        self.stereo_map_r_x = stereo_map_r[0]
        self.stereo_map_r_y = stereo_map_r[1]

        print("Rotation:  \n", self.rot)
        print("Translation:  \n", self.trans)
        print("Left matrix:  \n", self.mtx_l)
        print("Right matrix:  \n", self.mtx_r)

    def update_disp_params(self):
        """Update disparity parameters to stereo compute"""
        self.stereo.setNumDisparities(self.num_disparities)
        self.stereo.setBlockSize(self.block_size)
        self.stereo.setMinDisparity(self.min_disparity)
        self.stereo.setPreFilterType(self.pre_filter_type)
        self.stereo.setPreFilterSize(self.pre_filter_size)
        self.stereo.setPreFilterCap(self.pre_filter_cap)
        self.stereo.setUniquenessRatio(self.uniqueness_ratio)
        self.stereo.setTextureThreshold(self.texture_threshold)
        self.stereo.setSpeckleRange(self.speckle_range)
        self.stereo.setSpeckleWindowSize(self.speckle_window_size)
        self.stereo.setDisp12MaxDiff(self.disp12_max_diff)

    def get_disparity(self, rectified_left, rectified_right):
        """Create disparity map from left and right images"""
        self.update_disp_params()
        disparity = self.stereo.compute(rectified_left, rectified_right)
        disparity = disparity.astype(np.float32)
        disparity = disparity / 16.0
        disparity_norm = (disparity - self.min_disparity) / self.num_disparities

        return disparity, disparity_norm

    def depth_value(self, event, x, y, flags, param): # pylint: disable=W0613
        """mouse event to get depth value"""
        if event == cv2.EVENT_MOUSEMOVE:
            param["x1"] = x
            param["y1"] = y

    def find_bm_disparity(self, left_folder_path=None, right_folder_path=None):
        """Find optimal disparity parameters for the given stereo setup using bm method"""
        cam_obj = None
        cap_l = None
        cap_r = None
        if left_folder_path is not None and right_folder_path is not None:
            img_obj_l = FolderReader(folder_path=left_folder_path)
            img_obj_r = FolderReader(folder_path=right_folder_path)
            x1 = int(img_obj_l.frame_width / 2)
            y1 = int(img_obj_r.frame_height / 2)
            self.left_img, _, _ = img_obj_l.next_frame()
            self.right_img, _, _ = img_obj_r.next_frame()
        else:
            if self.realsense:
                cam_obj = RealSenseReader()
                x1 = int(cam_obj.cam_width / 2)
                y1 = int(cam_obj.cam_height / 2)
            else:
                cam_obj_l = CameraReader(cam_index=self.left_id, ui_flag=True, setting_path="data/left_setting.json")
                cam_obj_r = CameraReader(cam_index=self.right_id, ui_flag=True, setting_path="data/right_setting.json")
                cam_width = cam_obj_l.cam_width
                cam_height = cam_obj_l.cam_height
                cap_l = cam_obj_l.get_cap()
                cap_r = cam_obj_r.get_cap()
                x1 = 0
                y1 = 0
                if cam_width is not None and cam_height is not None:
                    x1 = int(cam_width / 2)
                    y1 = int(cam_height / 2)

        param = {"x1": x1, "y1": y1}
        cv2.namedWindow("Depth", cv2.WINDOW_GUI_NORMAL)
        cv2.namedWindow("disparity", cv2.WINDOW_GUI_NORMAL)
        cv2.setMouseCallback("Depth", self.depth_value, param)

        while True:
            left_img = None
            right_img = None
            if left_folder_path is None and right_folder_path is None:
                if self.realsense and cam_obj is not None:
                    _, left_img, right_img = cam_obj.get_left_right()
                else:
                    if cap_l is not None and cap_r is not None:
                        _, left_img = cap_l.read()
                        _, right_img = cap_r.read()

            if left_img is None or right_img is None:
                break

            left_rect, right_rect = self.rectify_image(left_img, right_img)
            disparity, disparity_norm = self.get_disparity(left_rect, right_rect)
            depth_map, depth_image = self.compute_depth_map(disparity)

            x1 = param["x1"]
            y1 = param["y1"]
            depth = depth_map[y1, x1]
            cv2.circle(depth_image, (x1, y1), 5, (255, 255, 255), -3)
            put_text(f"Depth: {depth}", depth_image, (20), (50), color=(255, 255, 255), thickness=3, font=cv2.QT_FONT_NORMAL, draw_bg=False)

            cv2.imshow("disparity", disparity_norm)
            cv2.imshow("Depth", depth_image)

            k = cv2.waitKey(10)

            if k == 27:
                break

        cv2.destroyAllWindows()

    def compute_depth_map(self, disp, focal_len=None, baseline=None):
        """Calculate depth map using disparity map, left camera matrix, and translation vectors"""
        if focal_len is None or baseline is not None:
            # decompose projection matrix to get intrinsic matrix, rotation matrix, and 3D translation vector
            k_left, _, t_left, _, _, _, _ = cv2.decomposeProjectionMatrix(self.proj_l)
            t_left = (t_left / t_left[3])[:3]

            _, _, t_right, _, _, _, _ = cv2.decomposeProjectionMatrix(self.proj_r)
            t_right = (t_right / t_right[3])[:3]

            # Get focal length of x axis for left camera
            focal_len = k_left[0][0]

            # Calculate baseline of stereo pair
            baseline = t_right[0] - t_left[0]

        # Avoid instability and division by zero
        disp[disp == 0.0] = 0.1
        disp[disp == -1.0] = 0.1

        # Make empty depth map then fill with depth
        depth_map = (focal_len * baseline) / disp
        depth_map = depth_map + self.fi_bias

        depth_norm = cv2.normalize(depth_map, None, 0, 255, cv2.NORM_MINMAX)  # type: ignore
        depth_image = np.array(depth_norm, dtype=np.uint8)
        depth_color = cv2.applyColorMap(depth_image, cv2.COLORMAP_JET)

        return depth_map, depth_color


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-cs", "--calib_settings", default="calibration_settings.json", help="path for calibration settings json")
    parser.add_argument("-nd", "--no_display", default=False, nargs="?", const=True, help="Dont show calibration image output")
    parser.add_argument("-rs", "--realsense", default=False, nargs="?", const=True, help="To record from realsense camera")
    parser.add_argument("-li", "--left_images", default=None, help="left input images")
    parser.add_argument("-ri", "--right_images", default=None, help="right input images")
    parser.add_argument("-fw", "--frame_width", default=1920, type=int, help="Frame width")
    parser.add_argument("-fh", "--frame_height", default=1080, type=int, help="Frame height")
    parser.add_argument("-cid", "--calib_id", default="CALIB_0_0", help="camera calibration id for calibration params")
    parser.add_argument("-oid", "--optim_id", default="OPTIM_0_0", help="camera optimization id for optimized params")
    parser.add_argument("-rid", "--rs_id", default="RS_0_0", help="Realsense camera id for calibrated params")

    parser = parser.parse_args()
    calib_settings_ = parser.calib_settings
    realsense_ = parser.realsense
    left_images_ = parser.left_images
    right_images_ = parser.right_images
    frame_width_ = parser.frame_width
    frame_height_ = parser.frame_height
    calib_id_ = parser.calib_id
    optim_id_ = parser.optim_id
    rs_id_ = parser.rs_id

    disp_obj = DisparityCalc(calib_settings_, frame_width_, frame_height_, calib_id_, optim_id_, rs_id_, realsense_)
    disp_obj.find_bm_disparity(left_images_, right_images_)
