"""To dump stereo image pairs for left and right cameras"""
import argparse
import os
import cv2

from ignutils.json_utils import read_json
from ignutils.cam_utils.camera_reader import CameraReader
from ignutils.cam_utils.realsense_reader import RealSenseReader


def stereo_dump(calib_settings="calibration_settings.json", realsense=False):
    """Dump stereo image pairs for left and right cameras

    Args:
        calib_settings (str, optional): Calibration settings json. Defaults to "calibration_settings.json".
        realsense (bool, optional): To use realsense camera. Defaults to False.
    """
    # create frames directory
    left_dump_dir = os.path.join("data", "stereo_images", "left")
    os.makedirs(left_dump_dir, exist_ok=True)
    right_dump_dir = os.path.join("data", "stereo_images", "right")
    os.makedirs(right_dump_dir, exist_ok=True)

    calib_settings = read_json(calib_settings)
    cooldown_time = calib_settings["cooldown"]
    number_to_save = calib_settings["stereo_calibration_frames"]
    left_id = calib_settings["left_id"]
    right_id = calib_settings["right_id"]
    cam_obj = None
    left_cap = None
    right_cap = None
    left_img = None
    right_img = None
    start = False
    saved_count = 0
    cooldown = cooldown_time

    if realsense:
        cam_obj = RealSenseReader()
        left_fps = 10
        left_width = cam_obj.cam_width
        left_height = cam_obj.cam_height
    else:
        left_cam_obj = CameraReader(cam_index=left_id, ui_flag=True, setting_path="data/left_setting.json")
        right_cam_obj = CameraReader(cam_index=right_id, ui_flag=True, setting_path="data/right_setting.json")

        left_width = left_cam_obj.cam_width
        left_height = left_cam_obj.cam_height
        right_width = right_cam_obj.cam_width
        right_height = right_cam_obj.cam_height
        left_fps = left_cam_obj.fps
        right_fps = right_cam_obj.fps

        assert left_width == right_width, "Image width is not matching between two cameras"
        assert left_height == right_height, "Image height is not matching between two cameras"
        assert left_fps == right_fps, "FPS is not matching between two cameras"
        left_cap = left_cam_obj.get_cap()
        right_cap = right_cam_obj.get_cap()

    cv2.namedWindow("left", cv2.WINDOW_GUI_NORMAL)
    cv2.namedWindow("right", cv2.WINDOW_GUI_NORMAL)
    while True:
        if realsense and cam_obj is not None:
            _, left_img, right_img = cam_obj.get_left_right()
        else:
            if left_cap is not None and right_cap is not None:
                _, left_img = left_cap.read()
                _, right_img = right_cap.read()

        if left_img is None or right_img is None:
            print("Cameras not returning video data. Exiting...")
            break

        left_small = left_img.copy()
        right_small = right_img.copy()

        if not start:
            cv2.putText(left_small, "Make sure both cameras can see the calibration pattern well", (50, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 5)
            cv2.putText(left_small, "Press SPACEBAR to start collection frames", (50, 130), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 5)

        if start:
            cooldown -= 1
            cv2.putText(left_small, "Cooldown: " + str(cooldown), (50, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 7)
            cv2.putText(left_small, "Num frames: " + str(saved_count), (50, 130), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 7)

            cv2.putText(right_small, "Cooldown: " + str(cooldown), (50, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 7)
            cv2.putText(right_small, "Num frames: " + str(saved_count), (50, 130), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 7)

            # save the frame when cooldown reaches 0.
            if cooldown <= 0:
                savename = os.path.join(left_dump_dir, f"frame_{str(saved_count)}.png")
                cv2.imwrite(savename, left_img)

                savename = os.path.join(right_dump_dir, f"frame_{str(saved_count)}.png")
                cv2.imwrite(savename, right_img)

                saved_count += 1
                cooldown = cooldown_time

        cv2.imshow("left", left_small)
        cv2.imshow("right", right_small)
        k = cv2.waitKey(1)

        if k == 27:
            break

        if k == 32:
            start = True

        if saved_count == number_to_save:
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-cs", "--calib_settings", default="calibration_settings.json", help="path for calibration settings json")
    parser.add_argument("-rs", "--realsense", default=False, nargs="?", const=True, help="To record from realsense camera")

    parser = parser.parse_args()
    calib_settings_ = parser.calib_settings
    realsense_ = parser.realsense

    stereo_dump(calib_settings_, realsense_)
