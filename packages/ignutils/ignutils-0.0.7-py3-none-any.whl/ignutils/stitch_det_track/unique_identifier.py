# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : unique_identifier.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""To get unique frames based on y_shift."""

import logging

import numpy as np


class UniqueIdentifier:
    """Class to get unique frames based on y_shift."""

    def __init__(self, threshold: int) -> None:
        """Create object for getting unique images.

        Args:
            threshold (int): Threshold for calculating unique shifts.
        """
        self.threshold = threshold
        self.sum_y_shift = 0
        self.uniq_sum_y_shift = 0
        self.first_frame_flag = True

    def check_unique(self, sum_y_shift: int) -> bool:
        """To calcualte whether image is unique or not based on y_shift.

        Args:
            sum_y_shift (int): y-shift of image

        Returns:
            bool: True/False based on whether y-shift exceeds threshold
            (cumulative from previous image).
        """
        unique_flag = False
        if self.first_frame_flag:
            unique_flag = True
            self.first_frame_flag = False
            self.uniq_sum_y_shift = sum_y_shift

        elif abs(sum_y_shift - self.uniq_sum_y_shift) > self.threshold:
            self.uniq_sum_y_shift = sum_y_shift
            unique_flag = True

        return unique_flag

    def check_unique_list(self, sum_y_shift_list: list) -> list:
        """takes in a list of y_shift values, calculates the unique y_shift values, and returns a list of indexes corresponding to the unique values"""
        self.uniq_sum_y_shift = sum_y_shift_list[0]
        uniq_list = [True] + [self.check_unique(sum_y_shift) for sum_y_shift in sum_y_shift_list[1:]]
        uniq_idx = np.where(uniq_list)[0]
        logging.info("Unique y_shift indexes are %s", uniq_idx)
        return uniq_idx


if __name__ == "__main__":
    uniq_obj = UniqueIdentifier(600)
    sum_y_shifts = [0, 601, 999, 1596, 2192, 2762, 3281, 3865, 4501, 5153, 5764, 6378]

    uniq_obj = UniqueIdentifier(600)
    res = uniq_obj.check_unique_list(sum_y_shifts)
    assert res.tolist() == [
        0,
        1,
        3,
        5,
        7,
        8,
        9,
        10,
        11,
    ], f"Result mismatch. Result obtained is {res}"
