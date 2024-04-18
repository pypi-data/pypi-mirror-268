# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : stitch_det_track_seq.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""To do stiching, detection and tracking of the given video pair."""

import argparse
import os
from selectors import EpollSelector
import time
from operator import itemgetter

import cv2
import numpy as np
from ignutils.algo_utils import binary_search_lower, binary_search_upper
from ignutils.clone_utils import CloneRepo
from ignutils.contour_utils import check_overlap_height, get_overlap_area, translate_points, get_xy_loc
from ignutils.draw_utils import print_colored
from ignutils.stitch_det_track.stitch import StitchRetainCanvas
from ignutils.stitch_det_track.unique_identifier import UniqueIdentifier
from ignutils.system_utils import check_service_available
from ignutils.transform_utils import transform_crop
from ignutils.workflow.workflow_main import InferWorkflow
from ignutils.draw_utils import put_text
from ignutils.show_utils import show
from threading import Thread
from queue import Queue

CWD = os.getcwd()


class StitchDetTrackSeq:
    """Class for handling stitching, detection and tracking in sequential."""

    def __init__(  # pylint: disable=too-many-arguments
        self,
        threshold: int,
        projectname: str,
        nodes: list,
        tracking_nodes: list,
        project_config_path=None,
        work_dir=None,
        disabled_nodes=None,
        stitch_flag: bool = True,
        nfeatures=2000,
        reg_threshold=None,
        window_len=30,
        uniq_flag: bool = True,
        det_flag: bool = True,
        track_flag: bool = True,
        write_canvas_flag: bool = False,
        roi_frac=(-1, -1, -1, -1),
        roi_flag=False,
        resize_factor=-1,
        life_count=8,
        overlap_threshold=0,
        roi_pts_path=".",
        redraw_pts=False,
        gps_data=None,
        lat_f=None,
        long_f=None,
        gps_f=None,
        show_id=False,
        show_pos=False,
        det_show=False,
        write_csv=True,
        cluster_mode="non_cluster",
        fps=30,  # TO-DO as input (No hardcoding)
        count_up=True,  # Upward direction counting
        history_cleanup=True,
        triton_mode=False,
        print_flag=True,
        cam_direction="Down",  # Up, Down, Up_Down # camera moving direction, LR_Stitcher Down
        git_flag=True,
        gpu_flag=True,
        stash_flag=False,
        pull_flag=False,
        y1_pos=-600,
        show_flag=False,
        relay_trigger=True,
        pause_dis=False,
        device_file=None,
        on_time=0.5,
        queue_frame_skip=False,
        infer_workflow=True,
        start_id=0
    ) -> None:
        """Init for Stitch_Det_Track"""
        if disabled_nodes is None:
            disabled_nodes = []

        if reg_threshold is None:
            reg_threshold = [-300, 2]

        self.project_config_path = project_config_path
        self.count_up = count_up
        self.cluster_mode = cluster_mode
        self.cam_direction = cam_direction
        self.print_flag = print_flag
        self.history_cleanup = history_cleanup
        self.index = 0
        self.first_frame = True
        self.gps_data = gps_data  # gps_data extracted from Video file
        self.prev_frame_num = None
        self.y_shift = None
        self.life_count = life_count
        self.overlap_threshold = overlap_threshold
        self.uniq_iden = UniqueIdentifier(threshold)
        self.stitch_flag = stitch_flag
        self.uniq_flag = uniq_flag
        self.det_flag = det_flag
        self.track_flag = track_flag
        self.write_canvas_flag = write_canvas_flag
        self.last_id = 0
        self.last_cntr = []
        self.prev_frame = None
        self.resize_factor = resize_factor
        self.src_pts = None
        self.roi_flag = roi_flag
        self.roi_pts_path = roi_pts_path
        self.roi_frac = roi_frac
        self.transform_mtx = None
        self.write_csv = write_csv
        self.video_times = None
        self.gps_times = None
        self.lat_f = lat_f
        self.long_f = long_f
        self.gps_f = gps_f
        self.video_start_time = None
        self.stitcher = StitchRetainCanvas(
            nfeatures=nfeatures,
            canvas_flag=write_canvas_flag,
            reuse_prev_keypts=True,
            roi_frac=roi_frac,
            reg_threshold=reg_threshold,
            window_len=window_len,
            print_flag=print_flag,
        )
        self.fps = fps
        self.show_id = show_id
        self.show_pos = show_pos
        self.tracking_nodes = tracking_nodes
        self.nodes = nodes
        self.stash_flag = (stash_flag,)
        self.pull_flag = pull_flag
        self.y1_pos = y1_pos
        self.show_flag = show_flag
        self.relay_trigger = relay_trigger
        self.pause_dis = pause_dis
        self.app_start_time = time.time()
        self.prev_frame_time = None
        # self.stop_q = Queue(maxsize=1)
        # self.tie_q = Queue(maxsize=1000)
        # self.thread = Thread(target=self.thread_relay_call)
        # self.thread.daemon = True
        # self.thread.start()
        self.queue_frame_skip = queue_frame_skip
        self.infer_workflow = infer_workflow
        self.start_id = start_id
        print("Started thread")

        self.init_track_dict()
        if self.gps_data is not None:
            self.video_times, self.gps_times, self.latitudes, self.longitudes = self.gps_data
            self.video_start_time = self.video_times[0]

        if self.roi_flag:
            if not redraw_pts:
                self.src_pts = np.loadtxt(roi_pts_path, "float32")

        if self.det_flag:
            triton_container = check_service_available(f"{projectname}_triton", exit_flag=False)
            if triton_container is None:
                if triton_mode:
                    raise ValueError("Triton service not available")
            else:
                triton_mode = True

        if self.infer_workflow:
            self.workflow_obj = InferWorkflow(
                projectname=projectname,
                project_config_path=self.project_config_path,
                workspace=work_dir,
                ex_nodes=disabled_nodes,
                dump_results=False,
                show_flag=det_show,
                apply_filter=True,
                triton_mode=triton_mode,
                print_flag=print_flag,
                git_flag=git_flag,
                gpu_flag=gpu_flag,
                stash_flag=stash_flag,
                pull_flag=pull_flag,
            )
        else:
            self.workflow_obj = None
        # self.child_node = self.get_tracker_node_child()

        # Sample detection for queue based frame skipping
        if self.queue_frame_skip:
            sample_img = np.zeros((3000, 3000, 3), dtype=np.float32)
            self.workflow_obj.run_image(sample_img)

    def get_curr_time(self):
        curr_time = time.time()
        curr_time = curr_time - self.app_start_time

        return curr_time

    def init_track_dict(self):
        """Initialise tracker dict, csv dict, yshift tracker_dict: For storing contours, track ids on each frame csv_dict: Tie_ID,Abs_Center_Time,Frame_number,Latitude,Longitude,TLx,TLy,BRx,BRy,DFIC"""
        self.track_dict = {"max_id": self.start_id, "min_id": self.start_id, "contours_dict_list": []}
        self.csv_dict = {}
        self.y_shift = 0
        self.prev_frame = None
        self.first_frame = True
        self.prev_frame_num = None
        self.stitcher.init_stitch_vars()

    def linear_inter(self, video_time):
        """d - [[lower video time, lat/long], [upper video time, lat/long]]
        x - video time for which lat long to be calculated
        """

        lower_ind = binary_search_lower(self.video_times, video_time)
        upper_ind = binary_search_upper(self.video_times, video_time)
        lower_time = self.video_times[lower_ind]
        upper_time = self.video_times[upper_ind]

        lat_lower = self.latitudes[lower_ind]
        lat_upper = self.latitudes[upper_ind]
        long_lower = self.longitudes[lower_ind]
        long_upper = self.longitudes[upper_ind]
        gps_time_lower = self.gps_times[lower_ind]
        gps_time_upper = self.gps_times[upper_ind]

        lat_intrp = ((upper_time - video_time) * lat_lower + (video_time - lower_time) * lat_upper) / (upper_time - lower_time)
        long_intrp = ((upper_time - video_time) * long_lower + (video_time - lower_time) * long_upper) / (upper_time - lower_time)
        gps_time_intrp = ((upper_time - video_time) * gps_time_lower + (video_time - lower_time) * gps_time_upper) / (upper_time - lower_time)
        return lat_intrp, long_intrp, gps_time_intrp

    def unpack_gps_data(self, frame_num):
        """Given frame number, if available in gps data return latitude and longitude or calculate
        latitude and longitude by linear interpolation from gps data

        :param frame_num: _description_
        :type frame_num: _type_
        :return: _description_
        :rtype: _type_
        """
        video_time = self.video_start_time + frame_num / self.fps
        # video_time = math.floor(video_time * 1000) / 1000  # convert to 3 decimal place to match with input csv
        # if in cleaned data take from the gps data

        if video_time in self.video_times:
            video_ind = self.video_times.index(video_time)
            latitude = self.latitudes[video_ind]
            longitude = self.longitudes[video_ind]
            gps_time = self.gps_times[video_ind]
        # if greater or lesser than the cleaned data take from fitted data
        elif video_time > max(self.video_times) or video_time < min(self.video_times):
            latitude = float(self.lat_f(video_time))
            longitude = float(self.long_f(video_time))
            gps_time = float(self.gps_f(video_time))
        # if in between the cleaned data do a linear interpolation
        else:
            latitude, longitude, gps_time = self.linear_inter(video_time)

        return latitude, longitude, gps_time

    def get_lat_long_diff(self, frame_num):
        """Calculate latitude and longitude difference between current frame and previous frame

        :param frame_num: _description_
        :type frame_num: _type_
        :return: _description_
        :rtype: _type_
        """
        if frame_num == 0:
            latitude, longitude, gps_time = self.unpack_gps_data(frame_num + 1)
            prev_latitude, prev_longitude, prev_gps_time = self.unpack_gps_data(frame_num)

        else:
            latitude, longitude, gps_time = self.unpack_gps_data(frame_num)
            prev_latitude, prev_longitude, prev_gps_time = self.unpack_gps_data(frame_num - 1)
        diff_latitude = latitude - prev_latitude
        diff_longitude = longitude - prev_longitude
        diff_gps_time = gps_time - prev_gps_time

        return diff_latitude, diff_longitude, diff_gps_time

    def thread_relay_call(self):
        tie_dict = {}
        last_trigger_id = 0
        while True:
            if self.stop_q.qsize():
                print("Thread stopping")
                break

            # Getting from the queue and adding to dict
            for _ in range(self.tie_q.qsize()):
                output = self.tie_q.get()
                tie_id, trigger_time = output
                if tie_id is None:
                    continue
                if tie_id <= last_trigger_id:
                    continue
                tie_dict[tie_id] = trigger_time

            if len(tie_dict):
                tie_ids = list(tie_dict.keys())
                tie_ids.sort()
                new_tie_dict = {}
                # loop thru dict and check if trigger time
                for tie_id in tie_ids:
                    curr_time = self.get_curr_time()
                    trigger_time = tie_dict[tie_id]
                    if trigger_time is None:
                        continue
                    if curr_time > trigger_time:
                        print(f"Calling relay trigger {tie_id}")
                        last_trigger_id = tie_id
                    else:
                        new_tie_dict[tie_id] = trigger_time

                tie_dict = new_tie_dict
            time.sleep(0.01)

    def calc_dist_threshold(self, img, y_shift, frame_num, frame_time, y3=600):
        """Calcualting distance between tie and y3 threshold and calling relay func"""
        trigger_ids = []
        k = None
        debug_img = None
        img_ht, img_wd, _ = img.shape
        bottom_pad = y3 + 400
        y3_line = img_ht + y3
        gps_dict = {}

        try:
            time_diff = frame_time - self.prev_frame_time
            tile_velocity = abs(y_shift) / time_diff
        except:
            tile_velocity = None

        self.prev_frame_time = frame_time

        if self.show_flag:
            debug_img = img.copy()
            if y3 > 0:
                debug_img = cv2.copyMakeBorder(debug_img, top=0, bottom=bottom_pad, left=0, right=0, borderType=cv2.BORDER_CONSTANT, value=(0, 0, 0))
            debug_img = cv2.line(debug_img, (0, y3_line), (img_wd, y3_line), [0, 255, 255], thickness=3)
            debug_img = put_text(f"Frame No: {frame_num}", debug_img, debug_img.shape[1] - 30, 60, color=(0, 255, 255), font_scale=2, thickness=3, auto_align_h=True)

        # finding less than threshold
        for _, cnt_dict in enumerate(self.track_dict["contours_dict_list"]):
            tracking_node = list(cnt_dict.keys())[0]
            contour = cnt_dict[tracking_node]
            thresh_check = cnt_dict["thresh_check"]
            triggered = cnt_dict["triggered"]
            time_stamp = cnt_dict["timestamp"]
            video_time = cnt_dict["videotime"]
            real_asset_name = cnt_dict["real_asset"]
            if real_asset_name is not None:
                for id_, asset_dict in enumerate(self.track_dict["contours_dict_list"]):
                    if list(asset_dict.keys())[0] == real_asset_name:
                        break
                track_id = self.track_dict["contours_dict_list"][id_]['track_id']
            else:
                track_id = None

            x1, y1, w, h = cv2.boundingRect(np.array(contour, dtype=np.float32))
            x2 = x1 + w
            y2 = y1 + h
            tile_dist = (img_ht + y3) - y2

            if y_shift == 0:
                trigger_time = np.nan
                clock_trigger = None
            else:
                time_to_thresh = tile_dist / tile_velocity
                trigger_time = np.round(time_to_thresh, 3)
                clock_time = self.get_curr_time()
                clock_trigger = clock_time + trigger_time
            trigger_ids.append([track_id, clock_trigger])

            if self.show_flag:
                lg_x1, _ = get_xy_loc(contour, position="left_aligned", xy_shift=[debug_img.shape[1] // 27, debug_img.shape[1] // 45])
                lg_y = y2
                if not triggered:
                    cv2.rectangle(debug_img, (x1, y1), (x2, y2), [0, 255, 0], 4)
                else:
                    curr_time = time.strftime("%H:%M:%S", time_stamp)
                    cv2.rectangle(debug_img, (x1, y1), (x2, y2), [0, 0, 255], 4)

            if tile_dist > y3_line and thresh_check is True:
                if not triggered:
                    cnt_dict["triggered"] = True
                    time_stamp = time.localtime()
                    video_time = round((frame_num * (1 / self.fps)), 2)
                    # trigger_ids.append([track_id, tile_dist, time_stamp])
                    curr_time = time.strftime("%H:%M:%S", time_stamp)
                    cnt_dict["timestamp"] = time_stamp
                    cnt_dict["videotime"] = video_time
                    gps_dict['id'] = track_id
                    gps_dict['frame_num'] = frame_num
                    gps_dict['asset_name'] = real_asset_name

                    if self.show_flag:
                        cv2.rectangle(debug_img, (x1, y1), (x2, y2), [0, 0, 255], 4)

        # finding tie ids crossed the threshold
        for _, cnt_dict in enumerate(self.track_dict["contours_dict_list"]):
            tracking_node = list(cnt_dict.keys())[0]
            contour = cnt_dict[tracking_node]
            thresh_check = cnt_dict["thresh_check"]
            real_asset_name = cnt_dict["real_asset"]
            triggered = cnt_dict["triggered"]
            x1, y1, w, h = cv2.boundingRect(np.array(contour, dtype=np.float32))
            x2 = x1 + w
            y2 = y1 + h
            tile_dist = (img_ht + y3) - y2
            if real_asset_name is not None:
                for id_, asset_dict in enumerate(self.track_dict["contours_dict_list"]):
                    if list(asset_dict.keys())[0] == real_asset_name:
                        break
                track_id = self.track_dict["contours_dict_list"][id_]['track_id']
            else:
                track_id = None

            if tile_dist < 0 and thresh_check is True:
                if not triggered:
                    time_stamp = time.localtime()
                    video_time = round((frame_num * (1 / self.fps)), 2)
                    curr_time = time.strftime("%H:%M:%S", time_stamp)
                    cnt_dict["timestamp"] = time_stamp
                    cnt_dict["triggered"] = True
                    cnt_dict["videotime"] = video_time
                    gps_dict['id'] = track_id
                    gps_dict['frame_num'] = frame_num
                    gps_dict['asset_name'] = real_asset_name

                    if self.show_flag:
                        cv2.rectangle(debug_img, (x1, y1), (x2, y2), [0, 0, 255], 4)

        if self.pause_dis:
            time_var = 0
        else:
            time_var = 1

        if self.show_flag:
            k = show(debug_img, win="relay trigger", time=time_var,  window_normal=True)

        return gps_dict, k

    def insert_to_csv_dict(self, frame_num, img_ht, change_ids, y_shift):
        """For every tie, calcuate distance from centre,
        update csv dict if distance is reduced
        """
        gps_y_shift = y_shift
        tile_velocity = (gps_y_shift) / (1 / self.fps)

        for _, cnt_dict in enumerate(self.track_dict["contours_dict_list"]):
            contour = cnt_dict[self.tracking_node]
            cx, cy = np.mean(contour, axis=0).tolist()
            latitude = cnt_dict.get("latitude")
            longitude = cnt_dict.get("longitude")
            gps_t = cnt_dict.get("gps_t")

            tile_dist = cy - img_ht // 2
            if y_shift == 0:
                abs_centre_time = np.nan
            else:
                time_to_centre = tile_dist / tile_velocity
                abs_centre_time = (frame_num * (1 / self.fps)) + time_to_centre
                abs_centre_time = np.round(abs_centre_time, 3)

            track_id = cnt_dict["track_id"]

            x1, y1, w, h = cv2.boundingRect(contour)
            x2 = x1 + w
            y2 = y1 + h

            if self.csv_dict.get(str(track_id)) is None:
                self.csv_dict[str(track_id)] = [
                    gps_t,
                    abs_centre_time,
                    frame_num,
                    latitude,
                    longitude,
                    x1,
                    y1,
                    x2,
                    y2,
                    int(tile_dist),
                ]

            elif abs(tile_dist) < self.csv_dict[str(track_id)][-1]:
                self.csv_dict[str(track_id)] = [
                    gps_t,
                    abs_centre_time,
                    frame_num,
                    latitude,
                    longitude,
                    x1,
                    y1,
                    x2,
                    y2,
                    int(tile_dist),
                ]

        for src_id, dst_id in change_ids:
            self.csv_dict[str(src_id)], self.csv_dict[str(dst_id)] = (
                self.csv_dict[str(dst_id)],
                self.csv_dict[str(src_id)],
            )

    def get_lat_long(self, contour, y_shift, frame_num, img_height):
        """Calculate latitude and longitude for a contour position"""
        img_center_pos = img_height // 2
        lat, long, gps_t = None, None, None
        latitude, longitude, gps_time = self.unpack_gps_data(frame_num)

        diff_latitude, diff_longitude, diff_gps_time = self.get_lat_long_diff(frame_num)
        if y_shift == 0:
            lat = latitude
            long = longitude
            gps_t = gps_time
        else:
            gps_y_shift = y_shift
            cx, cy = np.mean(contour, axis=0).tolist()
            lat = latitude + (cy - img_center_pos) * (diff_latitude / gps_y_shift)
            long = longitude + (cy - img_center_pos) * (diff_longitude / gps_y_shift)
            gps_t = gps_time + (cy - img_center_pos) * (diff_gps_time / gps_y_shift)

        return lat, long, gps_t

    def insert_to_track_dict(self, contours_dict, tracking_node, img_height, img_width, frame_num=None, y_shift=None):
        """insert a contour from a dictionary of contours into the tracking dictionary.

        Parameters:
        - self (object): Instance of the class that holds the current tracking information.
        - contours_dict (dict): Dictionary of contours, where the keys are the contour names, and the values are the contour points.
        - img_height (int): Height of the image from which the contours are extracted.
        - img_width (int): Width of the image from which the contours are extracted.
        - frame_num (int, optional): The frame number for which the contour is being inserted. Defaults to None.
        - y_shift (int, optional): Shift in the y-direction of the contour. Defaults to None.

        Returns:
        None. The function updates the tracking dictionary by adding a new entry with the given contour and its related information.

        """

        contour = contours_dict[tracking_node]
        thresh_check = contours_dict["threshold_check"]
        real_asset_name = contours_dict["real_asset"]
        track_ids = [i["track_id"] for i in self.track_dict["contours_dict_list"] if i["track_id"] is not None]

        # up count False, y shift + ve : track_id = max_id # False, True = True
        # up count False, y shift - ve : track_id = min_id # False, False = False
        # up count True, y shift + ve : track_id = min_id # True, True = False
        # up count True, y shift - ve : track_id = max_id # True, False = True

        # TO-DO Mention each case seperately wiith comments
        if len(track_ids) <= 0:
            max_id = self.track_dict["max_id"]
            min_id = self.track_dict["min_id"]
        else:
            max_id = max(track_ids)
            min_id = min(track_ids)

        if self.first_frame:
            if self.count_up is False:
                y_ = y_shift >= 0
            else:
                y_ = y_shift > 0
            if y_ ^ self.count_up:
                track_id = max_id + 1
            else:
                track_id = min_id - 1
        else:
            if len(track_ids):
                if self.cam_direction == "Up_Down":
                    if self.count_up:
                        if contour[:, 1].min() < img_height // 2:
                            track_id = max_id + 1
                        else:
                            track_id = min_id - 1
                    else:
                        if contour[:, 1].min() < img_height // 2:
                            track_id = min_id - 1
                        else:
                            track_id = max_id + 1
                elif self.cam_direction == "Down":
                    track_id = max_id + 1
            else:
                if self.count_up:
                    track_id = max_id + 1
                else:
                    track_id = max_id

        if thresh_check:
            track_id = None

        if self.print_flag:
            print_colored(f"Id {track_id} added", "green")

        if track_id is not None:
            if self.track_dict["max_id"] < track_id:
                self.track_dict["max_id"] = track_id
            if self.track_dict["min_id"] > track_id:
                self.track_dict["min_id"] = track_id

        # TO-DO Handle multiple child nodes
        shape_dict = {
            tracking_node: contour,
            # self.child_node: contours_dict.get(self.child_node, []),
            "match_count": 0,
            "match_flag": False,
            "track_id": track_id,
            "triggered": False,
            "timestamp": None,
            "videotime":None,
            "thresh_check": thresh_check,
            "real_asset": real_asset_name
        }

        self.track_dict["contours_dict_list"].append(shape_dict)

    def reorder_history(self):
        """Reorder history dict"""

        self.track_dict["contours_dict_list"] = sorted(
            self.track_dict["contours_dict_list"],
            key=lambda k: list(k.values())[0][:, 1].min(),
        )

        track_ids = [i["track_id"] for i in self.track_dict["contours_dict_list"] if i["track_id"] is not None]

        sorted_track_ids = sorted(track_ids, reverse=self.count_up)
        track_changed_list = np.where(track_ids != sorted_track_ids)[0].tolist()
        change_ids = []
        for index in track_changed_list:
            change_ids.append([track_ids[index], sorted_track_ids[index]])

        if len(change_ids):  # Handling numbering issue (Maybe delayed prediction)
            for i, _ in enumerate(self.track_dict["contours_dict_list"]):
                self.track_dict["contours_dict_list"][i]["track_id"] = sorted_track_ids[i]
        return change_ids

    def update_contours(
        self,
        img,
        curr_contours: list,
        y_shift: int,
        img_height: int,
        img_width: int,
        frame_num=None,
    ) -> None:
        """Method to update contours in self.track_dict. Procedure is:
        - Shift tracked contours by y_shift.
        - Check overlap of these shifted tracked contours with present detected contours.
        - If overlap, mark both of these contours as non-new contours and replace track contours with current contour. track_id remains same.
        - If no overlap, then this contour is new and add this contour to track_dict by giving it new track_id.
        - If track_cntr doesn't matches with current contours, then this contours is shifted and track_id remains same.

        :param img: _description_
        :param curr_contours: List of dicts current contours based on detection.
                                Format: [
                                    {'tracker_node':[], 'child_node':[]},
                                    {'tracker_node':[], 'child_node':[]},
                                    ]
        :param y_shift: y-shift between the previous frame and current frame.
        :param img_height: Current frame height.
        :param img_width: Current frame width.
        :param frame_num: _description_, defaults to None
        """

        # Sort contours based on min y-point
        curr_contours = sorted(curr_contours, key=lambda x: list(x.values())[0][:, 1].min())

        # History shifting
        for track_ind, track_dict in enumerate(self.track_dict["contours_dict_list"]):
            tracking_node = list(track_dict.keys())[0]
            track_cntr = track_dict[tracking_node]
            shifted_cntr = translate_points(track_cntr, 0, -y_shift)
            self.track_dict["contours_dict_list"][track_ind][tracking_node] = np.array(shifted_cntr)
            # child_cntrs = track_dict[self.child_node]
            # if len(child_cntrs):
            #     shifted_cntrs = [translate_points(child_cntr, 0, -y_shift) for child_cntr in child_cntrs]
            #     shifted_cntrs = [np.array(cntr, dtype="int") for cntr in shifted_cntrs]
            #     self.track_dict["contours_dict_list"][track_ind][self.child_node] = shifted_cntrs

        tracked_contours_idx = [True for _ in range(len(self.track_dict["contours_dict_list"]))]
        new_contours_idx = [True for _ in range(len(curr_contours))]

        if self.print_flag:
            print(
                "Trackids: ",
                [i["track_id"] for i in self.track_dict["contours_dict_list"]],
            )
            print("curr cntrs: ", len(curr_contours))

        # Resetting all match flags
        for cnt_dict in self.track_dict["contours_dict_list"]:
            cnt_dict["match_flag"] = False

        for i, cntr_dict in enumerate(curr_contours):
            match_indices = []
            cntr1_node = list(cntr_dict.keys())[0]
            cntr1 = cntr_dict[cntr1_node]
            thresh_check = cntr_dict['threshold_check']
            if not thresh_check: # if real assets
                for j, cntr_dict2 in enumerate(self.track_dict["contours_dict_list"]):
                    cntr2_node = list(cntr_dict2.keys())[0]
                    if cntr1_node != cntr2_node:
                        continue
                    cntr2 = cntr_dict2[cntr2_node]
                    overlap_ht = get_overlap_area(cntr1, cntr2)
                    # print('\t', '*** Overlap bw curr {} and hist {}: {} ***'.format(i, cntr_dict2['track_id'], overlap_ht), '\n')
                    if overlap_ht > self.overlap_threshold:
                        match_indices.append([i, j, overlap_ht])

                if match_indices:  # TO-DO testcase: two ties at similar height having 2 different ids
                    curr_ind, best_index, _ = max(filter(lambda a: max(a), match_indices), key=itemgetter(2))
                    self.track_dict["contours_dict_list"][best_index]["match_flag"] = True
                    self.track_dict["contours_dict_list"][best_index]["match_count"] += 1
                    tracked_contours_idx[best_index] = False
                    self.track_dict["contours_dict_list"][best_index][cntr1_node] = curr_contours[curr_ind][cntr1_node]
                    # self.track_dict["contours_dict_list"][best_index][self.child_node] = curr_contours[curr_ind].get(self.child_node, [])
                    new_contours_idx[curr_ind] = False

            else: # if psuedo box
                for j, cntr_dict2 in enumerate(self.track_dict["contours_dict_list"]):
                    cntr2_node = list(cntr_dict2.keys())[0]
                    if cntr1_node != cntr2_node:
                        continue
                    self.track_dict["contours_dict_list"][j][cntr1_node] = curr_contours[i][cntr1_node]
                    new_contours_idx[i] = False

        # logging.info(f"Found {len(np.where(new_contours_idx)[0])} new contours and {len(np.where(tracked_contours_idx)[0])} same contours.")
        # Add new contours to track_dict
        if True in new_contours_idx:
            new_cntrs_idx = np.where(new_contours_idx)[0]
            for new_cntr_idx in new_cntrs_idx:
                tracker_node = list(curr_contours[new_cntr_idx].keys())[0]
                self.insert_to_track_dict(curr_contours[new_cntr_idx], tracker_node, img_height, img_width, frame_num=frame_num, y_shift=y_shift)

        # if self.gps_data is not None and (self.show_pos or self.write_csv or self.cluster_mode != "non_cluster"):
        #     for tracked_ind, cnt_dict in enumerate(self.track_dict["contours_dict_list"]):
        #         contour = cnt_dict[self.tracking_node]
        #         latitude, longitude, gps_t = self.get_lat_long(contour, y_shift, frame_num, img_height)
        #         self.track_dict["contours_dict_list"][tracked_ind]["latitude"] = latitude
        #         self.track_dict["contours_dict_list"][tracked_ind]["longitude"] = longitude
        #         self.track_dict["contours_dict_list"][tracked_ind]["gps_t"] = gps_t

        if self.history_cleanup:
            # Check tracked contours inside image boundary, If True, keep it, else delete it
            new_cntrs_dict_list = []
            if self.relay_trigger:
                cleanup_thresh = self.y1_pos + 300
                img_roi = np.array([[0, 0], [img_width, 0], [img_width, img_height + cleanup_thresh], [0, img_height + cleanup_thresh]])
            else:
                img_roi = np.array([[0, 0], [img_width, 0], [img_width, img_height], [0, img_height]])
            for tracked_ind, cnt_dict in enumerate(self.track_dict["contours_dict_list"]):
                tracking_node = list(cnt_dict.keys())[0]
                contour = cnt_dict[tracking_node]
                overlap_area = get_overlap_area(contour, img_roi)

                if overlap_area > 0:
                    new_cntrs_dict_list.append(cnt_dict)
                else:
                    if self.print_flag:
                        print(f'Deleting {cnt_dict["track_id"]}')
            self.track_dict["contours_dict_list"] = new_cntrs_dict_list
        # change_ids = self.reorder_history()

        # if self.cluster_mode != "non_cluster" and frame_num is not None or self.write_csv and self.gps_data is not None and frame_num is not None:
        #     self.insert_to_csv_dict(frame_num, img_height, change_ids, y_shift)
        self.prev_frame_num = frame_num

    def get_track_cntrs_list(self, result_dict):
        """Get tracker node contours from result json, keep child contours if any
        Format: [{'A2_RSSI_tie':[tie_cnt1], 'A3_RSSI_crack':[crack1, crack2, ..]},
        {'A2_RSSI_tie':[tie_cnt2], 'A3_RSSI_crack':[]},]

        :param result_dict: _description_
        :type result_dict: _type_
        :return: _description_
        :rtype: _type_
        """
        # TO-DO avoid list for tracker node, handle multiple children
        tracker_list = []
        for node in self.tracking_nodes:
            node_dict = result_dict.get(node)
            if node_dict is None:
                continue
            tracker_cntrs = node_dict.get("contours")
            thresh_check = node_dict.get("threshold_check")
            real_asset = node_dict.get("real_asset")

            if not len(tracker_cntrs):
                continue
            for trk_cntr in tracker_cntrs:
                tracker_dict = {node: np.array(trk_cntr, dtype="int"), "threshold_check": thresh_check, "real_asset": real_asset}
                tracker_list.append(tracker_dict)

        return tracker_list

    def get_tracker_node_child(self):
        """Get child node of tracker node

        :return: _description_
        :rtype: _type_
        """
        child_nodes = []
        if self.workflow_obj is None:
            return None
        for ind, node in enumerate(self.nodes):
            if node == self.tracking_node:
                continue
            # It's a child of tracker node
            if self.workflow_obj.pix_objs[node].node_config_obj("parent_contour") == self.tracking_node:
                # if self.workflow_obj.pix_objs[node]["inf"].node_config("parent_contour") == self.tracking_node:
                child_nodes.append(node)
        if child_nodes:  # TO-DO Handle multiple chile nodes
            child_node = child_nodes[0]
        else:
            child_node = None
        return child_node

    def convert_labelme_json_to_dict(self, json_dict):
        """Return a dictinary having keys as labels, contours as values"""
        shape_list = json_dict["shapes"]
        result_dict = {}
        for shape_dict in shape_list:
            label = shape_dict["label"]
            contours = shape_dict["points"]
            if not len(contours):
                continue
            if result_dict.get(label):
                result_dict[label]["contours"].append(contours)
            else:
                result_dict[label] = {}
                result_dict[label]["contours"] = [contours]
                result_dict[label]["threshold_check"] = False
                result_dict[label]["real_asset"] = None
                result_dict[label]["position"] = None

            if len(shape_dict['intersection_pt']):
                for inter, pt in shape_dict['intersection_pt'].items():
                    x1 = pt[0] - 200
                    y1 = pt[1] - 50
                    x2 = pt[0] + 200
                    y2 = pt[1]
                    cntr = [[[x1, y1], [x2, y1], [x2, y2], [x1, y2]]]
                    result_dict[f"{label}_{inter}_pseudo"] = {}
                    result_dict[f"{label}_{inter}_pseudo"]["contours"] = cntr
                    result_dict[f"{label}_{inter}_pseudo"]["threshold_check"] = True
                    result_dict[f"{label}_{inter}_pseudo"]["real_asset"] = label
                    result_dict[f"{label}_{inter}_pseudo"]["position"] = inter

        return result_dict

    def filter_contours(self, json_dict, img, filter_thres=0.2):
        """Method to filter contours on the top portion""" 
        shape_list = json_dict["shapes"]
        img_ht, _, _ = img.shape
        rem_ind = []
        for num, shape_dict in enumerate(shape_list):
            contour = shape_dict["points"]
            x1, y1, w, h = cv2.boundingRect(np.array(contour, dtype=np.float32))
            x2 = x1 + w
            y2 = y1 + h

            if y2 > img_ht - (img_ht * filter_thres):
                rem_ind.append(num)

        for ind in rem_ind:
            del json_dict["shapes"][ind]

        return json_dict

    def run_seq(self, img: np.ndarray, frame_time, frame_num=None, y_shift_q=None, json_dict=None) -> None:
        """Method to run stitch-det-track sequentially.

        :param img: Input image to be stitched.
        :type img: np.ndarray
        :param frame_num: _description_, defaults to None
        :type frame_num: _type_, optional
        :param y_shift_q: _description_, defaults to None
        :type y_shift_q: _type_, optional
        """
        k = -1
        relay_img = None
        t1 = time.time()
        if self.roi_flag:
            img, _, json, self.transform_mtx = transform_crop(
                image=img,
                crop_cntr=self.src_pts,
                # save_path=self.roi_pts_path,
                pad_l=20,
                pad_r=20,
                tr=self.transform_mtx,
            )
        if self.resize_factor != -1:
            img = cv2.resize(
                (
                    int(img.shape[1] * self.resize_factor),
                    int(img.shape[0] * self.resize_factor),
                ),
                img,
            )
        
        #cv2.imwrite(str(frame_num) + '.png', img)
        # Stitch
        y_shift, sum_y_shift, _ = self.stitcher.stitch(img, y_shift_q)
        if frame_num < 3:
            uniq_flag = True
        else:
            uniq_flag = self.uniq_iden.check_unique(sum_y_shift)
        t_stitch = time.time() - t1
        if self.print_flag:
            print(f"Time stitch and unique: {t_stitch}")
        if uniq_flag is False:
            print(f"Skipping detection for Frame num: {frame_num} \n")
        else:
            print(f"\n Detecting for frame number: {frame_num}")
        # If y_shift > uniq_iden threshold
        if uniq_flag or not isinstance(self.prev_frame, np.ndarray):
            t2 = time.time()
            # adding threshold
            # Detection
            if self.workflow_obj is not None and json_dict is None:
                overlay_img, json_dict = self.workflow_obj.run_image(img)
            # if self.relay_trigger:
            #     json_dict = self.filter_contours(json_dict, img)
            t_workflow = time.time() - t2
            if self.print_flag:
                print(f"Time workflow: {t_workflow}")
            t2 = time.time()
            result_dict = self.convert_labelme_json_to_dict(json_dict)
            track_dict_list = self.get_track_cntrs_list(result_dict)
            # Track
            self.update_contours(img, track_dict_list, y_shift, img.shape[0], img.shape[1], frame_num=frame_num)
            if self.print_flag:
                print(f"Time update contours: {time.time() - t2}")
        
        else:  # Shift contours in track_dict by y_shift
            for i, cntr_dict in enumerate(self.track_dict["contours_dict_list"]):
                tracking_node = list(cnt_dict.keys())[0]
                self.track_dict["contours_dict_list"][i][tracking_node] = np.array(translate_points(cntr_dict[tracking_node], 0, -y_shift))
                # child_cntrs = cntr_dict[self.child_node]
                # if len(child_cntrs):
                #     shifted_cntrs = [translate_points(child_cntr, 0, -1 * y_shift) for child_cntr in child_cntrs]
                #     shifted_cntrs = [np.array(cntr, dtype="int") for cntr in shifted_cntrs]
                #     self.track_dict["contours_dict_list"][i][self.child_node] = shifted_cntrs
            # print(f'Time shifting contours: {t_shift_cntrs}')
        if self.relay_trigger:
            gps_dict, k = self.calc_dist_threshold(img, y_shift, frame_num, frame_time, self.y1_pos)
        self.prev_frame = img
        self.first_frame = False
        self.y_shift = y_shift

        return gps_dict, k


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-roi",
        "--select_roi",
        default=False,
        nargs="?",
        const=True,
        help="Whether to draw points or take from video dir",
    )
    parser.add_argument(
        "-w",
        "--write_video",
        default=True,
        nargs="?",
        const=False,
        help="Whether to write video to results directory",
    )
    parser.add_argument(
        "-s",
        "--play_video",
        default=False,
        nargs="?",
        const=True,
        help="Whether to show frames",
    )
    parser.add_argument(
        "-c",
        "--canvas_flag",
        default=True,
        nargs="?",
        const=True,
        help="Whether to enable canvas stitching and write canvas.",
    )
    parser.add_argument(
        "-dur",
        "--duration",
        type=int,
        default=1,
        help="Duration for which the application to be run",
    )
    parser = parser.parse_args()
    roi_flag = parser.select_roi
    write_video = parser.write_video
    show_flag = parser.play_video
    canvas_flag = parser.canvas_flag
    duration = parser.duration

    # Clone DB, weight
    from ignutils.video_utils.video_reader import VideoReader

    CloneRepo("https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db_dummy.git", "herzog_short_vid", "herzog_short_vid", access_token_name="DB_CLONE_TOKEN")
    VIDEO_PATH = "herzog_short_vid/blend_sample/blend_sample.mp4"
    reader = VideoReader(VIDEO_PATH)
    fps = reader.fps
    total_frames = reader.frame_count
    print("Total frames:", total_frames)

    stit_det_tr_obj = StitchDetTrackSeq(
        threshold=0,
        projectname="herzog",
        project_config_path=None,
        nodes=["herzog_blend_tile"],
        tracking_node="A2_tile",
        stitch_flag=True,
        uniq_flag=True,
        det_flag=True,
        track_flag=True,
        write_canvas_flag=True,
        roi_frac=(0.5, 0, 0.75, 1),
    )
    track_node = stit_det_tr_obj.tracking_node
    sum_y_shift_list, merged_cntrs_list = [], []
    RESULT_VIDEO = None
    if show_flag:
        cv2.namedWindow("Prediction", cv2.WINDOW_GUI_NORMAL)

    t_start = time.time()
    if duration is None:
        num_imgs = total_frames
    else:
        num_imgs = int(duration * fps)

    for i in range(num_imgs):
        t1 = time.time()
        frame, _, frame_num = reader.read()
        t_read_img = time.time() - t1
        stit_det_tr_obj.run_seq(frame)
        t_run_seq = time.time() - t1 - t_read_img

        cntrs_list = [cntr_dict[track_node] for cntr_dict in stit_det_tr_obj.track_dict["contours_dict_list"]]
        cv2.drawContours(stit_det_tr_obj.prev_frame, cntrs_list, -1, (0, 255, 0), 3)

        for cntr_dict in stit_det_tr_obj.track_dict["contours_dict_list"]:
            cntr = cntr_dict[track_node]
            cntr_id = cntr_dict["track_id"]

        if show_flag:
            cv2.imshow("Prediction", stit_det_tr_obj.prev_frame)
            cv2.waitKey(1)

        if write_video:
            RESULT_VIDEO = (
                cv2.VideoWriter(
                    "../results/stitch_det_track_seq.mp4",
                    cv2.VideoWriter_fourcc(*"mp4v"),
                    5.0,
                    (
                        stit_det_tr_obj.prev_frame.shape[1],
                        stit_det_tr_obj.prev_frame.shape[0],
                    ),
                )
                if not RESULT_VIDEO
                else RESULT_VIDEO
            )
            RESULT_VIDEO.write(stit_det_tr_obj.prev_frame)

        print(f"---> Read image time = {t_read_img}")
        print(f"---> Run seq time = {t_run_seq}")

    t_end = time.time()
    fps = num_imgs / (t_end - t_start)
    if show_flag:
        cv2.destroyAllWindows()
    if write_video:
        RESULT_VIDEO.release()
    if canvas_flag:
        cv2.imwrite(
            "../results/stitch_det_track_seq_canvas.jpg",
            stit_det_tr_obj.stitcher.canvas,
        )
    NUM_CNTRS = stit_det_tr_obj.track_dict["max_id"]
    print(f"LR_Stitcher stitch-det-track-seq FPS = {fps:.3f}")
    print(f"Found {NUM_CNTRS} contours in input.")
    assert fps > 0.5, f"LR_Stitcher stitch-det-track-seq FPS is {fps}"