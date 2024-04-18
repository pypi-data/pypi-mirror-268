import numpy as np


def getTransform(cur_pose, prev_pose):

        """
        Computes the error of the transformation between 2 poses
        """

        Rt = np.eye(4)
        Rt[:3,:3] = cur_pose[:3,:3].T @ prev_pose[:3, :3]
        Rt[:3, -1] = cur_pose[:3, :3].T @ (cur_pose[:3,-1] - prev_pose[:3, -1])

        return Rt


def convert_to_4_by_4(Rt):

    try:
        assert Rt.shape==(3,4)
    except:
        print(Rt.shape)
        raise AssertionError("Input Matrix form should be of 3x4")

    return np.vstack((Rt, np.array([0,0,0,1])))

def convert_to_Rt(R,t):
    
    """
    converts to 3x4 transformation matrix
    """

    return np.hstack((R, t.reshape(-1,1)))