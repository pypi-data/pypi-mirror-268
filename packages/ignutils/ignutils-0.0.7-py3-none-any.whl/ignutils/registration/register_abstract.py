"""Abstract class for registration methods"""
import abc
import cv2

from ignutils.config_utils import ConfigAbstract
from ignutils.transform_utils import transform_img


class RegisterAbstract(ConfigAbstract):
    """Abstract class for Registration methods"""

    def __init__(self, config_path, show_flag=False, print_flag=False, use_gpu=True):
        self.config_path = config_path
        self.show_flag = show_flag
        self.print_flag = print_flag
        self.use_gpu = use_gpu
        super().__init__(config_path=config_path)

    @abc.abstractmethod
    def register(self, fixed_img, moving_img):
        """Register fixed and moving images"""

        register_matrix = None
        return register_matrix

    @abc.abstractmethod
    def get_main_config(self):
        """Register main config creation"""
        config = {}
        return config

    @abc.abstractmethod
    def get_child_configs(self):
        """Register child configs creation"""
        child_configs = []

        return child_configs

    def conv_to_gray(self, fixed_img, moving_img):
        """Convert fixed and moving images to gray scale"""

        fixed_img = cv2.cvtColor(fixed_img, cv2.COLOR_BGR2GRAY)
        moving_img = cv2.cvtColor(moving_img, cv2.COLOR_BGR2GRAY)
        return fixed_img, moving_img

    def get_transformed_img(self, img, target_ht, target_wd, trans_mat):
        """Get transformed image after applying registration matrix"""
        trans_img = transform_img(img, target_ht, target_wd, trans_mat, flag=cv2.INTER_LINEAR)

        return trans_img

    def get_transformation_matrix(self, src_points, dst_points):
        """Get transformation matrix given source and destination keypoints"""
        trans_mat, _ = cv2.findHomography(src_points, dst_points, cv2.RANSAC, 5.0)

        return trans_mat
