"""IvLabs, VNIT
MONOCULAR VISUAL ODOMETRY ON KITTI DATASET

TEAM MEMBERS:
1. Arihant Gaur
2. Saurabh Kemekar
3. Aman Jain
"""

import cv2
import numpy as np

# from ignutils.geom_utils import euclidean
from ignutils.show_utils import show


def FeatureTracking(image_ref, image_cur, img_cur_color, kp0, kp1=None, matchDiff=1, show_flag=False):
    """Feature Tracking"""
    # show(image_ref, win='prev grey', time=10)
    # show(image_cur, win='curr grey', time=10)
    lk_params = dict(
        winSize=(21, 21),
        maxLevel=3,
        criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 30, 0.01),
    )
    kp1, st, err = cv2.calcOpticalFlowPyrLK(image_ref, image_cur, kp0, None, **lk_params)
    kp0_dummy, st, err = cv2.calcOpticalFlowPyrLK(image_cur, image_ref, kp1, None, **lk_params)

    print("input kp0     : ", kp0.shape[0])
    print("flow kp1      : ", kp1.shape[0])
    print("flow kp dummy : ", kp0_dummy.shape[0])

    good = []
    for index, (x0, y0) in enumerate(kp0):
        x1, y1 = kp0_dummy[index]
        dist = max(abs(x0 - x1), abs(y0 - y1))
        # print('dist: ', dist)
        if dist < matchDiff:
            good.append(True)
        else:
            good.append(False)
    good_count = list(good).count(True)

    print("good_count: ", good_count)
    # Draw match b/w kp0 & kp1
    if show_flag:
        for ind in range(len(kp0)):
            k1 = kp0[ind]
            k2 = kp1[ind]
            good_flag = good[ind]
            if good_flag:
                color = (0, 255, 0)
            else:
                color = (0, 0, 255)
            start_point = tuple(k1.astype(int))
            end_point = tuple(k2.astype(int))
            if good_flag:
                cv2.circle(img_cur_color, start_point, 2, (255, 255, 255), 1)
                cv2.circle(img_cur_color, end_point, 2, (255, 0, 0), 1)
            cv2.line(img_cur_color, start_point, end_point, color, 1)

        show(img_cur_color, win="Tracking", time=10, x=650, y=400, height=300, width=600)

    if good_count == 0:
        print("Error: No matches where made.")
        return None, None, None, 0

    # If less than 5 good points, then the backtracked points are not used.
    if good_count <= 5:
        print("Warning: No match was good. Returns the list without good point correspondence.")
        return kp0, kp1, None, good_count

    # Considering good features
    n_kp0 = kp0[good]
    n_kp1 = kp1[good]
    diff_mean = get_mean_diff(n_kp0, n_kp1)

    return n_kp0, n_kp1, diff_mean, good_count


def get_mean_diff(kp0, kp1):
    """Function to get the mean difference"""
    if not isinstance(kp0, np.ndarray):
        kp0 = np.array(kp0)
    if not isinstance(kp1, np.ndarray):
        kp1 = np.array(kp1)

    if 1:
        d = abs(kp0 - kp1).reshape(-1, 2).max(-1)
        diff_mean = np.mean(d)

    if 0:  # eucledian based difference
        diff = np.linalg.norm(kp0 - kp1, axis=1)
        diff_mean = np.mean(diff)

    return diff_mean
