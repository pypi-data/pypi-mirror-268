"""Reads web camera frames and set camera properties."""
import unittest
import os
import cv2
from ignutils.draw_utils import put_text
from ignutils.yaml_utils import read_yaml, write_yaml


class CameraReader:
    """Reading the frames from web camera and a basic track bar based UI to change settings of the camera.
    cam_obj = CameraReader(cam_index=0, ui_flag=ui_flag)
    cam_obj.get_cap()
    cam_obj.cam_props_ui()
    """

    def __init__(self, cam_index=0, ui_flag=False, setting_path="cam_setting.yaml"):
        self.focus = None
        self.saturation = None
        self.cam_width = None
        self.cam_height = None
        self.auto_focus = None
        self.fps = 25
        self.frame_num = 0
        self.ui_flag = ui_flag
        self.cam_index = cam_index
        self.setting_path = setting_path
        self.cam_window_name = "CamSettings"
        self.cap = cv2.VideoCapture(cam_index)
        self.load_params()
        if ui_flag:
            self.cam_props_ui()

    def next_frame(self):
        """Get the next frame from cap
        Returns the image and the frame number
        """
        ret, img = self.cap.read()
        if ret:
            self.frame_num += 1
        else:
            img = None
        return img, self.frame_num - 1

    def get_cap(self):
        """Returns a cap object"""
        return self.cap

    def get_cam_props(self):
        """Get camera properties from cap"""
        self.focus = int(self.cap.get(cv2.CAP_PROP_FOCUS))
        self.saturation = int(self.cap.get(cv2.CAP_PROP_SATURATION))
        self.cam_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.cam_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.auto_focus = int(self.cap.get(cv2.CAP_PROP_AUTOFOCUS))
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))

    def load_params(self):
        """Load camera params from setting file provided"""
        if os.path.isfile(self.setting_path):
            self.params = read_yaml(self.setting_path)
        else:
            self.get_cam_props()
            self.params = {
                "cam_width": self.cam_width,
                "cam_height": self.cam_height,
                "auto_focus": self.auto_focus,
                "saturation": self.saturation,
                "focus": self.focus,
            }
            self.save_params()
        self.set_cam_params()

    def save_params(self):
        """Save the cam params"""
        properties = {
            "cam_width": self.cam_width,
            "cam_height": self.cam_height,
            "auto_focus": 0,
            "saturation": self.saturation,
            "focus": self.focus,
        }
        write_yaml(self.setting_path, properties)

    def create_trackbar(self):
        """Create trackbar for saturation, focus adjust"""
        window_name = self.cam_window_name
        cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)
        cv2.createTrackbar("SATURATION", window_name, int(self.saturation), 255, self.on_trackbar_sat)
        cv2.createTrackbar("FOCUS", window_name, int(self.focus), 255, self.on_trackbar_foc)

    def on_trackbar_foc(self, val):
        """tracker adjustment for focus"""
        self.cap.set(cv2.CAP_PROP_FOCUS, val)
        self.focus = int(self.cap.get(cv2.CAP_PROP_FOCUS))
        self.cap.set(cv2.CAP_PROP_FOCUS, self.focus)
        cv2.setTrackbarPos("FOCUS", self.cam_window_name, self.focus)

    def on_trackbar_sat(self, val):
        """tracker adjustment for saturation"""
        self.cap.set(cv2.CAP_PROP_SATURATION, val)
        self.saturation = int(self.cap.get(cv2.CAP_PROP_SATURATION))
        self.cap.set(cv2.CAP_PROP_SATURATION, self.saturation)
        cv2.setTrackbarPos("SATURATION", self.cam_window_name, self.saturation)

    def set_cam_params(self):
        """set camera properties from loaded params"""
        self.cap.set(cv2.CAP_PROP_AUTOFOCUS, self.params["auto_focus"])
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.params["cam_width"])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.params["cam_height"])
        self.cap.set(cv2.CAP_PROP_FPS, self.fps)
        self.cap.set(cv2.CAP_PROP_SATURATION, self.params["saturation"])
        self.cap.set(cv2.CAP_PROP_FOCUS, self.params["focus"])
        self.get_cam_props()

    def cam_props_ui(self):
        """UI with property settings"""
        self.create_trackbar()
        text = "Press Esc to save settings & Quit"
        while True:
            ret, frame = self.cap.read()
            frame = put_text(
                f"{text}",
                frame,
                (20),
                (50),
                color=(0, 255, 0),
                font_scale=1.8,
                thickness=3,
                font=cv2.QT_FONT_NORMAL,
                draw_bg=True,
            )
            cv2.imshow("InputFrame", frame)
            k = cv2.waitKey(30)
            if k == 27:
                self.save_params()
                break
        cv2.destroyAllWindows()


class TestCameraReader(unittest.TestCase):
    """Test methods"""

    def test_camera_reader_with_ui(self, ui_flag=True):
        """Demo of the camera reader with cam setting ui"""
        cam_obj = CameraReader(cam_index=0, ui_flag=ui_flag)
        cap = cam_obj.get_cap()
        while True:
            ret_, frame = cap.read()
            cv2.imshow("InputFrame", frame)
            k = cv2.waitKey(30)
            if k == 27:
                break

    def test_camera_reader_wo_ui(self):
        """Demo of the camera reader without cam setting"""
        self.test_camera_reader_with_ui(ui_flag=False)


if __name__ == "__main__":
    test_obj = TestCameraReader()
    test_obj.test_camera_reader_with_ui()
    # test_obj.test_camera_reader_wo_ui()
