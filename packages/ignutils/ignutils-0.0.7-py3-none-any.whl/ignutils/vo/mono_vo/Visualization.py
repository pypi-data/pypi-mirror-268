"""IvLabs, VNIT
MONOCULAR VISUAL ODOMETRY ON KITTI DATASET

TEAM MEMBERS:
1. Arihant Gaur
2. Saurabh Kemekar
3. Aman Jain
"""

import math

import cv2
import numpy as np
import open3d as o3d


def drawOpticalFlowField(img, ref_pts, cur_pts):
    """drawOpticalFlowField"""
    for i, (new, old) in enumerate(zip(cur_pts, ref_pts)):
        x, y = old.ravel()
        v1 = tuple((new - old) * 2.5 + old)
        d_v = [new - old][0] * 0.75
        arrow_color = (0, 0, 255)
        arrow_t1 = rotateFunct([d_v], 0.5)
        arrow_t2 = rotateFunct([d_v], -0.5)
        tip1 = tuple(np.array([x, y], dtype=np.float32) + arrow_t1)[0]
        tip2 = tuple(np.array([x, y], dtype=np.float32) + arrow_t2)[0]
        cv2.line(img, v1, (x, y), (0, 0, 255), 2)
        cv2.line(img, (x, y), tip1, arrow_color, 2)
        cv2.line(img, (x, y), tip2, arrow_color, 2)
        cv2.circle(img, v1, 1, (0, 255, 0), -1)
    return img


def rotateFunct(pts_l, angle, degrees=False):
    """rotateFunct"""
    if degrees == True:
        theta = math.radians(angle)
    else:
        theta = angle

    R = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
    rot_pts = []
    for v in pts_l:
        v = np.array(v).transpose()
        v = R.dot(v)
        v = v.transpose()
        rot_pts.append(v)

    return rot_pts


def plot_trajectory(image, x, y, t):
    text = "x = {}    y = {}    z = {}".format(t[0, 0], t[1, 0], t[2, 0])

    # cv2.putText(image, "Prediction", (200, 90), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2, 8)
    # cv2.rectangle(image, (0, 0), (950, 70), (0, 0, 0), cv2.FILLED)
    # cv2.putText(image, text, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, 8)
    cv2.circle(image, (int(x) + 500, 1000 - int(y)), 3, (0, 0, 255))
    return image


def plot_ground_truth(window, x, z):
    cv2.putText(window, "Ground_truth", (10, 90), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2, 8)
    cv2.circle(window, (int(x), 700 - int(z)), 3, (0, 255, 0))
    return window

def plot_trajectory_o3d(points):
    # Create a list of 3D points (replace these with your own points)
    # points = np.array([
    #     [t[0, 0], t[1, 0], t[2, 0]]
    # ])

    

    # Create a point cloud from the list of points
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)

    

    # Create lines connecting the points for the curve
    lines_curve = []
    for i in range(len(points) - 1):
        lines_curve.append([i, i + 1])

    

    # Create a line set to represent the curve
    line_set_curve = o3d.geometry.LineSet()
    line_set_curve.points = point_cloud.points
    line_set_curve.lines = o3d.utility.Vector2iVector(lines_curve)

    

    # Create lines for coordinate axes
    axis_length = 200.0
    # x_axis = [[0, 0], [axis_length, 0]]
    x_axis_1 = [[0, 0, 0], [axis_length, 0, 0]]
    # print(x_axis_1.shape)
    # exit()
    # y_axis = [[0, 0], [0, axis_length]]
    y_axis_1 = [[0, 0, 0], [0, axis_length, 0]]
    # z_axis = [[0, 0], [0, 0, axis_length]]
    z_axis_1 = [[0, 0, 0], [0, 0, axis_length]]

    

    # Create line sets for the coordinate axes
    line_set_x_axis = o3d.geometry.LineSet()
    # print(type(x_axis))
    line_set_x_axis.points = o3d.utility.Vector3dVector(x_axis_1)
    line_set_x_axis.lines = o3d.utility.Vector2iVector([[0, 1]])

    

    line_set_y_axis = o3d.geometry.LineSet()
    line_set_y_axis.points = o3d.utility.Vector3dVector(y_axis_1)
    line_set_y_axis.lines = o3d.utility.Vector2iVector([[0, 1]])

    

    line_set_z_axis = o3d.geometry.LineSet()
    line_set_z_axis.points = o3d.utility.Vector3dVector(z_axis_1)
    line_set_z_axis.lines = o3d.utility.Vector2iVector([[0, 1]])

    

    # Create a visualization window
    o3d.visualization.draw_geometries([line_set_curve, line_set_x_axis, line_set_y_axis, line_set_z_axis])
