"""mono VO"""
import argparse
import os.path as osp
import cv2
import numpy as np
import pandas as pd
import unittest

from ignutils.vo.mono_vo.feature_det import featureDet
from ignutils.vo.mono_vo.find_match import keypoint_register_match, knn_match, optical_flow_match, ransac_based_match

from ignutils.clone_utils import CloneRepo
from ignutils.geom_utils import euclidean
from ignutils.show_utils import show
from ignutils.video_utils.video_reader import VideoReader
from ignutils.video_utils.video_writer import VideoWriter
from ignutils.vo.mono_vo.Visualization import plot_ground_truth, plot_trajectory, plot_trajectory_o3d
from optimizer import PoseGraph
# from ignutils.vo.mono_vo.test import PoseGraph
from utils import getTransform, convert_to_4_by_4, convert_to_Rt


class MONO_VO:
    """MONO_VO class"""

    def __init__(
        self,
        K=None,
        dist=None,
        gt_path=None,
        FeatureMethod="FAST",
        good_count_thresh_fraction=100,
        kp_count_thresh=1000,
        recompute_frame_thresh=1,
        min_move=1,
        match_method="optical_flow_based",
        show_flag=True,
        show_canvas=True,
        optimize=True,
        mulit_edge = False
    ):
        """### Visual Odometry class constructor ###
        K               : Camera calibration matrix
        dist            : Distortion coefficients
        gt_path         : GT pose file path
        FeatureMethod   : feature detection method (FAST, SIFT, SURF)
        good_count_thresh_fraction    : minimum Key points count
        kp_count_thresh   : minimum feature count for re running feature detection
        show_flag       : Enable Show
        show_canvas     : plot pose on a canvas

        """

        self.K = None
        self.dist = dist
        self.GT = None
        self.t_curr = np.zeros((3, 1))
        self.R_curr = np.eye(3)
        self.canvas = None
        self.good_count_thresh = 600
        self.valid_kp0 = None
        self.valid_img0 = None
        self.min_good_count = 100
        self.good_count_thresh_fraction = good_count_thresh_fraction
        self.FeatureMethod = FeatureMethod
        self.recompute_frame_thresh = recompute_frame_thresh
        self.first_frame = True
        self.first_pair = True
        self.re_compute_count = 0
        self.show_flag = show_flag
        self.match_method = match_method
        self.kp_count_thresh = kp_count_thresh
        self.min_move = min_move
        self.show_canvas = show_canvas
        self.feat_det = featureDet(self.FeatureMethod)
        self.Xold = None
        self.poses = []
        self.window = 10
        self.optimize = optimize
        self.num_iter = 100
        self.multi_edge = mulit_edge

        if K is None:
            K = np.array(
                [
                    [7.188560000000e02, 0.000000000000e00, 6.071928000000e02],
                    [0.000000000000e00, 7.188560000000e02, 1.852157000000e02],
                    [0.000000000000e00, 0.000000000000e00, 1.000000000000e00],
                ]
            )

        if gt_path is not None and osp.isfile(gt_path):
            self.GT = np.loadtxt(gt_path)

        if self.show_canvas:
            self.canvas = np.zeros((700, 1000, 3), dtype=np.uint8)

        self.K = K

        print("\t", "K            : ", *self.K)
        print("\t", "FeatureMethod: ", FeatureMethod)
        print("\t", "GT Path      : ", gt_path)
        print("\t", "good_count_thresh_fraction : ", good_count_thresh_fraction)
        print("\t", "feat_Thresh  : ", self.kp_count_thresh)
        print("\t", "show_pose    : ", self.show_canvas)

    def AbsoluteScale(self, last_id, curr_id):
        """Find absolute scale"""
        x_prev = self.GT[last_id, 3]
        y_prev = self.GT[last_id, 7]
        z_prev = self.GT[last_id, 11]

        x = self.GT[curr_id, 3]
        y = self.GT[curr_id, 7]
        z = self.GT[curr_id, 11]
        Enorm = np.sqrt((x - x_prev) ** 2 + (y - y_prev) ** 2 + (z - z_prev) ** 2)
        return Enorm

    def RelativeScale(self, last_cloud, new_cloud):
        """Find relative scale"""
        min_idx = min([new_cloud.shape[0], last_cloud.shape[0]])
        p_Xk = new_cloud[:min_idx]
        Xk = np.roll(p_Xk, shift=-3)
        p_Xk_1 = last_cloud[:min_idx]
        Xk_1 = np.roll(p_Xk_1, shift=-3)
        d_ratio = (np.linalg.norm(p_Xk_1 - Xk_1, axis=-1)) / (np.linalg.norm(p_Xk - Xk, axis=-1))

        return np.median(d_ratio)

    def Triangulation(self, R, t, kp0, kp1, K):
        "Traingulate points"
        P0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
        P0 = K.dot(P0)
        P1 = np.hstack((R, t))
        P1 = K.dot(P1)
        points1 = kp0.reshape(2, -1)
        points2 = kp1.reshape(2, -1)
        cloud = cv2.triangulatePoints(P0, P1, points1, points2).reshape(-1, 4)[:, :3]
        return cloud

    def get_error(self, index):
        """Get error in pose estimation"""
        error = None
        if self.GT is not None:
            gt_X = self.GT[index - 1, 3]
            gt_Y = self.GT[index - 1, 11]
            pr_X = self.t_curr[0][0]
            pr_Y = self.t_curr[2][0]
            error = euclidean((gt_X, gt_Y), (pr_X, pr_Y))
        return error
    
    
    def run_optimizer_multi_edge(self, local_window=10):

        """
        Add poses to the optimizer graph multi node
        """
        if len(self.poses)<local_window+1:
            return False, 0

        self.pose_graph = PoseGraph(verbose = True)
        local_poses = self.poses[1:][-local_window:]

        for i in range(4,len(local_poses)):   
            self.pose_graph.add_vertex(i, local_poses[i])
            self.pose_graph.add_vertex(i-1, local_poses[i-1])
            self.pose_graph.add_vertex(i-2, local_poses[i-2])
            self.pose_graph.add_vertex(i-3, local_poses[i-3])
            self.pose_graph.add_edge((i-1, i), getTransform(local_poses[i], local_poses[i-1]))
            self.pose_graph.add_edge((i-2, i-1), getTransform(local_poses[i-1], local_poses[i-2]))
            self.pose_graph.add_edge((i-3, i-2), getTransform(local_poses[i-2], local_poses[i-3]))
            self.pose_graph.add_edge((i-4, i-3), getTransform(local_poses[i-3], local_poses[i-4]))
            flag, RT = self.pose_graph.optimize(self.num_iter)
        if flag == True:
            self.t_curr = RT[0:3,-1].reshape(3,1)
            self.R_curr = RT[0:3,0:3]

        self.poses[-local_window+1:] = self.pose_graph.nodes_optimized
    
    def run_optimizer(self, local_window=10):

        """
        Add poses to the optimizer graph
        """

        if len(self.poses)<local_window+1:
            return False, 0

        self.pose_graph = PoseGraph(verbose = True)
        local_poses = self.poses[1:][-local_window:]

        for i in range(1,len(local_poses)):   
            self.pose_graph.add_vertex(i, local_poses[i])
            self.pose_graph.add_edge((i-1, i), getTransform(local_poses[i], local_poses[i-1]))
            flag, RT = self.pose_graph.optimize(self.num_iter)
        if flag == True:
            self.t_curr = RT[0:3,-1].reshape(3,1)
            self.R_curr = RT[0:3,0:3]

        self.poses[-local_window+1:] = self.pose_graph.nodes_optimized
    
    
    def extract_RT(self, kp0, kp1, frame_num):
        "Generate R and T"
        E, mask = cv2.findEssentialMat(
            kp1,
            kp0,
            self.K,
            method=cv2.RANSAC,
            prob=0.999,
            threshold=0.4,
            mask=None,
        )
        if mask is None or E.size != 9:
            print("MASK NONE")
            return None, None
        kp0 = kp0[mask.ravel() == 1]

        kp1 = kp1[mask.ravel() == 1]
        self.kp0 = kp0
        # t vecs is a unit vec, mulitply with magnitude to get actual translation
        _, R0, t0, mask = cv2.recoverPose(E, kp0, kp1, self.K)

        

        if self.first_pair:
            self.first_pair = False
            self.cur_Rt = convert_to_Rt(R0, t0)
            self.poses.append(convert_to_4_by_4(self.cur_Rt))
        Xnew = self.Triangulation(R0, t0, kp0, kp1, self.K)
        if self.Xold is None:
            self.Xold = Xnew
        if self.GT is not None:
            scale = -self.AbsoluteScale(frame_num - 1, frame_num)
        else:
            scale = -self.RelativeScale(self.Xold, Xnew)

        self.t_curr = self.t_curr + scale * self.R_curr.dot(t0)
        self.R_curr = self.R_curr.dot(R0)
        
        self.cur_Rt = convert_to_Rt(self.R_curr, self.t_curr)
        self.poses.append(convert_to_4_by_4(self.cur_Rt))

        if self.optimize:
            # self.run_optimizer(self.window)
            if self.multi_edge == False:
                self.run_optimizer(self.window)
            else:
                self.run_optimizer_multi_edge(self.window)
            # breakpoint()

        self.Xold = Xnew
        print("t_curr: ", *self.t_curr)
        print("r_curr", self.R_curr)
        print("")

        return self.t_curr, self.R_curr

    def find_match(self, img0, img1, kp0, show_flag=False, match_method=None, K=None):
        "generate match based on the given match method"
        img1_copy = img1.copy()
        img0gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
        img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        if match_method == "optical_flow_based":
            kp0, kp1, diff, good_count = optical_flow_match(img0gray, img1gray, img1_copy, kp0, show_flag=self.show_flag)
        elif match_method == "ransac_based":
            kp0, kp1, diff, good_count = ransac_based_match(img0, img1, K)
        elif match_method == "keypoint_register_based":
            kp0, kp1, diff, good_count = keypoint_register_match(kp0, img1gray, img0gray)
        elif match_method == "knn_filter_based":
            image_pair = [img0, img1]
            kp0, kp1, diff, good_count = knn_match(image_pair)
        elif match_method == "superglue_based":
            kp0, kp1, diff, good_count = superglue_based_match(img1, img0)
        return kp0, kp1, diff, good_count

    def run(self, img1, frame_num):
        print("frame_num: ", frame_num)
        h, w = img1.shape[:2]
        img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        scale = None

        if self.first_frame:
            self.img0gray = img1gray.copy()
            self.img0 = img1.copy()
            self.kp0 = self.feat_det.FeatureDetection(self.img0gray)
            self.kp1 = self.kp0
            self.valid_kp0 = self.kp0
            self.valid_img0 = self.img0gray
            self.first_frame = False
            self.prev_Rt = np.eye(4) 
            self.poses.append(self.prev_Rt)
            return None, None

        # Feature Matching
        kp0, kp1, diff, good_count = self.find_match(self.img0, img1, self.kp0, show_flag=self.show_flag, match_method=self.match_method, K=self.K)

        self.good_count_thresh = max((self.good_count_thresh_fraction / 100) * good_count, self.min_good_count)
        print("DIFF: ", diff)
        print("kp0, kp1", len(kp0), len(kp1))
        print("good_count: ", good_count)
        print("new threshold", self.good_count_thresh)

        if good_count < int(self.good_count_thresh) or self.re_compute_count > self.recompute_frame_thresh:
            print("Recalculating feat det")
            kp0 = self.feat_det.FeatureDetection(self.img0gray)
            kp0, kp1, diff, good_count = self.find_match(self.img0, img1, kp0, show_flag=self.show_flag, match_method=self.match_method, K=self.K)
            self.re_compute_count = 0
            print("******After cleanup************", len(kp0))
            print("kp0, kp1", len(kp0), len(kp1))
            print("good_count: ", good_count)
            self.good_count_thresh = max((self.good_count_thresh_fraction / 100) * good_count, self.min_good_count)
            print("new threshold", self.good_count_thresh)
        if diff < self.min_move or good_count < int(self.good_count_thresh):
            if diff < self.min_move:
                print("Skipping,  diff less than threshold", diff, self.min_move)
            else:
                print("Skipping,  good count less than threshold")
            self.img0 = img1
            self.img0gray = img1gray
            self.kp0 = kp1
            return self.t_curr, self.R_curr

        self.t_curr, self.R_curr = self.extract_RT(kp0, kp1, frame_num)
        if kp0.shape[0] < self.kp_count_thresh:
            print("After cleanup Recalculating feat det from end", kp0.shape[0])
            kp1 = self.feat_det.FeatureDetection(img1gray)

        self.img0gray = img1gray
        self.img0 = img1
        self.valid_kp0 = kp1
        self.valid_img0 = img1gray.copy()
        self.kp0 = kp1
        return self.t_curr, self.R_curr


class TestMonoVO(unittest.TestCase):
    """Test for Mono VO"""

    def test_monovo(self):

        VO = MONO_VO(show_flag=False, show_canvas=False)

        file_path = "samples/mono_vo_test/test.LRV"
        
        reader_obj = VideoReader(file_path)
        count = reader_obj.total_frame_count
        processed_frame_count = 0

        canvas = np.zeros((700, 1000, 3), dtype=np.uint8)
        outputfile = "samples/test_results/mono_vo_out.mp4"
        write_in_obj = VideoWriter(outputfile, reader_obj.fps, use_ffmpeg=True)
        # write_in_obj = None

        run_flag = False

        while processed_frame_count < count:
            frame, _, framenum, trans_mat, _ = reader_obj.get_frame(processed_frame_count)
            if framenum > 47:
                run_flag = True
            frame_height, frame_width, _ = frame.shape

            # write_in_obj = VideoWriter(outputfile, reader_obj.fps, use_ffmpeg=True)

            # write_in_obj.write_frame(canvas)

            if 1:  # run_flag: #reader_obj.set_framenum(47):
                t_curr, r_curr = VO.run(frame, framenum)


                if t_curr is not None:
                    canvas = plot_trajectory(canvas, int(t_curr[0]) + 200, int(t_curr[2]) + 200, t_curr)
                    if VO.GT is not None:
                        plot_ground_truth(
                            canvas,
                            VO.GT[framenum - 1, 3] + 200,
                            VO.GT[framenum - 1, 11] + 200,
                        )
                    write_in_obj.write_frame(canvas)
                processed_frame_count += 1
                VO.re_compute_count += 1
        # if write_input:
        write_in_obj.release()

        Error = VO.get_error(processed_frame_count)
        if VO.GT is not None:
            print("ERROR: ", Error)
            assert Error < 2



if __name__ == "__main__":
    # CloneRepo(url="https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db.git", branch="kitty_dummy", repo_path="../kitty_dummy", access_token_name="DB_CLONE_TOKEN")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file_path",
        type=str,
        default="../kitty_dummy/sequences/04/image_0",
        help="input video file/images folder path",
    )
    parser.add_argument(
        "-d",
        "--display",
        default=False,
        nargs="?",
        const=True,
        help="Whether to show frames",
    )
    parser.add_argument(
        "-c",
        "--recompute_frame_count",
        default=False,
        nargs="?",
        const=True,
        help="frame count threshol for feature re computation",
    )
    parser.add_argument(
        "-match_method",
        "--match_method",
        default="optical_flow_based",
        nargs="?",
        const=True,
        help="mathcing method, eg: keypoint_register_based, superglue_based, knn_filter_based, ransac_based",
    )
    parser.add_argument(
        "-m",
        "--input_mode",
        type=str,
        default="folder",
        help="input mode : video/camera/folder",
    )
    parser.add_argument("-cam", "--cam_index", type=int, default=0, help="cam index")
    parser.add_argument(
        "-wi",
        "--write_input",
        default=False,
        nargs="?",
        const=True,
        help="Write input video",
    )

    parser.add_argument(
        "-op",
        "--optimize",
        default=False,
        nargs="?",
        const=True,
        help="Write input video",
    )

    parser.add_argument(
        "-me",
        "--multi_edge",
        default=False,
        nargs="?",
        const=True,
        help="use multi edge optimizer",
    )

    args = parser.parse_args()
    display = args.display
    file_path = args.file_path
    input_mode = args.input_mode
    write_input = args.write_input
    match_method = args.match_method
    recompute_count_thresh = args.recompute_frame_count
    optimize = args.optimize
    multi_edge = args.multi_edge
    dist = None
    K = None
    gt_path = None

    good_count_thresh_fraction = 50
    kp_count_thresh = 50
    FeatureMethod = "FAST"
    recompute_frame_thresh = 3
    if input_mode == "camera":
        file_path = args.cam_index
        K = K
        dist = cam_mtx["dist"]
        dist = None
        FeatureMethod = "ORB"

    elif input_mode == "video":
        # CloneRepo(url="https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db.git", branch="rssi_vo", repo_path="../rssi_vo", access_token_name="DB_CLONE_TOKEN")
        good_count_thresh_fraction = 95  # prcentage of kp0
        kp_count_thresh = 3000

        dist_ = "../rssi_vo/left/dist.npy"
        cam_calib = "../rssi_vo/left/mtx.npy"
        K = np.load(cam_calib)
        print(K)
        dist = np.load(dist_)

    # FeatureMethod = "ORB"
    VO = MONO_VO(
        K=K,
        dist=dist,
        FeatureMethod=FeatureMethod,
        good_count_thresh_fraction=good_count_thresh_fraction,
        kp_count_thresh=kp_count_thresh,
        recompute_frame_thresh=recompute_frame_thresh,
        show_flag=display,
        match_method=match_method,
        gt_path=gt_path,
        optimize=optimize,
        mulit_edge=multi_edge
    )

    print("Filepath: ", file_path)
    reader_obj = VideoReader(file_path)
    count = reader_obj.total_frame_count
    processed_frame_count = 0

    if display:
        canvas = np.zeros((1000, 1000, 3), dtype=np.uint8)
        canvas2 = np.zeros((512, 512, 3), dtype=np.uint8)
    if write_input:
        outputfile = "input.mp4"
    write_in_obj = None

    if input_mode == "camera":
        for i in range(10):
            frame, framenum, name = reader_obj.next_frame()
    run_flag = False

    # mapx,mapy = cv2.initUndistortRectifyMap(K,None,R1,P1,(image_size[1],image_size[0]),cv2.CV_16SC2)
    trajectory = []
    new_trajectory = []
    trajectory_path_new = []
    while processed_frame_count < count:
        print("Inside limit")
        # frame, framenum, name = reader_obj.next_frame()
        frame, _, framenum, trans_mat, _ = reader_obj.get_frame(processed_frame_count)
        # frame, _, framenum, trans_mat, _
        if framenum > 47:
            run_flag = True
        #
        # if processed_frame_count==0:
        #     h,  w = frame.shape[:2]
        #     newcameramtx, roi = cv2.getOptimalNewCameraMatrix(K, dist, (w,h), 1, (w,h))
        #     mapx, mapy = cv2.initUndistortRectifyMap(K, dist, None, newcameramtx, (w,h), 5)
        # frame = cv2.remap(frame, mapx, mapy, cv2.INTER_LINEAR)
        # frame = cv2.undistort(frame, K, dist, None, newcameramtx)
        # do unditort here
        if display:
            k = show(frame, win="input frame", time=10)
            if k == 27:
                break
        frame_height, frame_width, _ = frame.shape

        if write_input and write_in_obj is None:
            # write_in_obj = VideoWriter.remote(outputfile, reader_obj.fps, frame_width, frame_height)
            write_in_obj = VideoWriter(outputfile, reader_obj.fps, use_ffmpeg=True)

        if write_input:
            write_in_obj.write_frame(canvas)

        if 1:  # run_flag: #reader_obj.set_framenum(47):
            t_curr, r_curr = VO.run(frame, framenum)

            if t_curr is not None:
                if display:
                    print("trajectory :", int(t_curr[0]), int(t_curr[2]))
                    canvas = plot_trajectory(canvas,int(t_curr[0]) + 0, int(t_curr[2]) + 0, t_curr)
                    trajectory.append((int(t_curr[0]), int(t_curr[2]), int(t_curr[1])))
                    trac_np = np.array(trajectory)
                    max_ = np.max(trac_np, axis=0)
                    min_ = np.min(trac_np, axis=0)
                    boundary = max_ - min_
                    w_ = boundary[0] + 200 * 2
                    h_ = boundary[1] + 200 * 2
                    trac_np -= min_
                    trac_np += 200
                    # thresh_ = 100
                    # projected_x = trac_np[-1][0]
                    # projected_y = trac_np[-1][1]
                    # if projected_x > thresh_ or projected_y > thresh_:
                    #     new_projected_x = projected_x * thresh_/512
                    #     new_projected_y = projected_y * thresh_/512
                    #     new_projected_z = trac_np[-1][2] * thresh_/512
                    #     new_trajectory.append((int(new_projected_x), int(new_projected_y)))
                    #     trajectory_path_new.append((int(new_projected_x), int(new_projected_y), int(new_projected_z)))
                    #     new_trac_np = np.array(new_trajectory, np.int32)
                    #     print("old_track_np : ",trac_np)
                    #     print("new_track_np : ",new_trac_np)
                    #     # exit()
                    #     image_2 = cv2.polylines(canvas2, [new_trac_np], isClosed=False, color=(0, 0, 255), thickness=2)
                    # else:
                    #     image_2 = cv2.polylines(canvas2, [trac_np], isClosed=False, color=(0, 0, 255), thickness=2)
                    # show(image_2, win="polylines", time=10)
                    # cv2.imshow("polylines", image_2)

                    # for track in trajectory:
                    #     x = track[0]
                    #     y = track[1]
                    #     canvas = plot_trajectory(canvas, x, y, t_curr)
                    if VO.GT is not None:
                        plot_ground_truth(
                            canvas,
                            VO.GT[framenum - 1, 3] + 200,
                            VO.GT[framenum - 1, 11] + 200,
                        )
            
            processed_frame_count += 1
            VO.re_compute_count += 1
            if display:
                show(canvas, win="Trajectory", time=10)
                # show(image_2, win="polylines", time=10)
                # cv2.imshow("polylines", image_2)
    print("Outside Limit")
    cv2.imwrite("final.png", canvas)
    if write_input:
        write_in_obj.release.remote()

    Error = VO.get_error(processed_frame_count)
    if VO.GT is not None:
        print("ERROR: ", Error)
        assert Error < 2
