"""Script for finding matches"""
import os
import cv2
import numpy as np
from ignutils.vo.mono_vo.feature_track import FeatureTracking, get_mean_diff
from skimage.measure import ransac
from skimage.transform import FundamentalMatrixTransform

from ignutils.registration.register_wrapper import RegistrationWrapper
from ignutils.show_utils import show
from ignutils.transform_utils import transform_contour


def keypoint_register_match(kp0, img0gray, img1gray):
    """ keypoint register match"""
    reg_obj = RegistrationWrapper(register_type="keypoint", config_dir=os.getcwd())
    _, mat, _, _ = reg_obj.register(img0gray, img1gray)
    print(mat)
    kp1_ = transform_contour(kp0, mat)
    kp1 = kp1_[0]
    good_count = len(kp1)
    diff = get_mean_diff(kp0, kp1)
    return kp0, kp1, diff, good_count


def normalize(count_inv, pts):
    """normalization"""
    return np.dot(count_inv, np.concatenate([pts, np.ones((pts.shape[0], 1))], axis=1).T).T[:, 0:2]


def denormalize(count, pt):
    """denormalization"""
    ret = np.dot(count, np.array([pt[0], pt[1], 1.0]))
    ret /= ret[2]
    return int(round(ret[0])), int(round(ret[1]))


def featureMapping(image):
    "feature mapping"
    image_ = image.copy()
    orb = cv2.ORB_create()
    pts = cv2.goodFeaturesToTrack(np.mean(image, axis=2).astype(np.uint8), 1000, qualityLevel=0.01, minDistance=7)
    key_pts = [cv2.KeyPoint(x=f[0][0], y=f[0][1], size=20) for f in pts]
    key_pts, descriptors = orb.compute(image, key_pts)
    # moving_kp = cv2.drawKeypoints(image_, key_pts, None, color=(0, 255, 0))
    # show(moving_kp, win="moving_kp", time=10, destroy=False)
    # Return Key_points and ORB_descriptors
    return np.array([(kp.pt[0], kp.pt[1]) for kp in key_pts]), descriptors


def extract(frame):
    """extract keypoints"""
    # extract keypoints and dicriptor
    orb = cv2.ORB_create()
    feats = cv2.goodFeaturesToTrack(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 1000, qualityLevel=0.01, minDistance=7)
    kp = [cv2.KeyPoint(*f[0], size=3) for f in feats]
    kp, des = orb.compute(frame, kp)
    return kp, des


def superglue_based_match(img0, img1):
    """matcing based on super glue"""
    reg_obj = RegistrationWrapper(register_type="superglue", config_dir=os.getcwd())
    # _, _, kp1, kp0 = reg_obj.register(img0, img1, True)
    _, _, kp1, kp0 = reg_obj.register(img0, img1)
    diff = get_mean_diff(kp0, kp1)
    good_count = len(kp0)
    return kp0, kp1, diff, good_count


def knn_match(frame_pair):
    """match based on knn"""
    curr, prev = frame_pair
    # matching two frames
    curr_features, curr_discriptor = extract(curr)
    prev_features, prev_discriptor = extract(prev)
    matches = cv2.BFMatcher(cv2.NORM_HAMMING).knnMatch(curr_discriptor, prev_discriptor, k=2)
    matched0 = []
    matched1 = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            p1 = curr_features[m.queryIdx].pt
            p2 = prev_features[m.trainIdx].pt
            p1, p2 = tuple(p1), tuple(p2)
            matched0.append([p1])
            matched1.append([p2])
    good_count = len(matched0)
    kp0 = np.array(matched0, dtype=np.float32)
    kp1 = np.array(matched1, dtype=np.float32)
    diff = get_mean_diff(kp0, kp1)
    return kp0, kp1, diff, good_count


def ransac_based_match(image_0, image_1, K):
    """match based on ransac"""
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    key_pts0, descriptors_0 = featureMapping(image_0)
    key_pts1, descriptors_1 = featureMapping(image_1)
    print(len(key_pts0))
    count_inv = np.linalg.inv(K)
    # print("inv", count_inv)
    key_pts_0 = normalize(count_inv, key_pts0)
    key_pts_1 = normalize(count_inv, key_pts1)
    matches = bf.knnMatch(descriptors_0, descriptors_1, k=2)
    h, w = image_0.shape[0:2]
    # Lowe's ratio test
    ret = []
    x1, x2 = [], []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            pts1 = key_pts_0[m.queryIdx]
            pts2 = key_pts_1[m.trainIdx]

            # travel less than 10% of diagonal and be within orb distance 32
            if np.linalg.norm((pts1 - pts2)) < 0.1 * np.linalg.norm([w, h]) and m.distance < 32:
                # keep around indices
                # TO-DO: refactor this to not be O(N^2)
                if m.queryIdx not in x1 and m.trainIdx not in x2:
                    x1.append(m.queryIdx)
                    x2.append(m.trainIdx)

                    ret.append((pts1, pts2))

    # print("ret", ret)
    # no duplicates
    assert len(set(x1)) == len(x1)
    assert len(set(x2)) == len(x2)

    assert len(ret) >= 8
    ret = np.array(ret)
    x1 = np.array(x1)
    x2 = np.array(x2)

    # fit matrix
    print("len ret", len(ret))
    model, f_pts = ransac(
        (ret[:, 0], ret[:, 1]),
        FundamentalMatrixTransform,
        # EssentialMatrixTransform,
        min_samples=8,
        residual_threshold=0.001,
        max_trials=100,
    )
    # print("Matches: %d -> %d -> %d -> %d" % (len(descriptors_0), len(matches), len(f_pts), sum(f_pts)))
    print(f"Matches: {len(descriptors_0)} -> {len(matches)} -> {len(f_pts)} -> {sum(f_pts)}")

    kp0 = []
    kp1 = []
    X1_ = x1[f_pts]
    X2_ = x2[f_pts]

    image_1_copy = image_1.copy()
    for pt1, pt2 in zip(key_pts_0[X1_], key_pts_1[X2_]):
        # import pdb;pdb.set_trace()
        u1, v1 = denormalize(K, pt1)
        u2, v2 = denormalize(K, pt2)
        cv2.circle(image_1_copy, (u1, v1), color=(255, 0, 0), radius=1)
        cv2.line(image_1_copy, (u1, v1), (u2, v2), color=(255, 255, 0))
        kp0.append([u1, v1])
        kp1.append([u2, v2])

    show(image_1_copy, win="MATCHFRAME", time=10)
    kp0 = np.array(kp0, dtype=np.float32)
    kp1 = np.array(kp1, dtype=np.float32)
    diff = get_mean_diff(kp0, kp1)
    # print("Matches: %d -> %d -> %d -> %d" % (len(descriptors_0), len(matches), len(f_pts), sum(f_pts)))
    print(f"Matches: {len(descriptors_0)} -> {len(matches)} -> {len(f_pts)} -> {sum(f_pts)}")

    good_count = len(kp0)
    return kp0, kp1, diff, good_count


def optical_flow_match(image_ref, image_cur, img_cur_color, kp0, kp1=None, matchDiff=1, show_flag=False): # pylint: disable=unused-argument
    """match based on optical flow"""
    kp0, kp1, diff, good_count = FeatureTracking(image_ref, image_cur, img_cur_color, kp0, matchDiff=1, show_flag=show_flag)
    return kp0, kp1, diff, good_count
