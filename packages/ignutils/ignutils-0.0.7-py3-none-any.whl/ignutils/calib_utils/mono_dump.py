"""Dump calibration images for single camera"""
import os
import argparse
import cv2

from ignutils.cam_utils.camera_reader import CameraReader
from ignutils.cam_utils.realsense_reader import RealSenseReader
from ignutils.json_utils import read_json


def mono_dump(camera_name, calib_settings, realsense=False):
    """Save images from single camera for mono calibration

    Args:
        camera_name (str): Name of the camera left/right
        calib_settings (str): Calibration settings file location
        realsense (bool, optional): To use realsense camera. Defaults to False.
    """
    dump_dir = f"data/mono_images/{camera_name}"
    os.makedirs(dump_dir, exist_ok=True)

    # Calibration settings
    settings = read_json(calib_settings)
    left_id = settings["left_id"]
    right_id = settings["right_id"]
    number_to_save = settings["mono_calibration_frames"]
    cooldown_time = settings["cooldown"]

    cam_obj, rs_cam_obj, cap, frame = None, None, None, None
    if realsense:
        rs_cam_obj = RealSenseReader()
    else:
        setting_path = "data/left_setting.json" if camera_name == "left" else "data/right_setting.json"
        cam_id = left_id if camera_name == "left" else right_id
        cam_obj = CameraReader(cam_index=cam_id, ui_flag=True, setting_path=setting_path)
        cap = cam_obj.get_cap()

    cooldown = cooldown_time
    start = False
    saved_count = 0

    cv2.namedWindow("frame_small", cv2.WINDOW_GUI_NORMAL)
    while True:
        if realsense and rs_cam_obj is not None:
            _, left_img, right_img = rs_cam_obj.get_left_right()
            if camera_name == "left":
                frame = left_img
            else:
                frame = right_img
        else:
            if cap is not None:
                _, frame = cap.read()

        if frame is None:
            # if no video data is received, can't calibrate the camera, so exit.
            print("No video data received from camera. Exiting...")
            break

        frame_small = frame.copy()

        if not start:
            cv2.putText(frame_small, "Press SPACEBAR to start collection frames", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

        if start:
            cooldown -= 1
            cv2.putText(frame_small, "Cooldown: " + str(cooldown), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
            cv2.putText(frame_small, "Num frames: " + str(saved_count), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

            # save the frame when cooldown reaches 0.
            if cooldown <= 0:
                savename = os.path.join(dump_dir, f"frame_{str(saved_count)}.png")
                cv2.imwrite(savename, frame)
                saved_count += 1
                cooldown = cooldown_time

        cv2.imshow("frame_small", frame_small)
        k = cv2.waitKey(1)

        if k == 27:
            quit()

        if k == 32:
            # Press spacebar to start data collection
            start = True

        # Break out when enough number of frames have been saved
        if saved_count == number_to_save:
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-cs", "--calib_settings", default="calibration_settings.json", help="path for calibration settings json")
    parser.add_argument("-cn", "--camera_name", default="left", type=str, help="Left/Right camera")
    parser.add_argument("-rs", "--realsense", default=False, nargs="?", const=True, help="To record from realsense camera")

    parser = parser.parse_args()
    cam_name_ = parser.camera_name
    calib_settings_ = parser.calib_settings
    realsense_ = parser.realsense

    mono_dump(cam_name_, calib_settings_, realsense_)
