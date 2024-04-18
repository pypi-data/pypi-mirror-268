# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : stitch.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""To do stiching operations of left and right camera streams."""

import cv2
import numpy as np

from ignutils.stitch_det_track.register_seq import RegImageSeq


def pad_image_(img: np.ndarray, pad: int, mode: str) -> np.ndarray:
    """Pad img either in the top or bottom depending on mode.

    Args:
        img (np.ndarray): Input image to be padded
        pad (int): Amount of padding to be added
        mode (str): Padding mode. Either 'pad_up' or 'pad_down'
    """

    if mode == "pad_down":
        padded = cv2.copyMakeBorder(img, 0, pad, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))
    elif mode == "pad_up":
        padded = cv2.copyMakeBorder(img, pad, 0, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))
    return padded


class StitchRetainCanvas:
    """intended to stitch together multiple images and keep a track of the canvas height with each iteration"""

    def __init__(
        self,
        nfeatures=5000,
        canvas_flag=False,
        roi_frac=(-1, -1, -1, -1),
        reuse_prev_keypts=False,
        window_len=30,
        reg_threshold=None,
        print_flag=True,
    ) -> None:
        """Initializes an instance of the class

        Args:
            nfeatures (int, optional): _description_, defaults to 5000
            canvas_flag (bool, optional): _description_, defaults to
                False
            roi_frac (tuple, optional): _description_, defaults to (-1,
                -1, -1, -1)
            reuse_prev_keypts (bool, optional): _description_, defaults
                to False
            window_len (int, optional): _description_, defaults to 30
            reg_threshold (list, optional): _description_, defaults to
                [-2, 300]
            print_flag (bool, optional): _description_, defaults to True
        """
        if reg_threshold is None:
            reg_threshold = [-2, 300]

        self.canvas_flag = canvas_flag
        self.print_flag = print_flag

        self.register = RegImageSeq(
            nfeatures=nfeatures,
            fixed_roi_frac=roi_frac,
            moving_roi_frac=roi_frac,
            reuse_prev_keypts=reuse_prev_keypts,
            reg_threshold=reg_threshold,
            window_len=window_len,
            print_flag=print_flag,
        )

        self.init_stitch_vars()

    def init_stitch_vars(self):
        """Initializes variables used in the stitching process"""
        self.canvas = None
        self.prev_frame = None
        self.sum_y_shift = 0
        self.origin_y_shift = 0
        self.sum_y_shift_list = []
        self.canvas_ht = 0
        self.register.init_reg_image_seq()

    def stitch(self, img, y_shift_q=None):
        """
        stitches a new image `img` onto the current canvas, updating the class attributes `prev_frame`, `canvas_ht`, and `canvas`.
         The `y_shift_q` parameter specifies the shift amount in the y direction,
         or if None, the shift amount is computed using the `reg_image_seq` function from the `register` attribute
        """
        if self.canvas is None:
            self.prev_frame = img
            self.canvas_ht = img.shape[0]

        if self.canvas_flag and self.canvas is None:
            self.canvas = img

        if y_shift_q is not None:
            y_shift = y_shift_q
        else:
            y_shift = self.register.reg_image_seq(self.prev_frame, img)
        # logging.info(f"y-shift obtained is {y_shift}")

        self.sum_y_shift += y_shift
        self.sum_y_shift_list.append(self.sum_y_shift)

        if self.sum_y_shift > 0:
            pad = self.sum_y_shift + img.shape[0] + self.origin_y_shift - self.canvas_ht
            if pad > 0 and self.canvas_flag:  # Only pad when img exceeds canvas height
                self.canvas = pad_image_(self.canvas, pad, "pad_down")

            top = self.sum_y_shift + self.origin_y_shift

            if self.canvas_flag:
                self.canvas[top : top + img.shape[0], :, :] = img
        else:
            pad = abs(self.sum_y_shift) - self.origin_y_shift
            if pad > 0 and self.canvas_flag:  # Only pad when img exceeds canvas height
                self.canvas = pad_image_(self.canvas, pad, "pad_up")
            if abs(self.sum_y_shift) > self.origin_y_shift:
                self.origin_y_shift = abs(self.sum_y_shift)

            top = abs(abs(self.sum_y_shift) - self.origin_y_shift)

            if self.canvas_flag:
                self.canvas[top : top + img.shape[0], :, :] = img

        self.canvas_ht += pad

        self.sum_y_shift_list = [sum_y_shift + self.origin_y_shift for sum_y_shift in self.sum_y_shift_list]
        # logging.info(f"sum_y_shift_list = {self.sum_y_shift_list}")

        self.prev_frame = img

        return y_shift, self.sum_y_shift, self.canvas
