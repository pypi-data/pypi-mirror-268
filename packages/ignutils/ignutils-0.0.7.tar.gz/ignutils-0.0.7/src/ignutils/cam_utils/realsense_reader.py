"""Basic functions to read frames from realsense camera"""
import argparse
import cv2
import numpy as np
import pyrealsense2 as rs
import os
import time
from PIL import Image

class RealSenseReader:
    """Depth & Color of RGB frame reader class for Real Sense Depth camera"""

    def __init__(self, mode="stereo"):
        # Configure depth and color streams
        self.mode = mode
        self.pipeline = rs.pipeline()
        config = rs.config()

        if self.mode == "stereo":
            # Disable infrared in case of stereo
            self.cam_width = 1280
            self.cam_height = 720
            pipeline_wrapper = rs.pipeline_wrapper(self.pipeline)
            pipeline_profile = config.resolve(pipeline_wrapper)
            device = pipeline_profile.get_device()
            depth_sensor = device.query_sensors()[0]
            depth_sensor.set_option(rs.option.emitter_enabled, 1)
            config.enable_stream(rs.stream.infrared, 1, self.cam_width, self.cam_height, rs.format.y8, 6)
            config.enable_stream(rs.stream.infrared, 2, self.cam_width, self.cam_height, rs.format.y8, 6)
        
        if self.mode == "rgbd":
            self.cam_width = 640
            self.cam_height = 480
            config.enable_stream(rs.stream.depth, self.cam_width, self.cam_height, rs.format.z16, 30)
            config.enable_stream(rs.stream.color, self.cam_width, self.cam_height, rs.format.bgr8, 30)
        
        if self.mode == "imu":
            config.enable_stream(rs.stream.accel)
            config.enable_stream(rs.stream.gyro)

        # Start streaming
        self.pipeline.start(config)

    def get_depth_color(self):
        """Get depth and color images from camera
        Returns the depth colour map and the colour image"""
        frames = self.pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        depth_image = np.asanyarray(depth_frame.get_data())
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
        color_image = np.asanyarray(color_frame.get_data())
        return depth_image, depth_colormap, color_image

    def get_left_right(self):
        """Returns the left and right images from camera and return then as np-array"""
        frames = self.pipeline.wait_for_frames()
        left_data = frames.get_infrared_frame(1)
        right_data = frames.get_infrared_frame(2)

        left_img = np.asanyarray(left_data.get_data())
        right_img = np.asanyarray(right_data.get_data())
        return left_img, right_img

    def get_gyro_data(self, gyro):
        return np.asarray([gyro.x, gyro.y, gyro.z])

    def get_accel_data(self, accel):
        return np.asarray([accel.x, accel.y, accel.z])

    def get_imu_data(self):
        frames = self.pipeline.wait_for_frames()
        accel = self.get_accel_data(frames[0].as_motion_frame().get_motion_data())
        gyro = self.get_gyro_data(frames[1].as_motion_frame().get_motion_data())
        return accel, gyro

    def release(self):
        """Stop pipeline after reading"""
        self.pipeline.stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", default="stereo", help="Type of output: stereo, rgbd or imu")
    parser.add_argument("-o", "--output_folder", default="output", help="output folder name")
    parser.add_argument("-w", "--write_output", default=False, nargs="?", const=True, help="TO write output images")

    parser = parser.parse_args()
    mode_ = parser.mode
    output_folder = parser.output_folder
    write_output = parser.write_output

    reader_obj = RealSenseReader(mode_)
    output_path = os.path.join("data", output_folder)

    if mode_ == "stereo":
        cv2.namedWindow("left_frame", cv2.WINDOW_GUI_NORMAL)
        cv2.namedWindow("right_frame", cv2.WINDOW_GUI_NORMAL)
        left_out_path = os.path.join(output_path, "left")
        right_out_path = os.path.join(output_path, "right")
        os.makedirs(left_out_path, exist_ok=True)
        os.makedirs(right_out_path, exist_ok=True)
        frame_no = 0
        while True:
            left_frame, right_frame = reader_obj.get_left_right()
            cv2.imshow("left_frame", left_frame)
            cv2.imshow("right_frame", right_frame)
            left_write_path = os.path.join(left_out_path, f"frame_{frame_no}.jpg")
            right_write_path = os.path.join(right_out_path, f"frame_{frame_no}.jpg")
            if write_output:
                cv2.imwrite(left_write_path, left_frame)
                cv2.imwrite(right_write_path, right_frame)
            k = cv2.waitKey(1)
            frame_no += 1 
            if k == 27:
                break

    if mode_ == "rgbd":
        cv2.namedWindow("Depth", cv2.WINDOW_GUI_NORMAL)
        cv2.namedWindow("RGB", cv2.WINDOW_GUI_NORMAL)
        depthc_out_path = os.path.join(output_path, "depth_color")
        rgb_out_path = os.path.join(output_path, "rgb")
        depth_out_path = os.path.join(output_path, "depth")
        os.makedirs(depthc_out_path, exist_ok=True)
        os.makedirs(rgb_out_path, exist_ok=True)
        os.makedirs(depth_out_path, exist_ok=True)
        frame_no = 0
        while True:
            depth_image, depth_colormap, rgb_image = reader_obj.get_depth_color()
            cv2.imshow("Depth", depth_colormap)
            cv2.imshow("RGB", rgb_image)
            depthc_write_path = os.path.join(depthc_out_path, f"frame_{frame_no}.jpg")
            rgb_write_path = os.path.join(rgb_out_path, f"frame_{frame_no}.jpg")
            depth_write_path = os.path.join(depth_out_path, f"frame_{frame_no}.tif")
            if write_output:
                cv2.imwrite(depthc_write_path, depth_colormap)
                cv2.imwrite(rgb_write_path, rgb_image)
                Image.fromarray(depth_image).save(depth_write_path)
            k = cv2.waitKey(1)
            frame_no += 1
            if k == 27:
                break

    if mode_ == "imu":
        accel_out_path = os.path.join(output_path, "accel")
        gyro_out_path = os.path.join(output_path, "gyro")
        os.makedirs(accel_out_path, exist_ok=True)
        os.makedirs(gyro_out_path, exist_ok=True)
        accel_write_path = os.path.join(accel_out_path, "accel.txt")
        gyro_write_path = os.path.join(gyro_out_path, "gyro.txt")
        with open(accel_write_path, 'w') as accel_file, open(gyro_write_path, 'w') as gyro_file:
            while True:
                accel, gyro = reader_obj.get_imu_data()
                print("Acceleration: ", accel)
                print("Gyro: ", gyro)
                accel_file.write(str(accel)+'\n')
                gyro_file.write(str(gyro)+'\n')
                blank_img = np.zeros((400, 400))
                cv2.imshow("accel_gyro", blank_img)
                k = cv2.waitKey(1)
                if k == 27:
                    break

