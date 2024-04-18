"""To get the GPS information of the tie locations in the camera pairs."""
import re
import math
from datetime import datetime
import unittest
import cv2
import numpy as np
from bs4 import BeautifulSoup
from scipy import interpolate

from ignutils.draw_utils import print_colored
from ignutils.video_utils.exif_utils import get_metadata


def get_gps_data(right_video_path, gpx_path):
    """get gps data"""
    file_info, gps_data = get_metadata(right_video_path, fmt_file=gpx_path)
    video_times = None
    gps_times = None
    latitude = None
    longitude = None
    if gps_data is not None:
        gps_data = BeautifulSoup(gps_data, "xml")
        sample_time, gps_times, latitude, longitude = get_gps_info(gps_data)
        video_times = sample_time[0]
        gps_times = gps_times[0]
        latitude = latitude[0]
        longitude = longitude[0]
    return video_times, gps_times, latitude, longitude


def get_gps_data_cleaned(right_video_path, gpx_path, print_flag=True):
    """Return video time, lat and longitude for every frame in a video.
    If video time of any frame number not increasing,
    new video time calculated with fps and
    assigns new lat long by curve fitting.
    """

    cap = cv2.VideoCapture(right_video_path)
    frames_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Reading from metadata
    if print_flag:
        print("Reading gps info from metadata")

    video_times, gps_times, latitude, longitude = get_gps_data(right_video_path, gpx_path)

    # video times clean up
    clean_times = []
    clean_lat = []
    clean_long = []
    clean_gps_times = []
    for index in range(len(video_times) - 1):
        if video_times[index + 1] <= video_times[index]:
            print_colored(
                f"[!] Warning, videoTime is not increasing in row {index} of gps data",
                "red",
            )
        else:
            clean_times.append(video_times[index])
            clean_lat.append(latitude[index])
            clean_long.append(longitude[index])
            clean_gps_times.append(gps_times[index])

    lat_f = interpolate.interp1d(clean_times, clean_lat, bounds_error=False, fill_value="extrapolate")
    long_f = interpolate.interp1d(clean_times, clean_long, bounds_error=False, fill_value="extrapolate")
    gps_f = interpolate.interp1d(clean_times, clean_gps_times, bounds_error=False, fill_value="extrapolate")
    # update error values
    gps_data = []
    for index in range(len(video_times) - 1):
        if video_times[index + 1] <= video_times[index]:
            new_time = (index + 1) / fps
            new_time = math.floor(new_time * 1000) / 1000
            video_times[index + 1] = new_time
            latitude[index + 1] = lat_f(new_time)
            longitude[index + 1] = long_f(new_time)
            gps_times[index + 1] = gps_f(new_time)

    if isinstance(video_times, np.ndarray):
        video_times = list(video_times)
    if isinstance(latitude, np.ndarray):
        latitude = list(latitude)
    if isinstance(longitude, np.ndarray):
        longitude = list(longitude)
    if isinstance(gps_times, np.ndarray):
        gps_times = list(gps_times)
    gps_data.append(video_times)
    gps_data.append(gps_times)
    gps_data.append(latitude)
    gps_data.append(longitude)

    return gps_data, lat_f, long_f, gps_f


def get_gps_info(data):
    """Extract info from gps xml data"""
    if isinstance(data, str):
        with open(data, "r", encoding="utf8") as f:
            data = f.read()
        data = BeautifulSoup(data, "xml")
    track_pt = data.find_all("trkpt")
    sample_time_list = [[], []]
    gps_time_list = [[], []]
    latitude_list = [[], []]
    longitude_list = [[], []]
    prev_sample_time = None
    gps_sensor_index = 0
    for index, trk in enumerate(track_pt):
        sample_time = trk.sampleTime.string
        sample_time = float(sample_time)
        if prev_sample_time is None:
            prev_sample_time = sample_time
        gps_time = trk.gpsTime.string
        gps_datetime = datetime.fromisoformat(gps_time)
        timestamp = gps_datetime.timestamp()

        # print("timestamp:", timestamp)
        # print("datetime:", gps_datetime)

        trk_s = str(trk)
        lat_s = trk_s.split("lat=")
        lat = lat_s[1].split("lon=")[0].strip(" ")
        lat = re.findall(r"([+-]?\d+(?:\.\d+)?(?:[eE][+-]\d+)?)", lat)[0]
        lat = float(lat)
        lon = lat_s[1].split("lon=")[1].split("<sampleTime>")[0].strip()
        lon = re.findall(r"([+-]?\d+(?:\.\d+)?(?:[eE][+-]\d+)?)", lon)[0]
        lon = float(lon)

        # Since there are two gps sensors, first set of values append to
        # gps_sensor_index 0, next set append to gps_sensor_index 1
        if prev_sample_time > sample_time:
            gps_sensor_index = 1
        sample_time_list[gps_sensor_index].append(sample_time)
        gps_time_list[gps_sensor_index].append(timestamp)
        latitude_list[gps_sensor_index].append(lat)
        longitude_list[gps_sensor_index].append(lon)
        prev_sample_time = sample_time
    return sample_time_list, gps_time_list, latitude_list, longitude_list

class TestExtractGpsData(unittest.TestCase):
    """Test Methods"""
    @classmethod
    def setUpClass(cls):
        cls.right_video_path = "/home/skycam/Downloads/StopwatchTest/Test2/Driver/20221107_100725_NF.mp4"
        # cls.right_video_path ='/home/skycam/Downloads/StopwatchTest/Test2/Passenger/20221107_150805_NF.mp4'
        cls.gpx_path="/home/skycam/aTYQI/ign_utils/Projects/LR_Stitcher/gpx.fmt"

    def test_get_gps_data_cleaned(self):
        """Test for getting cleaned gps data"""
        gps_data, lat_f, long_f, gps_f = get_gps_data_cleaned(self.right_video_path,self.gpx_path)
        print("gps_data:", gps_data)

    def test_get_gps_info(self):
        """test for getting gps info"""
        sample_time, gps_time, latitude_list, longitude_list = get_gps_info("gps_l.xml")

if __name__ == "__main__":
    test_obj = TestExtractGpsData()
    test_obj.setUpClass()
    test_obj.test_get_gps_data_cleaned()
    test_obj.test_get_gps_info()
