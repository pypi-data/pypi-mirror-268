"""Wrapper Class for Registration"""
from ignutils.registration.ecc_register import EccRegister
from ignutils.registration.keypoint_register import KeypointRegister
# from ignutils.registration.superglue_register import SuperglueRegister

# pylint: disable=too-few-public-methods
class RegistrationWrapper:
    """Optical flow based registration"""

    def __init__(
        self,
        register_type,
        config_dir=None,
        name="config", # can be used to differentiate between registration use cases
        show_flag=False,
        print_flag=False,
    ):
        config_path = f"{config_dir}/{register_type}_{name}.yaml"
        if register_type == "ecc":
            self.reg_obj = EccRegister(config_path, show_flag, print_flag)
        if register_type == "keypoint":
            self.reg_obj = KeypointRegister(config_path, show_flag, print_flag)
        # if register_type == "superglue":
        #     self.reg_obj = SuperglueRegister(config_path, show_flag, print_flag)

    def register(self, fixed_image, moving_image):
        """Calling register method based on the register type"""
        moved_img, trans_mat, mkpts, mdesc = self.reg_obj.register(fixed_image, moving_image)

        return moved_img, trans_mat, mkpts, mdesc
