import datetime
# import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
from data_handler import Dataset_Handler

from ignutils.clone_utils import CloneRepo


def decompose_projection_matrix(p):
    """Shortcut to use cv2.decomposeProjectionMatrix(), which only returns k, r, t, and divides
    t by the scale, then returns it as a vector with shape (3,) (non-homogeneous)

    Arguments:
    p -- projection matrix to be decomposed

    Returns:
    k, r, t -- intrinsic matrix, rotation matrix, and 3D translation vector

    """
    k, r, t, _, _, _, _ = cv2.decomposeProjectionMatrix(p)
    t = (t / t[3])[:3]

    return k, r, t


def stereo_2_depth(img_left, img_right, P0, P1, matcher="bm", rgb=False, verbose=False, rectified=True): # pylint: disable=unused-argument
    """Takes stereo pair of images and returns a depth map for the left camera. If your projection
    matrices are not rectified, set rectified=False.

    Arguments:
    img_left -- image of left camera
    img_right -- image of right camera
    P0 -- Projection matrix for the left camera
    P1 -- Projection matrix for the right camera

    Optional Arguments:
    matcher -- (str) can be 'bm' for StereoBM or 'sgbm' for StereoSGBM
    rgb -- (bool) set to True if images passed are RGB. Default is False
    verbose -- (bool) set to True to report computation time and method
    rectified -- (bool) set to False if P1 not rectified to P0. Default is True

    Returns:
    depth -- depth map for left camera

    """
    # Compute disparity map
    disp = compute_left_disparity_map(img_left, img_right, matcher=matcher, rgb=rgb, verbose=verbose)
    # Decompose projection matrices
    k_left, r_left, t_left = decompose_projection_matrix(P0)
    k_right, r_right, t_right = decompose_projection_matrix(P1)
    # Calculate depth map for left camera
    depth = calc_depth_map(disp, k_left, t_left, t_right)

    return depth


def pointcloud2image(pointcloud, imheight, imwidth, Tr, P0):
    """Takes a pointcloud of shape Nx4 and projects it onto an image plane, first transforming
    the X, Y, Z coordinates of points to the camera frame with tranformation matrix Tr, then
    projecting them using camera projection matrix P0.

    Arguments:
    pointcloud -- array of shape Nx4 containing (X, Y, Z, reflectivity)
    imheight -- height (in pixels) of image plane
    imwidth -- width (in pixels) of image plane
    Tr -- 3x4 transformation matrix between lidar (X, Y, Z, 1) homogeneous and camera (X, Y, Z)
    P0 -- projection matrix of camera (should have identity transformation if Tr used)

    Returns:
    render -- a (imheight x imwidth) array containing depth (Z) information from lidar scan

    """
    # We know the lidar X axis points forward, we need nothing behind the lidar, so we
    # ignore anything with a X value less than or equal to zero
    pointcloud = pointcloud[pointcloud[:, 0] > 0]

    # We do not need reflectance info, so drop last column and replace with ones to make
    # coordinates homogeneous for tranformation into the camera coordinate frame
    pointcloud = np.hstack([pointcloud[:, :3], np.ones(pointcloud.shape[0]).reshape((-1, 1))])

    # Transform pointcloud into camera coordinate frame
    cam_xyz = Tr.dot(pointcloud.T)

    # Ignore any points behind the camera (probably redundant but just in case)
    cam_xyz = cam_xyz[:, cam_xyz[2] > 0]

    # Extract the Z row which is the depth from camera
    depth = cam_xyz[2].copy()

    # Project coordinates in camera frame to flat plane at Z=1 by dividing by Z
    cam_xyz /= cam_xyz[2]

    # Add row of ones to make our 3D coordinates on plane homogeneous for dotting with P0
    cam_xyz = np.vstack([cam_xyz, np.ones(cam_xyz.shape[1])])

    # Get pixel coordinates of X, Y, Z points in camera coordinate frame
    projection = P0.dot(cam_xyz)
    # projection = (projection / projection[2])

    # Turn pixels into integers for indexing
    pixel_coordinates = np.round(projection.T, 0)[:, :2].astype("int")
    # pixel_coordinates = np.array(pixel_coordinates)

    # Limit pixel coordinates considered to those that fit on the image plane
    indices = np.where((pixel_coordinates[:, 0] < imwidth) & (pixel_coordinates[:, 0] >= 0) & (pixel_coordinates[:, 1] < imheight) & (pixel_coordinates[:, 1] >= 0))
    pixel_coordinates = pixel_coordinates[indices]
    depth = depth[indices]

    # Establish empty render image, then fill with the depths of each point
    render = np.zeros((imheight, imwidth))
    for j, (u, v) in enumerate(pixel_coordinates):
        if u >= imwidth or u < 0:
            continue
        if v >= imheight or v < 0:
            continue
        render[v, u] = depth[j]
    # Fill zero values with large distance so they will be ignored. (Using same max value)
    render[render == 0.0] = 3861.45

    return render


def extract_features(image, detector="sift", mask=None):
    """Find keypoints and descriptors for the image

    Arguments:
    image -- a grayscale image

    Returns:
    kp -- list of the extracted keypoints (features) in an image
    des -- list of the keypoint descriptors in an image
    """
    if detector == "sift":
        det = cv2.SIFT_create()
    elif detector == "orb":
        det = cv2.ORB_create()
    elif detector == "surf":
        det = cv2.xfeatures2d.SURF_create()

    kp, des = det.detectAndCompute(image, mask)

    return kp, des


def match_features(des1, des2, matching="BF", detector="sift", sort=True, k=2):
    """Match features from two images

    Arguments:
    des1 -- list of the keypoint descriptors in the first image
    des2 -- list of the keypoint descriptors in the second image
    matching -- (str) can be 'BF' for Brute Force or 'FLANN'
    detector -- (str) can be 'sift or 'orb'. Default is 'sift'
    sort -- (bool) whether to sort matches by distance. Default is True
    k -- (int) number of neighbors to match to each feature.

    Returns:
    matches -- list of matched features from two images. Each match[i] is k or less matches for
               the same query descriptor
    """
    if matching == "BF":
        if detector == "sift":
            matcher = cv2.BFMatcher_create(cv2.NORM_L2, crossCheck=False)
        elif detector == "orb":
            matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING2, crossCheck=False)
        matches = matcher.knnMatch(des1, des2, k=k)
    elif matching == "FLANN":
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        matcher = cv2.FlannBasedMatcher(index_params, search_params)
        matches = matcher.knnMatch(des1, des2, k=k)

    if sort:
        matches = sorted(matches, key=lambda x: x[0].distance)

    return matches


def filter_matches_distance(matches, dist_threshold):
    """Filter matched features from two images by distance between the best matches

    Arguments:
    match -- list of matched features from two images
    dist_threshold -- maximum allowed relative distance between the best matches, (0.0, 1.0)

    Returns:
    filtered_match -- list of good matches, satisfying the distance threshold
    """
    filtered_match = []
    for m, n in matches:
        if m.distance <= dist_threshold * n.distance:
            filtered_match.append(m)

    return filtered_match


def visualize_matches(image1, kp1, image2, kp2, match):
    """Visualize corresponding matches in two images

    Arguments:
    image1 -- the first image in a matched image pair
    kp1 -- list of the keypoints in the first image
    image2 -- the second image in a matched image pair
    kp2 -- list of the keypoints in the second image
    match -- list of matched features from the pair of images

    Returns:
    image_matches -- an image showing the corresponding matches on both image1 and image2 or None if you don't use this function
    """
    image_matches = cv2.drawMatches(image1, kp1, image2, kp2, match, None, flags=2)
    plt.figure(figsize=(16, 6), dpi=100)
    plt.imshow(image_matches)
    plt.show()
    plt.savefigure("match.png")


def estimate_motion(match, kp1, kp2, k, depth1=None, max_depth=3000):
    """Estimate camera motion from a pair of subsequent image frames

    Arguments:
    match -- list of matched features from the pair of images
    kp1 -- list of the keypoints in the first image
    kp2 -- list of the keypoints in the second image
    k -- camera intrinsic calibration matrix

    Optional arguments:
    depth1 -- Depth map of the first frame. Set to None to use Essential Matrix decomposition
    max_depth -- Threshold of depth to ignore matched features. 3000 is default

    Returns:
    rmat -- estimated 3x3 rotation matrix
    tvec -- estimated 3x1 translation vector
    image1_points -- matched feature pixel coordinates in the first image.
                     image1_points[i] = [u, v] -> pixel coordinates of i-th match
    image2_points -- matched feature pixel coordinates in the second image.
                     image2_points[i] = [u, v] -> pixel coordinates of i-th match

    """
    rmat = np.eye(3)
    tvec = np.zeros((3, 1))

    image1_points = np.array([kp1[m.queryIdx].pt for m in match], dtype=np.float32)
    image2_points = np.array([kp2[m.trainIdx].pt for m in match], dtype=np.float32)

    if depth1 is not None:
        cx = k[0, 2]
        cy = k[1, 2]
        fx = k[0, 0]
        fy = k[1, 1]
        object_points = np.zeros((0, 3))
        delete = []

        # Extract depth information of query image at match points and build 3D positions
        for i, (u, v) in enumerate(image1_points):
            z = depth1[int(v), int(u)]
            # If the depth at the position of our matched feature is above 3000, then we
            # ignore this feature because we don't actually know the depth and it will throw
            # our calculations off. We add its index to a list of coordinates to delete from our
            # keypoint lists, and continue the loop. After the loop, we remove these indices
            if z > max_depth:
                delete.append(i)
                continue

            # Use arithmetic to extract x and y (faster than using inverse of k)
            x = z * (u - cx) / fx
            y = z * (v - cy) / fy
            object_points = np.vstack([object_points, np.array([x, y, z])])
            # Equivalent math with dot product w/ inverse of k matrix, but SLOWER (see Appendix A)
            # object_points = np.vstack([object_points, np.linalg.inv(k).dot(z*np.array([u, v, 1]))])

        image1_points = np.delete(image1_points, delete, 0)
        image2_points = np.delete(image2_points, delete, 0)
        # print(object_points)
        # print(image2_points)
        # Use PnP algorithm with RANSAC for robustness to outliers
        _, rvec, tvec, inliers = cv2.solvePnPRansac(object_points, image2_points, k, None)
        # print('Number of inliers: {}/{} matched features'.format(len(inliers), len(match)))

        # Above function returns axis angle rotation representation rvec, use Rodrigues formula
        # to convert this to our desired format of a 3x3 rotation matrix
        rmat = cv2.Rodrigues(rvec)[0]

    else:
        # With no depth provided, use essential matrix decomposition instead. This is not really
        # very useful, since you will get a 3D motion tracking but the scale will be ambiguous
        image1_points_hom = np.hstack([image1_points, np.ones(len(image1_points)).reshape(-1, 1)])
        image2_points_hom = np.hstack([image2_points, np.ones(len(image2_points)).reshape(-1, 1)])
        E = cv2.findEssentialMat(image1_points, image2_points, k)[0]
        _, rmat, tvec, mask = cv2.recoverPose(E, image1_points, image2_points, k)

    return rmat, tvec, image1_points, image2_points


def compute_left_disparity_map(img_left, img_right, matcher="bm", rgb=False, verbose=False):
    """Takes a left and right stereo pair of images and computes the disparity map for the left
    image. Pass rgb=True if the images are RGB.

    Arguments:
    img_left -- image from left camera
    img_right -- image from right camera

    Optional Arguments:
    matcher -- (str) can be 'bm' for StereoBM or 'sgbm' for StereoSGBM matching
    rgb -- (bool) set to True if passing RGB images as input
    verbose -- (bool) set to True to report matching type and time to compute

    Returns:
    disp_left -- disparity map for the left camera image

    """
    # Feel free to read OpenCV documentation and tweak these values. These work well
    sad_window = 6
    num_disparities = sad_window * 16
    block_size = 11
    matcher_name = matcher

    if matcher_name == "bm":
        matcher = cv2.StereoBM_create(numDisparities=num_disparities, blockSize=block_size)

    elif matcher_name == "sgbm":
        matcher = cv2.StereoSGBM_create(
            numDisparities=num_disparities,
            minDisparity=0,
            blockSize=block_size,
            P1=8 * 3 * sad_window**2,
            P2=32 * 3 * sad_window**2,
            mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY,
        )
    if rgb:
        img_left = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
        img_right = cv2.cvtColor(img_right, cv2.COLOR_BGR2GRAY)
    start = datetime.datetime.now()
    disp_left = matcher.compute(img_left, img_right).astype(np.float32) / 16
    end = datetime.datetime.now()
    if verbose:
        print(
            f"Time to compute disparity map using Stereo{matcher_name.upper()}:",
            end - start,
        )

    return disp_left


def calc_depth_map(disp_left, k_left, t_left, t_right, rectified=True):
    """Calculate depth map using a disparity map, intrinsic camera matrix, and translation vectors
    from camera extrinsic matrices (to calculate baseline). Note that default behavior is for
    rectified projection matrix for right camera. If using a regular projection matrix, pass
    rectified=False to avoid issues.

    Arguments:
    disp_left -- disparity map of left camera
    k_left -- intrinsic matrix for left camera
    t_left -- translation vector for left camera
    t_right -- translation vector for right camera

    Optional Arguments:
    rectified -- (bool) set to False if t_right is not from rectified projection matrix

    Returns:
    depth_map -- calculated depth map for left camera

    """
    # Get focal length of x axis for left camera
    f = k_left[0][0]

    # Calculate baseline of stereo pair
    if rectified:
        b = t_right[0] - t_left[0]
    else:
        b = t_left[0] - t_right[0]

    # Avoid instability and division by zero
    disp_left[disp_left == 0.0] = 0.1
    disp_left[disp_left == -1.0] = 0.1

    # Make empty depth map then fill with depth
    depth_map = np.ones(disp_left.shape)
    depth_map = f * b / disp_left

    return depth_map


def visual_odometry(
    handler,
    detector="sift",
    matching="BF",
    filter_match_distance=None,
    stereo_matcher="bm",
    mask=None,
    depth_type="stereo",
    subset=None,
    plot=False,
):
    """Function to perform visual odometry on a sequence from the KITTI visual odometry dataset.
    Takes as input a Data_Handler object and optional parameters.

    Arguments:
    handler -- Data_Handler object instance

    Optional Arguments:
    detector -- (str) can be 'sift' or 'orb'. Default is 'sift'.
    matching -- (str) can be 'BF' for Brute Force or 'FLANN'. Default is 'BF'.
    filter_match_distance -- (float) value for ratio test on matched features. Default is None.
    stereo_matcher -- (str) can be 'bm' (faster) or 'sgbm' (more accurate). Default is 'bm'.
    mask -- (array) mask to reduce feature search area to where depth information available.
    depth_type -- (str) can be 'stereo' or set to None to use Essential matrix decomposition.
                        Note that scale will be incorrect with no depth used.
    subset -- (int) number of frames to compute. Defaults to None to compute all frames.
    plot -- (bool) whether to plot the estimated vs ground truth trajectory. Only works if
                   matplotlib is set to tk mode. Default is False.

    Returns:
    trajectory -- Array of shape Nx3x4 of estimated poses of vehicle for each computed frame.

    """
    # Determine if handler has lidar data
    lidar = handler.lidar

    # Report methods being used to user
    print(f"Generating disparities with Stereo{str.upper(stereo_matcher)}")
    print(f"Detecting features with {str.upper(detector)} and matching with {matching}")
    if filter_match_distance is not None:
        print(f"Filtering feature matches at threshold of {filter_match_distance}*distance")
    # if lidar:
    #     print('Improving stereo depth estimation with lidar data')
    if subset is not None:
        # subset = subset + 1
        num_frames = subset
    else:
        # Set num_frames to one less than the number of frames so we have sequential images
        # in the last frame run.
        num_frames = handler.num_frames

    if plot:
        fig = plt.figure(figsize=(14, 14))
        ax = fig.add_subplot(projection="3d")
        ax.view_init(elev=-20, azim=270)
        xs = handler.gt[:, 0, 3]
        ys = handler.gt[:, 1, 3]
        zs = handler.gt[:, 2, 3]
        ax.set_box_aspect((np.ptp(xs), np.ptp(ys), np.ptp(zs)))
        ax.plot(xs, ys, zs, c="k")

    # Establish homogeneous transformation matrix. First pose is identity
    T_tot = np.eye(4)
    trajectory = np.zeros((num_frames, 3, 4))
    trajectory[0] = T_tot[:3, :]
    imheight = handler.imheight
    imwidth = handler.imwidth

    # Decompose left camera projection matrix to get intrinsic k matrix
    k_left, r_left, t_left = decompose_projection_matrix(handler.P0)

    if handler.low_memory:
        handler.reset_frames()
        image_plus1 = next(handler.images_left)

    # Iterate through all frames of the sequence
    for i in range(num_frames - 1):
        # Stop if we've reached the second to last frame, since we need two sequential frames
        # if i == num_frames - 1:
        #    break
        # Start timer for frame
        start = datetime.datetime.now()
        # Get our stereo images for depth estimation
        if handler.low_memory:
            image_left = image_plus1
            image_right = next(handler.images_right)
            # Get next frame in the left camera for visual odometry
            image_plus1 = next(handler.images_left)
        else:
            image_left = handler.images_left[i]
            image_right = handler.images_right[i]
            # Get next frame in the left camera for visual odometry
            image_plus1 = handler.images_left[i + 1]

        # Estimate depth if using stereo depth estimation (recommended)
        if depth_type == "stereo":
            depth = stereo_2_depth(
                image_left,
                image_right,
                P0=handler.P0,
                P1=handler.P1,
                matcher=stereo_matcher,
            )
        # Otherwise use Essential Matrix decomposition (ambiguous scale)
        else:
            depth = None

        # Supercede stereo depth estimations where lidar points are available
        if lidar:
            if handler.low_memory:
                pointcloud = next(handler.pointclouds)
            else:
                pointcloud = handler.pointclouds[i]
            lidar_depth = pointcloud2image(
                pointcloud,
                imheight=imheight,
                imwidth=imwidth,
                Tr=handler.Tr,
                P0=handler.P0,
            )
            indices = np.where(lidar_depth < 3000)
            depth[indices] = lidar_depth[indices]

        # Get keypoints and descriptors for left camera image of two sequential frames
        kp0, des0 = extract_features(image_left, detector)
        kp1, des1 = extract_features(image_plus1, detector)

        # Get matches between features detected in the two images
        matches_unfilt = match_features(des0, des1, matching=matching, detector=detector, sort=True)

        # Filter matches if a distance threshold is provided by user
        if filter_match_distance is not None:
            matches = filter_matches_distance(matches_unfilt, filter_match_distance)
        else:
            matches = matches_unfilt

        # print("matches", matches)
        # Estimate motion between sequential images of the left camera
        rmat, tvec, img1_points, img2_points = estimate_motion(matches, kp0, kp1, k_left, depth)
        Tmat = np.eye(4)
        # Place resulting rotation matrix  and translation vector in their proper locations
        # in homogeneous T matrix
        Tmat[:3, :3] = rmat
        Tmat[:3, 3] = tvec.T
        T_tot = T_tot.dot(np.linalg.inv(Tmat))

        # Place pose estimate in i+1 to correspond to the second image, which we estimated for
        trajectory[i + 1, :, :] = T_tot[:3, :]
        # End the timer for the frame and report frame rate to user
        end = datetime.datetime.now()
        print("Time to compute frame {}:".format(i + 1), end - start)

        if plot:
            xs = trajectory[: i + 2, 0, 3]
            ys = trajectory[: i + 2, 1, 3]
            zs = trajectory[: i + 2, 2, 3]
            plt.plot(xs, ys, zs, c="chartreuse")
            plt.pause(1e-32)

    if plot:
        plt.close()

    return trajectory


if __name__ == "__main__":
    CloneRepo(url="https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db.git", branch="kitty_dummy", repo_path="../kitty_dummy", access_token_name="DB_CLONE_TOKEN")

    handler = Dataset_Handler("04")
    mask = np.zeros(handler.first_image_left.shape[:2], dtype=np.uint8)
    if 1:
        handler.lidar = True
        start = datetime.datetime.now()
        trajectory_nolidar_bm = visual_odometry(
            handler,
            filter_match_distance=0.5,
            detector="sift",
            matching="BF",
            stereo_matcher="sgbm",
            mask=mask,
            subset=None,
        )
        end = datetime.datetime.now()
        print("Time to perform odometry:", end - start)
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection="3d")

        ax.plot(
            trajectory_nolidar_bm[:, :, 3][:, 0],
            trajectory_nolidar_bm[:, :, 3][:, 1],
            trajectory_nolidar_bm[:, :, 3][:, 2],
            label="estimated",
            color="orange",
        )

        ax.plot(
            handler.gt[:, :, 3][:, 0],
            handler.gt[:, :, 3][:, 1],
            handler.gt[:, :, 3][:, 2],
            label="ground truth",
        )

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")

        ax.view_init(elev=-20, azim=270)
        plt.show()

    if 0:
        image_left = handler.first_image_left
        image_right = handler.first_image_right
        image_plus1 = handler.second_image_left
        depth = stereo_2_depth(image_left, image_right, handler.P0, handler.P1, matcher="bm", verbose=True)
        kp0, des0 = extract_features(image_left, "sift")
        kp1, des1 = extract_features(image_plus1, "sift")
        matches = match_features(des0, des1, matching="BF", detector="sift", sort=True)
        print("Number of matches before filtering:", len(matches))
        matches = filter_matches_distance(matches, 0.3)
        print("Number of matches after filtering:", len(matches))
        visualize_matches(image_left, kp0, image_plus1, kp1, matches)
