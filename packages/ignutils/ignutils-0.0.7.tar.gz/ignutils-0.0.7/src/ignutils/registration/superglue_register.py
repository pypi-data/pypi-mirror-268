"""Class for Superglue model based registration"""
import unittest
import os
import cv2
# import matplotlib.cm as cm
from matplotlib import cm
import numpy as np

from ignutils.show_utils import show, fuse
from ignutils.registration.register_abstract import RegisterAbstract
from ignutils.registration.superglue.models.matching import Matching
from ignutils.registration.superglue.models.utils import frame2tensor, make_matching_plot_fast
from ignutils.gpu_utils import select_device_pytorch

class SuperglueRegister(RegisterAbstract):
    """ECC transform based registration"""

    def __init__(self, config_path, show_flag=False, print_flag=False, use_gpu=True):
        super().__init__(config_path, show_flag, print_flag)
        self.nms_radius = self.config("nms_radius")
        self.keypoint_threshold = self.config("keypoint_threshold")
        self.max_keypoints = self.config("max_keypoints")
        self.superglue_weights = self.config("superglue_weights")
        self.sinkhorn_iterations = self.config("sinkhorn_iterations")
        self.match_threshold = self.config("match_threshold")
        self.resize = self.config("resize")
        self.superglue_config = {
            "superpoint": {"nms_radius": self.nms_radius, "keypoint_threshold": self.keypoint_threshold, "max_keypoints": self.max_keypoints},
            "superglue": {
                "weights": self.superglue_weights,
                "sinkhorn_iterations": self.sinkhorn_iterations,
                "match_threshold": self.match_threshold,
            },
        }
        self.device = select_device_pytorch(use_gpu, min_memory=4000)
        print(f"Running inference on device {self.device}")
        self.matching = Matching(self.superglue_config).eval().to(self.device)

    def get_main_config(self):
        """ECC register default config creation"""
        config = {
            "register type": {"value": "superglue", "choices": ["ecc", "keypoint", "superglue"], "hint": "Registration type"},
            "keypoint_threshold": {"value": 0.005, "choices": None, "hint": "SuperPoint keypoint detector confidence threshold"},
            "nms_radius": {"value": 4, "choices": None, "hint": "SuperPoint Non Maximum Suppression (NMS) radius"},
            "max_keypoints": {"value": -1, "choices": None, "hint": "Maximum number of keypoints detected by Superpoint ('-1' keeps all keypoints)"},
            "superglue_weights": {"value": "outdoor", "choices": ["outdoor", "indoor"], "hint": "SuperPoint keypoint detector confidence threshold"},
            "sinkhorn_iterations": {"value": 20, "choices": None, "hint": "Number of Sinkhorn iterations performed by SuperGlue"},
            "match_threshold": {"value": 0.2, "choices": None, "hint": "SuperGlue match threshold"},
            "force_cpu": {"value": False, "choices": [True, False], "hint": "Force pytorch to run in CPU mode"},
            "resize": {"value": [480, 640], "choices": None, "hint": "esize the input image before running inference. Two numbers required"},
        }

        return config

    def get_child_configs(self):
        """Child config abstract method override"""
        child_configs = []

        return child_configs

    def process_resize(self, w, h, resize):
        """Get new width and height based on given resize"""
        assert len(resize) > 0 and len(resize) <= 2
        if len(resize) == 1 and resize[0] > -1:
            scale = resize[0] / max(h, w)
            w_new, h_new = int(round(w * scale)), int(round(h * scale))
        elif len(resize) == 1 and resize[0] == -1:
            w_new, h_new = w, h
        else:  # len(resize) == 2:
            w_new, h_new = resize[0], resize[1]

        # Issue warning if resolution is too small or too large.
        if max(w_new, h_new) < 160:
            print("Warning: input resolution is very small, results may vary")
        elif max(w_new, h_new) > 2000:
            print("Warning: input resolution is very large, results may vary")

        return w_new, h_new

    def resize_imgs(self, img1, img2):
        """Convert image to grayscale and resize to config size"""
        grayim1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        grayim2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        w1, h1 = grayim1.shape[1], grayim1.shape[0]
        w2, h2 = grayim2.shape[1], grayim2.shape[0]
        w_new1, h_new1 = self.process_resize(w1, h1, self.resize)
        w_new2, h_new2 = self.process_resize(w2, h2, self.resize)
        grayim1 = cv2.resize(grayim1, (w_new1, h_new1), interpolation=cv2.INTER_AREA)
        grayim2 = cv2.resize(grayim2, (w_new2, h_new2), interpolation=cv2.INTER_AREA)

        return grayim1, grayim2

    def register(self, fixed_img, moved_img, resize_imgs=True):
        """Register given fixed and moving images"""
        # Convert input images to grayscale and resize if required
        if resize_imgs:
            fixed_resized, moving_resized = self.resize_imgs(fixed_img, moved_img)
        else:
            fixed_resized = fixed_img
            moving_resized = moved_img

        # Converting image to tensor
        fixed_tensor = frame2tensor(fixed_resized, self.device)
        moving_tensor = frame2tensor(moving_resized, self.device)

        # Loading superglue model and predicting matches
        last_data = self.matching.superpoint({"image": fixed_tensor})
        keys = ["keypoints", "scores", "descriptors"]
        last_data = {k + "0": last_data[k] for k in keys}
        last_data["image0"] = fixed_tensor
        pred = self.matching({**last_data, "image1": moving_tensor})  # pylint: disable=E1102

        # Getting keypoints and matches
        kpts0 = last_data["keypoints0"][0].cpu().numpy()
        kpts1 = pred["keypoints1"][0].cpu().numpy()
        matches = pred["matches0"][0].cpu().numpy()
        confidence = pred["matching_scores0"][0].cpu().detach().numpy()

        # Valid keypoints from fixed and moving images
        valid = matches > -1
        mkpts0 = kpts0[valid]
        mkpts1 = kpts1[matches[valid]]

        # Getting trans mat and moved img
        mat = self.get_transformation_matrix(mkpts1, mkpts0)
        moved = self.get_transformed_img(moving_resized, fixed_resized.shape[0], fixed_resized.shape[1], mat)
        if self.print_flag:
            print("Transformation Matrix :", mat)

        # Plotting matches
        small_text = [f"Keypoint Threshold: {self.keypoint_threshold}", f"Match Threshold: {self.match_threshold}"]
        color = cm.jet(confidence[valid])  # pylint: disable=E1101
        text = ["SuperGlue", f"Keypoints: {len(kpts0)}:{len(kpts1)}", f"Matches: {len(mkpts0)}"]
        make_matching_plot_fast(fixed_resized, moving_resized, kpts0, kpts1, mkpts0, mkpts1, color, text, path=None, show_keypoints=self.show_flag, opencv_display=self.show_flag, small_text=small_text)

        # Fused image
        fuz = fuse(fixed_resized, moved)
        if self.show_flag:
            show(fuz, win="fused", time=0, destroy=False, k=-1)

        return moved, mat, mkpts1, mkpts0


class TestSuperglueRegistration(unittest.TestCase):
    """Unit test for superglue registration"""

    def test_superglue_register(self):
        """Test superglue register"""
        fixed_img_path = os.path.join("samples", "kitti_fixed.jpg")
        moving_img_path = os.path.join("samples", "kitti_moving.jpg")

        fixed = cv2.imread(fixed_img_path)
        moving = cv2.imread(moving_img_path)

        reg_obj = SuperglueRegister(os.path.join("samples", "superglue_config.yaml"), False, True, use_gpu=False)
        moved, mat, _, _ = reg_obj.register(fixed, moving)
        fused_img = fuse(fixed, moved)
        cv2.imwrite(os.path.join("samples", "test_results", "superglue_moved.jpg"), moved)
        cv2.imwrite(os.path.join("samples", "test_results", "superglue_fused.jpg"), fused_img)
        out_mat = np.array([[9.99247677e-01, 1.20604239e-02, 3.24844081e00], [6.50844826e-03, 9.89924317e-01, 9.40535390e-02], [1.32211230e-05, -2.28360751e-05, 1.00000000e00]], dtype=np.float32)
        assert np.array_equal(np.int_(mat), np.int_(out_mat)), "Output matrix not matching with expected result"


if __name__ == "__main__":
    test_obj = TestSuperglueRegistration()
    test_obj.test_superglue_register()
