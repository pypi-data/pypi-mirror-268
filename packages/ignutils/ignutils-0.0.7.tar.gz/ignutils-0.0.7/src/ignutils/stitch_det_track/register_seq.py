# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : ray_stitcher.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""To do sequential registration of given video pair."""

import glob
import os
import re
import time
from collections import deque

import cv2
import numpy as np

# from ignutils.registration.superglue.super_glue_match import SuperGlueReg
from ignutils.clone_utils import CloneRepo
from ignutils.registration.keypoint_register import KeypointRegister


class RegImageSeq1: # pylint: disable=too-few-public-methods
    """to register two consecutive images in a sequence"""

    def __init__(
        self,
        nfeatures=5000,
        crop_w=(-1, -1),
        crop_h=(-1, -1),
        reuse_prev_keypts=False,
        print_flag=True,
    ) -> None:
        """_summary_

        Args:
            nfeatures (int, optional): _description_, defaults to 5000
            crop_w (tuple, optional): _description_, defaults to (-1,
                -1)
            crop_h (tuple, optional): _description_, defaults to (-1,
                -1)
            reuse_prev_keypts (bool, optional): _description_, defaults
                to False
            print_flag (bool, optional): _description_, defaults to True
        """
        self.nfeatures = nfeatures
        self.crop_w = crop_w
        self.crop_h = crop_h
        self.reuse_prev_keypts = reuse_prev_keypts
        self.fixed_kp = None
        self.fixed_des = None
        self.print_flag = print_flag
        register_config_path = os.path.join(os.getcwd(), "keypoint_config.yaml")
        self.reg_obj = KeypointRegister(register_config_path)

    def reg_image_seq(self, fixed, moving):
        """Calculate the transformation matrix to register the 'moving' image with respect to the 'fixed' image"""
        fixed_ht, fixed_wd = fixed.shape[:2]
        moving_ht, moving_wd = moving.shape[:2]

        fixed_roi = (0, 0, fixed_wd // 2, fixed_ht)
        moving_roi = (moving_wd // 2, 0, moving_wd, moving_ht)

        if self.reuse_prev_keypts is False:  # make kp None if not to reuse
            self.fixed_kp, self.fixed_des = None, None

        moved, mat, self.fixed_kp, self.fixed_des = self.reg_obj.register(
            fixed,
            moving,
            nfeatures=self.nfeatures,
            fixed_des=self.fixed_des,
            fixed_roi=fixed_roi,
            moving_roi=moving_roi,
        )

        return moved, mat


class RegImageSeq:
    """A class to register a sequence of images"""

    def __init__(
        self,
        nfeatures=5000,
        reuse_prev_keypts=False,
        fixed_roi_frac=(-1, -1, -1, -1),
        moving_roi_frac=(-1, -1, -1, -1),
        reg_threshold=(-2, 300),
        window_len=30,
        print_flag=True,
    ) -> None:
        self.window_len = window_len
        self.nfeatures = nfeatures
        self.print_flag = print_flag
        self.reuse_prev_keypts = reuse_prev_keypts
        self.fixed_roi_frac = fixed_roi_frac
        self.moving_roi_frac = moving_roi_frac
        self.reg_threshold = reg_threshold
        self.init_reg_image_seq()
        register_config_path = os.path.join(os.getcwd(), "keypoint_config.yaml")
        self.reg_obj = KeypointRegister(register_config_path, show_flag=False, print_flag=False)

    def init_reg_image_seq(self):
        """Initialize the registration parameters."""
        self.fixed_kp = None
        self.fixed_des = None
        self.prev_y_shift = 0
        self.y_shift_q = deque(maxlen=self.window_len)
        self.y_shift_list = []
        self.frame_count = 0

    def reg_image_seq(self, fixed, moving):
        """Calculate 1D shift in Y direction between two consecutive images"""
        if self.fixed_roi_frac != (-1, -1, -1, -1):
            fixed_roi = (
                int(self.fixed_roi_frac[0] * fixed.shape[1]),
                int(self.fixed_roi_frac[1] * fixed.shape[0]),
                int(self.fixed_roi_frac[2] * fixed.shape[1]),
                int(self.fixed_roi_frac[3] * fixed.shape[0]),
            )
        else:
            fixed_roi = (-1, -1, -1, -1)

        if self.moving_roi_frac != (-1, -1, -1, -1):
            moving_roi = (
                int(self.moving_roi_frac[0] * moving.shape[1]),
                int(self.moving_roi_frac[1] * moving.shape[0]),
                int(self.moving_roi_frac[2] * moving.shape[1]),
                int(self.moving_roi_frac[3] * moving.shape[0]),
            )
        else:
            moving_roi = (-1, -1, -1, -1)

        if not self.reuse_prev_keypts:
            self.fixed_kp, self.fixed_des = None, None

        reg_iter_count = 3
        if self.frame_count > 1:
            reg_iter_count = 1

        for i in range(reg_iter_count):  # Loop for retrying registration if it fails
            if self.print_flag:
                print("\t", f"REG Try: {i+1}")
            _, mat, self.fixed_kp, self.fixed_des = self.reg_obj.register(
                fixed,
                moving,
                x_y_diff_based=False,
                nfeatures=int((i + 1) * self.nfeatures),
                fixed_kp=self.fixed_kp,
                fixed_des=self.fixed_des,
                fixed_roi=fixed_roi,
                moving_roi=moving_roi,
                prev_y_shift=None,
            )
            if self.frame_count == 0:  # Ignore very first frame
                y_shift = self.prev_y_shift

            else:
                if not isinstance(mat, np.ndarray):
                    y_shift = self.prev_y_shift
                else:
                    y_shift = int(mat[1][2])

                    if self.reg_threshold is not None:
                        l_thr, u_thr = self.reg_threshold
                        if l_thr < y_shift < u_thr:  # Lower & Upper thresholds for Registration
                            self.y_shift_q.append(y_shift)
                            break  # Registration Successful
                    else:
                        if self.print_flag:
                            print(
                                "\t",
                                f"REG Try: {i+1} Failed \n y_shiftQ: ",
                                self.y_shift_q,
                            )

        if len(self.y_shift_q):
            if 1:  # Median method
                y_shift = int(np.median(self.y_shift_q))
            if 0:  # TO-DO line fit method
                x = np.arange(len(self.y_shift_q))
                y = np.array(self.y_shift_q)
                z = np.polyfit(x, y, 3)
                p = np.poly1d(z)
                y_shift = int(p[len(self.y_shift_q) - 1])

        self.prev_y_shift = y_shift
        if self.print_flag:
            print("**Medianyshift", y_shift)
            print("y Que: ", self.y_shift_q)
        self.frame_count += 1
        return y_shift


if __name__ == "__main__":
    CloneRepo("https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db_dummy", "AQM_stitch_mini", "DB", access_token_name="DB_CLONE_TOKEN")

    image_files = sorted(glob.glob("DB/Set0/*jpg"), key=lambda f: int(re.sub("\D", "", f)))
    assert len(image_files) >= 2, f"Only {len(image_files)} images found"
    img_list = []
    for i in range(len(image_files)):
        img_list.append(cv2.imread(image_files[i]))

    reg_obj = RegImageSeq()
    t1 = time.time()
    img1 = img_list[0]
    for i in range(1, len(img_list)):
        img2 = img_list[i]
        _ = reg_obj.reg_image_seq(img1, img2)
        img1 = img2
    t2 = time.time()
    seq_fps = len(img_list) / (t2 - t1)
    print(f"Sequential FPS = {seq_fps:.3f}")
    assert seq_fps > 0.5, f"Low fps:{seq_fps:.3f}"
