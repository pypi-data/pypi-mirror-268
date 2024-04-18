"""Main function for mono VO"""
import argparse
import os
import time
from copy import deepcopy
# from tkinter import filedialog

import cv2
# import matplotlib.pyplot as plt
import numpy as np
from feature_det import featureDet
from feature_track import FeatureTracking
from Visualization import *

from ignutils.clone_utils import CloneRepo
from ignutils.geom_utils import euclidean


def Triangulation(R, t, kp0, kp1, K):
    """Triangulation"""
    P0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
    P0 = K.dot(P0)
    P1 = np.hstack((R, t))
    P1 = K.dot(P1)
    points1 = kp0.reshape(2, -1)
    points2 = kp1.reshape(2, -1)
    cloud = cv2.triangulatePoints(P0, P1, points1, points2).reshape(-1, 4)[:, :3]
    return cloud

def AbsoluteScale(groundTruth, last_id, curr_id):
    """Absolute Scale"""
    x_prev = groundTruth[last_id, 3]
    y_prev = groundTruth[last_id, 7]
    z_prev = groundTruth[last_id, 11]

    x = groundTruth[curr_id, 3]
    y = groundTruth[curr_id, 7]
    z = groundTruth[curr_id, 11]
    Enorm = np.sqrt((x - x_prev) ** 2 + (y - y_prev) ** 2 + (z - z_prev) ** 2)
    return Enorm


def RelativeScale(last_cloud, new_cloud):
    """Relative Scale"""
    min_idx = min([new_cloud.shape[0], last_cloud.shape[0]])
    p_Xk = new_cloud[:min_idx]
    Xk = np.roll(p_Xk, shift=-3)
    p_Xk_1 = last_cloud[:min_idx]
    Xk_1 = np.roll(p_Xk_1, shift=-3)
    d_ratio = (np.linalg.norm(p_Xk_1 - Xk_1, axis=-1)) / (np.linalg.norm(p_Xk - Xk, axis=-1))

    return np.median(d_ratio)


def main(args):
    """Main Function"""
    CloneRepo(url="https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/sample_images.git", branch="KITTI_sample", repo_path="KITTI_sample", access_token_name="DB_CLONE_TOKEN")

    show_flag = args.show_flag

    # PARAMETERS THAT CAN BE CHANGED
    ImgLoc = "KITTI_sample/images/"
    GTLoc = True
    totImages = len(os.listdir(ImgLoc))
    print(totImages)
    # FEATURE DETECTION METHOD ('FAST', 'SIFT' and 'SURF')
    FeatureMethod = "FAST"
    pixDiffThresh = 3
    featureThresh = 1000
    if GTLoc:
        ground_truth = np.loadtxt("KITTI_sample/poses.txt")
    # Lucas Kanade Parameters for Optical Flow

    K = np.array(
        [
            [7.188560000000e02, 0.000000000000e00, 6.071928000000e02],
            [0.000000000000e00, 7.188560000000e02, 1.852157000000e02],
            [0.000000000000e00, 0.000000000000e00, 1.000000000000e00],
        ]
    )

    ft_obj = featureDet(FeatureMethod)
    kp_threshold = 100  # Key points count

    t = []
    R = []
    # Plotting values for absolute scale
    t.append(tuple([[0], [0], [0]]))
    R.append(tuple(np.zeros((3, 3))))

    i = 0
    canvas = np.zeros((700, 1000, 3), dtype=np.uint8)
    a = 200
    b = 200
    kp1_copy = None
    start_time = time.time()
    Xnew = None
    first_frame = True
    kp0, kp1 = None, None
    img0gray = None
    first_pair = True

    while i <= totImages - 1:
        print("Image ind: ", i)
        Xold = Xnew

        if kp1_copy is not None:
            kp0 = kp1_copy
        else:
            kp0 = kp1

        img1 = cv2.imread(ImgLoc + str(i + 1) + ".png")  # Image acquisition
        img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

        if first_frame:
            img0gray = img1gray.copy()
            kp0 = ft_obj.FeatureDetection(img0gray)
            kp1 = kp0  # for the first frame, assign kp1 to kp0
            i += 1
            first_frame = False
            continue

        kp0, kp1, diff, good_count = FeatureTracking(img0gray, img1gray, img1, kp0, show_flag=show_flag)
        if good_count < kp_threshold:
            print("Recalculating feat det")
            kp1 = ft_obj.FeatureDetection(img1gray)
            kp1_copy = deepcopy(kp1)
            kp0, kp1, diff, good_count = FeatureTracking(img0gray, img1gray, img1, kp0, show_flag=show_flag)
            if good_count < kp_threshold:
                print("Registration failed")
                continue
        else:
            kp1_copy = None

        # Pose recovery
        E, mask = cv2.findEssentialMat(kp1, kp0, K, method=cv2.RANSAC, prob=0.999, threshold=0.4, mask=None)
        kp0 = kp0[mask.ravel() == 1]
        kp1 = kp1[mask.ravel() == 1]
        _, R0, t0, mask = cv2.recoverPose(E, kp0, kp1, K)

        if first_pair:
            first_pair = False
            t_curr = R0.dot(t0)
            R_curr = R0

        # Triangulation
        Xnew = Triangulation(R0, t0, kp0, kp1, K)

        if GTLoc:
            scale = -AbsoluteScale(ground_truth, i - 1, i)
            plot_ground_truth(canvas, ground_truth[i, 3] + a, ground_truth[i, 11] + b)
        else:
            scale = -RelativeScale(Xold, Xnew)

        t_curr = t_curr + scale * R_curr.dot(t0)
        R_curr = R_curr.dot(R0)

        if kp0.shape[0] < featureThresh:
            print("Recalculating feat det")
            kp1 = ft_obj.FeatureDetection(img1gray)

        canvas = plot_trajectory(canvas, int(t_curr[0]) + a, int(t_curr[2]) + b, t_curr)

        if show_flag:
            cv2.imshow("canvas", canvas)
            cv2.imshow("img", img1)
            cv2.waitKey(0)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        i = i + 1
        Tf = time.time()

        if first_frame:
            first_frame = False
        img0gray = img1gray

    if show_flag:
        cv2.imshow("canvas", canvas)
        cv2.waitKey(0)

    exec_time = Tf - start_time
    print("Overall FPS: ", totImages / exec_time)

    gt_X = ground_truth[i - 1, 3]
    gt_Y = ground_truth[i - 1, 11]
    pr_X = t_curr[0][0]
    pr_Y = t_curr[2][0]

    error = euclidean((gt_X, gt_Y), (pr_X, pr_Y))
    if show_flag:
        cv2.destroyAllWindows()
    return error

    # TO-DO: adding class and args in main with K from calibration


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-show", "--show_flag", default=False, nargs="?", const=True, help="Debug mode")
    args = parser.parse_args()
    error = main(args)
    print("ERROR: ", error)
    assert error < 5
