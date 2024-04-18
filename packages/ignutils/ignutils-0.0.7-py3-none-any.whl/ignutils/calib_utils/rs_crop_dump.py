"""Class to get realsense crop by matching with custom crop"""
from copy import deepcopy
import os
import cv2
import numpy as np

from ignutils.draw_utils import put_texts
from ignutils.mouse_utils import MousePts
from ignutils.show_utils import show, fuse
from ignutils.json_utils import read_json, write_json


class RoiAdjust(MousePts):
    """ROI adjust based cropping for depth optimsation"""

    def __init__(self, custom_grey_img, custom_disp_norm, custom_depth_norm, rs_grey_img, rs_disp_norm, rs_depth_norm, rs_disp, rs_depth, optim_id="OPTIM_0_0", rs_id="RS_0_0"):
        self.window_name = "Roi Adjust"
        self.rs_grey_img = rs_grey_img
        self.rs_disp_norm = rs_disp_norm
        self.rs_depth_norm = rs_depth_norm
        self.rs_disp = rs_disp
        self.rs_depth = rs_depth
        self.optim_id = optim_id
        self.rs_id = rs_id
        self.custom_roi_path = os.path.join("data", self.optim_id, "custom_roi.json")
        self.rs_roi_path = os.path.join("data", self.rs_id, "rs_roi.json")
        MousePts.__init__(self, img=self.rs_grey_img, windowname=self.window_name)
        if os.path.isfile(self.custom_roi_path) and os.path.isfile(self.rs_roi_path):
            custom_roi = read_json(self.custom_roi_path)
            rs_roi = read_json(self.rs_roi_path)
            self.custom_roi = custom_roi["custom_roi"]
            self.rs_roi = rs_roi["rs_roi"]
        else:
            self.custom_roi = self.select_rect(custom_disp_norm)
            self.rs_roi = [[self.sz, self.sz], [200, self.sz], [200, 200], [self.sz, 200]]
        if self.custom_roi is not None:
            x1, y1 = self.custom_roi[0]
            x2, y2 = self.custom_roi[2]
            self.custom_grey_img = custom_grey_img[y1:y2, x1:x2]
            self.custom_disp_norm = custom_disp_norm[y1:y2, x1:x2]
            self.custom_depth_norm = custom_depth_norm[y1:y2, x1:x2]
        self.crop_height, self.crop_width = self.custom_grey_img.shape[:2]
        self.roi_old = deepcopy(self.rs_roi)
        self.seam_position = self.crop_width // 2

    def get_crop(self):
        """Get the crop images of grey and disparity images

        Returns:
            np.ndarray: crop images
        """
        x1, y1 = self.rs_roi[0]
        x2, y2 = self.rs_roi[2]
        rs_grey_crop = cv2.resize(self.rs_grey_img[y1:y2, x1:x2], (self.crop_width, self.crop_height), interpolation=cv2.INTER_AREA)
        rs_disp_crop_norm = cv2.resize(self.rs_disp_norm[y1:y2, x1:x2], (self.crop_width, self.crop_height), interpolation=cv2.INTER_AREA)
        rs_depth_crop_norm = cv2.resize(self.rs_depth_norm[y1:y2, x1:x2], (self.crop_width, self.crop_height), interpolation=cv2.INTER_AREA)
        rs_disp_crop = cv2.resize(self.rs_disp[y1:y2, x1:x2], (self.crop_width, self.crop_height), interpolation=cv2.INTER_AREA)
        rs_depth_crop = cv2.resize(self.rs_depth[y1:y2, x1:x2], (self.crop_width, self.crop_height), interpolation=cv2.INTER_AREA)

        return rs_grey_crop, rs_disp_crop_norm, rs_depth_crop_norm, rs_disp_crop, rs_depth_crop

    def adjust_roi(self, color=(255, 0, 0)):
        """select points in image and returns roi

        Args:
            color (tuple): Color of ROI, defaults to (255, 0, 0)

        Returns:
            NumpyArray: ROI points information
        """
        self.color = color

        custom_grey = self.custom_grey_img
        custom_disp = self.custom_disp_norm
        custom_depth = self.custom_depth_norm
        rs_grey = self.rs_grey_img
        rs_disp = self.rs_disp_norm
        rs_depth = self.rs_depth_norm

        self.h, self.w = rs_disp.shape[:2]
        mindim = min(self.h, self.w)
        self.sz = mindim // 100
        self.thick = max(1, mindim // 600)
        self.roi_type = "rect"

        txt = [
            "Adjust all the four blue color corner points such that blended image is matching",
            "Press Esc to save & Exit window",
        ]

        rs_disp_copy = rs_disp.copy()
        h, w = rs_disp_copy.shape[:2]
        thickness = max(1, int(h / 400))
        put_texts(
            rs_disp_copy,
            test_tuple_list=txt,
            txt_thickness=thickness,
            v_space=80,
            txt_color=(0, 255, 0),
            default_align=None,
            offsetval=0,
            font=cv2.FONT_HERSHEY_COMPLEX,
        )
        self.h, self.w = rs_disp.shape[:2]
        mindim = min(self.h, self.w)
        self.sz = mindim // 100
        self.thick = max(1, mindim // 600)

        cv2.namedWindow(self.windowname, cv2.WINDOW_GUI_NORMAL)
        cv2.resizeWindow(self.windowname, 900, 900)
        cv2.moveWindow(self.windowname, 100, 100)
        cv2.setMouseCallback(self.windowname, self.mouse_callback)

        cv2.namedWindow("Grey Fused", cv2.WINDOW_GUI_NORMAL)
        cv2.moveWindow("Grey Fused", 1000, 500)
        cv2.namedWindow("Depth Fused", cv2.WINDOW_GUI_NORMAL)
        cv2.moveWindow("Depth Fused", 1000, 900)

        self.contrs = [self.rs_roi]
        self.contr_indx = len(self.contrs)

        k = -1
        roi_old = None

        while True:
            img = rs_disp_copy.copy()
            self.pts = self.contrs
            pts = np.array(self.pts, np.int32)
            if len(pts) > 0:
                cv2.polylines(img, [pts], True, (255, 255, 255), 2)

            for _, pt in enumerate(self.contrs[0]): # type: ignore
                start = (int(pt[0] - self.sz), int(pt[1] - self.sz))
                end = (int(pt[0] + self.sz), int(pt[1] + self.sz))
                rect_color = self.color
                cv2.rectangle(img, start, end, rect_color, thickness=self.thick)

            self.rs_roi = self.contrs[0]
            if roi_old != self.rs_roi:
                rs_grey_crop, rs_disp_crop_norm, rs_depth_crop_norm, rs_disp_crop, rs_depth_crop = self.get_crop()

                grey_fuz = fuse(rs_grey_crop, custom_grey)
                depth_fuz = fuse(rs_disp_crop_norm, custom_disp)

                k = show(img, win=self.windowname, time=30, k=k, window_normal=False)
                k = show(grey_fuz, win="Grey Fused", time=30, k=k, window_normal=False)
                k = show(depth_fuz, win="Depth Fused", time=30, k=k, window_normal=False)

            if k == 27:
                cv2.destroyWindow(self.windowname)
                cv2.destroyWindow("Grey Fused")
                cv2.destroyWindow("Depth Fused")

                if self.roi_old != self.rs_roi or k == ord("s"):
                    custom_roi = {"custom_roi": self.custom_roi}
                    rs_roi = {"rs_roi": self.rs_roi}
                    write_json(self.custom_roi_path, custom_roi)
                    write_json(self.rs_roi_path, rs_roi)
                break

            k = -1

        return self.rs_roi, self.custom_roi


if __name__ == "__main__":
    # Loading custom, realsense grey, disparity and depth images
    custom_grey_img_ = cv2.imread("data/OPTIM_0_0/rectified_left.png")
    custom_disp_norm_ = cv2.imread("data/OPTIM_0_0/disparity.png")
    custom_depth_norm_ = cv2.imread("data/OPTIM_0_0/depth.png")

    rs_grey_img_ = cv2.imread("data/RS_0_0/rectified_left.png")
    rs_disp_norm_ = cv2.imread("data/RS_0_0/disparity.png")
    rs_depth_norm_ = cv2.imread("data/RS_0_0/depth.png")

    # Loading realsense disparity and depth numpy files for cropping
    rs_disp_ = np.load("data/RS_0_0/disparity.npz")
    rs_disp_ = rs_disp_["disp"]
    rs_depth_ = np.load("data/RS_0_0/depth.npz")
    rs_depth_ = rs_depth_["depth"]

    OPTIM_ID_ = "OPTIM_0_0"
    RS_ID_ = "RS_0_0"

    roi_obj = RoiAdjust(custom_grey_img_, custom_disp_norm_, custom_depth_norm_, rs_grey_img_, rs_disp_norm_, rs_depth_norm_, rs_disp_, rs_depth_, OPTIM_ID_, RS_ID_)
    roi_obj.adjust_roi()
