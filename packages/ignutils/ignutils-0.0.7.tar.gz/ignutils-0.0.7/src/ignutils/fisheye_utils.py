# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : gui_calib.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""To generate the calibration of video pairs using gui interface."""

from __future__ import division, print_function
import os
import os.path as osp
from copy import deepcopy

import cv2
import numpy as np
from ignutils.json_utils import read_json
from ignutils.transform_utils import transform_crop

CWD = os.getcwd()
np.set_printoptions(suppress=True)


class FisheyeCrop:
    """FishEye class for inference alone"""

    def __init__(
        self,
        calib_path,
        roi_path=None,
        print_flag=True,
        frame_width=None,
        frame_height=None,
        calib_mode=False,
    ):
        self.calib_path = calib_path
        self.roi_path = roi_path
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.print_flag = print_flag
        self.calib_mode = calib_mode
        self.moved_mtx = None
        self.moved_dist = None
        self.mapx = None
        self.mapy = None
        self.mapx_crop = None
        self.mapy_crop = None
        self.undistorted_roi = None
        self.load_params()

    def load_params(self):
        """load mtx, dist, roi"""
        if osp.isfile(self.calib_path):  # Looking inside data folder
            calib_json = read_json(self.calib_path)
            mtx = np.array(calib_json["mtx"])
            dist = np.array(calib_json["dist"])
        else:
            mtx = np.array([[2138.0, 0.0, 1916.0], [0.0, 2148.0, 999.0], [0.0, 0.0, 1.0]])
            dist = np.array([[-0.01, 0.023, 0.063, -0.00093, -0.035]])

        if self.print_flag:
            print("initial mtx", mtx)
            print("initial dist", dist)

        if self.roi_path is not None and os.path.isfile(osp.join(self.roi_path, "roi.txt")):
            roi = np.loadtxt(osp.join(self.roi_path, "roi.txt"), dtype=float)
        else:
            roi = None

        if roi is not None:
            roi = roi.tolist()

        if self.frame_width is not None and self.frame_height is not None:
            mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, mtx, (self.frame_width, self.frame_height), 5)
        else:
            mapx = None
            mapy = None

        self.initial_roi = roi
        self.undistorted_roi = roi
        self.moved_mtx = mtx
        self.moved_dist = dist
        self.mapx = mapx
        self.mapy = mapy
        self.mtx_org = deepcopy(mtx)
        self.dist_org = deepcopy(dist)
        self.validate_roi(self.undistorted_roi)

    def validate_roi(self, roi):
        """Validate roi and adjust ROI in case its more than image resolution"""
        if self.frame_width is not None and self.frame_height is not None:
            for pts in roi:
                if pts[0] > self.frame_width or pts[0] < 0 or pts[1] > self.frame_height or pts[1] < 0:
                    if self.calib_mode is False:
                        raise Exception("[!] Reloaded ROIs width or height more than frame size. Please do calibration") # pylint: disable=W0719
                    new_roi = np.array([[self.frame_width * 0.4, self.frame_height * 0.4], [self.frame_width * 0.6, self.frame_height * 0.4], [self.frame_width * 0.6, self.frame_height * 0.8], [self.frame_width * 0.4, self.frame_height * 0.8]])
                    roi = new_roi
                    print("Adjusted ROI for a different image resolution: ", roi)
                    break
        return roi

    def reload_params(self):
        """reload the params"""
        self.load_params()

    def save_roi(self, file_name="roi.txt"):
        """Save roi txt in the workspace directory"""
        if self.undistorted_roi is not None and len(self.undistorted_roi) == 4:
            print("ROI Updated: ", self.undistorted_roi)
            print(f"Saving roi to {self.roi_path}")
            np.savetxt(osp.join(self.roi_path, file_name), self.undistorted_roi, fmt="%f")

    def set_undistorted_roi(self, roi_pts):
        """Set default undistorted ROI"""
        if len(roi_pts) >= 2:
            self.undistorted_roi = np.array(roi_pts)

    def get_undistorted_roi(self):
        """Get undistorted ROI"""
        return self.undistorted_roi

    def get_distorted_roi(self):
        """Get distorted ROI"""
        roi = []
        distorted_roi = None
        if self.undistorted_roi is not None:
            for p in self.undistorted_roi:
                roi.append(self.get_distorted_pts(p))

        if len(roi) >= 2:
            distorted_roi = np.array(roi)

        return distorted_roi

    def get_undistorted_img(self, img, mtx=None, dist=None, new_mtx=None, optim=False):
        """Apply undistortion using loaded mtx and dist"""
        if mtx is None:
            mtx = self.moved_mtx
        if dist is None:
            dist = self.moved_dist
        # if new_mtx is None:
        #     new_mtx=mtx

        if optim or (self.mapx is None and self.mapy is None and mtx is not None and dist is not None):
            mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, new_mtx, (img.shape[1], img.shape[0]), 5)
            self.mapx = mapx
            self.mapy = mapy

        dst = cv2.remap(img, self.mapx, self.mapy, cv2.INTER_LINEAR)
        return dst

    def get_undistorted_pts(self, pts, mtx=None, dist=None):
        """Apply undistortion on point list"""
        if mtx is None:
            mtx = self.moved_mtx
        if dist is None:
            dist = self.moved_dist
        if not isinstance(pts, np.ndarray):
            pts = np.array(pts)
        pts = cv2.undistortPoints(np.expand_dims(pts, axis=1), mtx, dist, None, mtx)  # type: ignore
        pts = np.squeeze(pts, axis=1)
        return pts

    def get_distorted_pts(self, point):
        """Distort back the undistorted points"""
        y, x = point
        distorted_point_x, distorted_point_y = None, None
        if self.mapx is not None and self.mapy is not None:
            distorted_point_x = float(self.mapx[int(x), int(y)])
            distorted_point_y = float(self.mapy[int(x), int(y)])

        return (distorted_point_x, distorted_point_y)

    def get_distorted_lines(self, lines):
        """Distort back undistorted lines"""
        new_lines = []
        for line in lines:
            new_lines.append(self.get_distorted_pts(line))
        return new_lines

    def get_undistorted_lines(self, lines):
        """Get undistorted lines"""
        new_lines = []
        for line in lines:
            new_lines.append(self.get_undistorted_pts(line))
        return new_lines

    def get_mapx_mapy(self, img):
        """Get mapx mapy based on mtx and distortion"""
        mapx, mapy = cv2.initUndistortRectifyMap(
            self.moved_mtx,
            self.moved_dist,
            None,
            self.moved_mtx,
            (img.shape[1], img.shape[0]),
            5,
        )
        return mapx, mapy

    def get_undistorted_crop(self, img, h1=None, w1=None, pad_l=0, pad_r=0, pad_t=0, pad_b=0, caliberate=False, sync_roi_flag=False, dynamic_blend=False):
        """Cropping image based on undistorted ROI"""
        trans_mat = None
        if self.mapx is None or self.mapy is None or caliberate:
            self.mapx, self.mapy = self.get_mapx_mapy(img)

        if self.mapx_crop is None or self.mapy_crop is None or caliberate or sync_roi_flag or dynamic_blend:
            self.mapx_crop, _, _, trans_mat = transform_crop(image=self.mapx, crop_cntr=self.undistorted_roi, h1=h1, w1=w1, pad_l=pad_l, pad_r=pad_r, pad_t=pad_t, pad_b=pad_b, interpolation=cv2.INTER_NEAREST)
            self.mapy_crop, _, _, trans_mat = transform_crop(
                image=self.mapy,
                crop_cntr=self.undistorted_roi,
                h1=h1,
                w1=w1,
                pad_l=pad_l,
                pad_r=pad_r,
                pad_t=pad_t,
                pad_b=pad_b,
                interpolation=cv2.INTER_NEAREST,
            )
        crop = cv2.remap(img, self.mapx_crop, self.mapy_crop, cv2.INTER_LINEAR)

        return crop, trans_mat
