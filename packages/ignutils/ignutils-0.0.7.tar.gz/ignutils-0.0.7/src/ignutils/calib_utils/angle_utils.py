"""Module to calculate angular matrices"""
import math
import numpy as np


def euler_angles_to_rotation_matrix(theta):
    """Calculates Rotation Matrix given euler angles"""
    r_x = np.array([[1, 0, 0], [0, math.cos(theta[0]), -math.sin(theta[0])], [0, math.sin(theta[0]), math.cos(theta[0])]])
    r_y = np.array([[math.cos(theta[1]), 0, math.sin(theta[1])], [0, 1, 0], [-math.sin(theta[1]), 0, math.cos(theta[1])]])
    r_z = np.array([[math.cos(theta[2]), -math.sin(theta[2]), 0], [math.sin(theta[2]), math.cos(theta[2]), 0], [0, 0, 1]])
    r_mat = np.dot(r_z, np.dot(r_y, r_x))

    return r_mat


def is_rotation_matrix(r_mat):
    """Checks if a matrix is a valid rotation matrix."""
    rt = np.transpose(r_mat)
    should_be_identity = np.dot(rt, r_mat)
    i = np.identity(3, dtype=r_mat.dtype)
    n = np.linalg.norm(i - should_be_identity)
    return n < 1e-6


def rotation_matrix_to_euler(r_mat):
    """Calculates rotation matrix to euler angles"""
    assert is_rotation_matrix(r_mat)
    sy = math.sqrt(r_mat[0, 0] * r_mat[0, 0] + r_mat[1, 0] * r_mat[1, 0])
    singular = sy < 1e-6

    if not singular:
        x = math.atan2(r_mat[2, 1], r_mat[2, 2])
        y = math.atan2(-r_mat[2, 0], sy)
        z = math.atan2(r_mat[1, 0], r_mat[0, 0])
    else:
        x = math.atan2(-r_mat[1, 2], r_mat[1, 1])
        y = math.atan2(-r_mat[2, 0], sy)
        z = 0

    return np.array([x, y, z])
