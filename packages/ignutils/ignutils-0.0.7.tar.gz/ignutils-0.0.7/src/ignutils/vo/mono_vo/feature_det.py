"""IvLabs, VNIT
MONOCULAR VISUAL ODOMETRY ON KITTI DATASET

TEAM MEMBERS:
1. Arihant Gaur
2. Saurabh Kemekar
3. Aman Jain
"""

import cv2
import numpy as np

# from ignutils.show_utils import show


class featureDet: # pylint: disable=too-few-public-methods
    """Class for feature detection"""
    def __init__(self, FeatureDetectMethod="FAST", show_flag=False): #pylint: disable=unused-argument
        self.FeatureDetectMethod = FeatureDetectMethod

    def FeatureDetection(self, img0gray):
        """Feature detecton"""
        if self.FeatureDetectMethod == "FAST":
            featuredetect = cv2.FastFeatureDetector_create(threshold=25, nonmaxSuppression=True)
            kp0 = featuredetect.detect(img0gray)
            kp0 = np.array([kp0[idx].pt for idx in range(len(kp0))], dtype=np.float32)
        elif self.FeatureDetectMethod == "SIFT":
            featuredetect = cv2.xfeatures2d.SIFT_create()
            kp0, des0 = featuredetect.detectAndCompute(img0gray, None)
            kp0 = np.array([kp0[idx].pt for idx in range(len(kp0))], dtype=np.float32)
        elif self.FeatureDetectMethod == "SURF":
            featuredetect = cv2.xfeatures2d.SURF_create()
            kp0, des0 = featuredetect.detectAndCompute(img0gray, None)
            kp0 = np.array([kp0[idx].pt for idx in range(len(kp0))], dtype=np.float32)

        elif self.FeatureDetectMethod == "ORB":
            score_type = cv2.FAST_FEATURE_DETECTOR_TYPE_9_16
            featuredetect = cv2.ORB_create(
                nfeatures=5000,
                scaleFactor=1.2,
                nlevels=2,
                edgeThreshold=22,
                firstLevel=0,
                WTA_K=2,
                scoreType=score_type,
                patchSize=29,
                fastThreshold=2,
            )
            kp0, des0 = featuredetect.detectAndCompute(img0gray, None)
            kp0 = np.array([kp0[idx].pt for idx in range(len(kp0))], dtype=np.float32)
        return kp0
