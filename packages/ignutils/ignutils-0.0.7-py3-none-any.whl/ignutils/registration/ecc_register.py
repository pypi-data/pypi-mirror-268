"""Class for ECC transform based registration"""
import os
import unittest
import cv2
import numpy as np

from ignutils.registration.register_abstract import RegisterAbstract
from ignutils.show_utils import fuse


class EccRegister(RegisterAbstract):
    """ECC transform based registration"""

    def __init__(
        self,
        config_path,
        show_flag=False,
        print_flag=False,
    ):
        super().__init__(config_path, show_flag, print_flag)
        self.motion_type = self.config("motion_type")
        number_of_iters = self.config("number_of_iters")
        termination_eps = self.config("termination_eps")
        self.gauss_filt_size = self.config("gauss_filt_size")
        self.criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, number_of_iters, termination_eps)

        # selecting motion type based on user input
        if self.motion_type == "homography":
            self.motion_type_inp = cv2.MOTION_HOMOGRAPHY
        elif self.motion_type == "affine":
            self.motion_type_inp = cv2.MOTION_AFFINE
        elif self.motion_type == "euclidean":
            self.motion_type_inp = cv2.MOTION_EUCLIDEAN
        elif self.motion_type == "translation":
            self.motion_type_inp = cv2.MOTION_TRANSLATION
        else:
            raise ValueError(f"Motion type {self.motion_type_inp} not supported")

    def get_main_config(self):
        """ECC register default config creation"""
        config = {
            "register type": {"value": "ecc", "choices": ["ecc", "keypoint", "superglue"], "hint": "Registration type"},
            "motion_type": {"value": "affine", "choices": ["homography", "affine", "euclidean", "translation"], "hint": "Motion type to be used for registration"},
            "number_of_iters": {"value": 200, "choices": None, "hint": "The number of iterations to be done"},
            "termination_eps": {"value": 1e-4, "choices": None, "hint": "Threshold of the increment in the correlation coefficient between two iterations"},
            "gauss_filt_size": {"value": 5, "choices": None, "hint": "An optional value indicating size of gaussian blur filter"},
        }

        return config

    def get_child_configs(self):
        """Child config abstract method override"""
        child_configs = []

        return child_configs

    def register(self, fixed_img, moving_img, prev_matrix=None):
        """Register given fixed and moving images"""
        mkpts = None
        mdesc = None
        fixed_gray, moving_gray = self.conv_to_gray(fixed_img, moving_img)

        if prev_matrix is None:
            if self.motion_type == "homography":
                prev_matrix = np.eye(3, 3, dtype=np.float32)
            else:
                prev_matrix = np.eye(2, 3, dtype=np.float32)
        try:
            _, warp_matrix = cv2.findTransformECC(templateImage=fixed_gray, inputImage=moving_gray, warpMatrix=prev_matrix, motionType=self.motion_type_inp, criteria=self.criteria, inputMask=None, gaussFiltSize=self.gauss_filt_size)
        except:
            print("Registration failed, returning previous matrix")
            warp_matrix = prev_matrix

        moved = self.get_transformed_img(fixed_img, moving_img.shape[0], moving_img.shape[1], warp_matrix)

        return moved, warp_matrix, mkpts, mdesc


class TestEccRegister(unittest.TestCase):
    """Test methods"""

    def test_ecc_register(self):
        """Testing ecc register"""
        fixed_img_path = os.path.join("samples", "kitti_fixed.jpg")
        moving_img_path = os.path.join("samples", "kitti_moving.jpg")

        fixed_img = cv2.imread(fixed_img_path)
        moving_img = cv2.imread(moving_img_path)

        reg_obj = EccRegister(os.path.join("samples", "ecc_config.yaml"), False, True)
        _, warp_matrix, _, _ = reg_obj.register(fixed_img, moving_img)
        moved = reg_obj.get_transformed_img(fixed_img, moving_img.shape[0], moving_img.shape[1], warp_matrix)
        fused_img = fuse(fixed_img, moved)
        cv2.imwrite(os.path.join("samples", "test_results", "ecc_moved.jpg"), moved)
        cv2.imwrite(os.path.join("samples", "test_results", "ecc_fused.jpg"), fused_img)
        out_mat = np.array([[9.9359947e-01, -1.7977580e-02, -1.3662528e01], [-2.7650263e-04, 1.0068171e00, -7.9615694e-01]], dtype=np.float32)
        assert np.array_equal(np.int_(warp_matrix), np.int_(out_mat)), "Output matrix not matching with expected result"


if __name__ == "__main__":
    test_obj = TestEccRegister()
    test_obj.test_ecc_register()
