# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : sterio_record.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""Function to record video from left and right cameras at the same time"""
import argparse
import os
import sys
import cv2

from ignutils.cam_utils.camera_reader import CameraReader
from ignutils.cam_utils.realsense_reader import RealSenseReader
from ignutils.draw_utils import put_text

def stereo_record(left_cam_id=0, right_cam_id=2, path="data/stereo_videos", realsense=False):
    """Record left and right videos for stereo cameras

    Args:
        left_cam_id (int, optional): Left camera index. Defaults to 0.
        right_cam_id (int, optional): Right camera index. Defaults to 2.
        path (str, optional): Folder path for saving videos. Defaults to "stereo_videos".

    Raises:
        Exception: If dump folder already exists.
    """
    if os.path.exists(path):
        print("Dump folder already exists")
        sys.exit()
    os.makedirs(path)

    cam_obj = None
    left_cap = None
    right_cap = None
    write_flag = False
    img_left = None
    img_right = None

    if realsense:
        cam_obj = RealSenseReader()
        left_fps = 10
        left_width = cam_obj.cam_width
        left_height = cam_obj.cam_height
        is_color = False
    else:
        left_cam_obj = CameraReader(cam_index=left_cam_id, ui_flag=True, setting_path="data/left_setting.json")
        right_cam_obj = CameraReader(cam_index=right_cam_id, ui_flag=True, setting_path="data/right_setting.json")

        left_width = left_cam_obj.cam_width
        left_height = left_cam_obj.cam_height
        right_width = right_cam_obj.cam_width
        right_height = right_cam_obj.cam_height
        left_fps = left_cam_obj.fps
        right_fps = right_cam_obj.fps

        assert left_width == right_width, "Image width is not matching between two cameras"
        assert left_height == right_height, "Image height is not matching between two cameras"
        assert left_fps == right_fps, "FPS is not matching between two cameras"
        is_color = True
        left_cap = left_cam_obj.get_cap()
        right_cap = right_cam_obj.get_cap()

    print("Width: ", left_width)
    print("Height: ", left_height)
    print("FPS: ", left_fps)
    fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")

    writer_left = cv2.VideoWriter(f"{path}/left.mp4", fourcc, left_fps, (left_width, left_height), is_color)
    writer_right = cv2.VideoWriter(f"{path}/right.mp4", fourcc, left_fps, (left_width, left_height), is_color)

    cv2.namedWindow("Left", cv2.WINDOW_GUI_NORMAL)
    cv2.namedWindow("Right", cv2.WINDOW_GUI_NORMAL)

    while True:
        if realsense and cam_obj is not None:
            _, img_left, img_right = cam_obj.get_left_right()

        else:
            if left_cap is not None and right_cap is not None:
                _, img_left = left_cap.read()
                _, img_right = right_cap.read()

        if img_left is None or img_right is None:
            break

        left_show = img_left.copy()
        right_show = img_right.copy()

        if write_flag is False:
            left_show = put_text("Press 's' to start recording video", left_show, 50, 50, color=(255, 0, 0), thickness=3)
            right_show = put_text("Press 's' to start recording video", right_show, 50, 50, color=(255, 0, 0), thickness=3)

        k = cv2.waitKey(left_fps)

        if k == 27:
            print("Exiting video writing")
            break

        if k == ord("s"):
            if write_flag is False:
                write_flag = True
                print("Started video writing")

        if write_flag is True:
            left_show = put_text("Started Recording...", left_show, 50, 50, color=(255, 0, 0), thickness=3)
            left_show = put_text("Press 'Esc' to quit", left_show, 50, 100, color=(255, 0, 0), thickness=3)
            right_show = put_text("Started Recording...", right_show, 50, 50, color=(255, 0, 0), thickness=3)
            right_show = put_text("Press 'Esc' to quit", right_show, 50, 100, color=(255, 0, 0), thickness=3)
            writer_left.write(img_left)
            writer_right.write(img_right)

        cv2.imshow("Left", left_show)
        cv2.imshow("Right", right_show)

    writer_left.release()
    writer_right.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-left_id", "--left_id", default=0, type=int, help="Left camera index")
    parser.add_argument("-right_id", "--right_id", default=2, type=int, help="Right camera index")
    parser.add_argument("-p", "--path", default="data/stereo_videos", type=str, help="Folder path to save videos")
    parser.add_argument("-rs", "--realsense", default=False, nargs="?", const=True, help="To record from realsense camera")

    parser = parser.parse_args()
    left_id = parser.left_id
    right_id = parser.right_id
    path_ = parser.path
    realsense_ = parser.realsense

    stereo_record(left_id, right_id, path_, realsense_)
