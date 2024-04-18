"""Class for keypoint based registration"""
import os
import unittest
import math
from copy import deepcopy
import numpy as np
import cv2

from ignutils.registration.register_abstract import RegisterAbstract
from ignutils.show_utils import show, fuse


class KeypointRegister(RegisterAbstract):
    """ECC transform based registration"""

    def __init__(
        self,
        config_path,
        show_flag=False,
        print_flag=False,
    ):
        super().__init__(config_path, show_flag, print_flag)
        self.nfeatures = self.config("nfeatures")
        self.scale_factor = self.config("scaleFactor")
        self.nlevels = self.config("nlevels")
        self.edge_threshold = self.config("edgeThreshold")
        self.first_level = self.config("firstLevel")
        self.wta_k = self.config("WTA_K")
        self.patch_size = self.config("patchSize")
        self.fast_threshold = self.config("fastThreshold")
        self.score_type = cv2.FAST_FEATURE_DETECTOR_TYPE_9_16
        self.ratio_thresh = self.config("ratioThresh")
        self.min_matches = self.config("minMatches")
        self.orb = cv2.ORB_create(
            nfeatures=self.nfeatures, scaleFactor=self.scale_factor, nlevels=self.nlevels, edgeThreshold=self.edge_threshold, firstLevel=self.first_level, WTA_K=self.wta_k, scoreType=self.score_type, patchSize=self.patch_size, fastThreshold=self.fast_threshold
        )

    def get_main_config(self):
        """ECC register default config creation"""
        config = {
            "register type": {"value": "keypoint", "choices": ["ecc", "keypoint", "superglue"], "hint": "Registration type"},
            "nfeatures": {"value": 5000, "choices": None, "hint": "The number of iterations to be done"},
            "scaleFactor": {"value": 1.2, "choices": None, "hint": "Pyramid decimation ratio"},
            "nlevels": {"value": 2, "choices": None, "hint": "An optional value indicating size of gaussian blur filter"},
            "edgeThreshold": {"value": 22, "choices": None, "hint": "Size of the border where the features are not detected"},
            "firstLevel": {"value": 0, "choices": None, "hint": "The level of pyramid to put source image to"},
            "WTA_K": {"value": 2, "choices": None, "hint": "The number of points that produce each element of the oriented BRIEF descriptor"},
            "patchSize": {"value": 29, "choices": None, "hint": "Size of the patch used by the oriented BRIEF descriptor"},
            "fastThreshold": {"value": 2, "choices": None, "hint": "the fast threshold"},
            "ratioThresh": {"value": 0.75, "choices": None, "hint": "Lowe's ratio threshold"},
            "minMatches": {"value": 4, "choices": None, "hint": "Minimum no of good matches"},
        }

        return config

    def get_child_configs(self):
        """Child config abstract method override"""
        child_configs = []

        return child_configs

    def register(
        self,
        fixed_img,
        moving_img,
        nfeatures=None,
        fixed_kp=None,
        fixed_des=None,
        fixed_roi=(-1, -1, -1, -1),
        moving_roi=(-1, -1, -1, -1),
        prev_y_shift=None,
        x_y_diff_based=False,
        homography_prev=None,
        vertical_only=False,
        essent_mat_based=False
    ):
        """Register given fixed and moving images"""
        kp1_shift_flag = False
        kp2_shift_flag = False

        if nfeatures is not None:
            self.nfeatures = nfeatures

        if fixed_kp is not None and fixed_des is not None:  # Old key points available
            kp2, des2 = fixed_kp, fixed_des
            # ROI based shift for fixed
            if fixed_roi != (-1, -1, -1, -1):
                for _, kp2_ in enumerate(kp2):
                    kp2_.pt = (kp2_.pt[0] - fixed_roi[0], kp2_.pt[1] - fixed_roi[1])
                kp2_shift_flag = True


        # Old key points not available, If roi, use roi for fixed crop
        elif fixed_roi != (-1, -1, -1, -1):
            x1, y1, x2, y2 = fixed_roi
            fixed_img = fixed_img[y1:y2, x1:x2, :]
            kp2, des2 = self.orb.detectAndCompute(fixed_img, None)
            kp2_shift_flag = True

        else:  # Detect & compute on full fixed (old kp, roi not available)
            kp2, des2 = self.orb.detectAndCompute(fixed_img, None)

        # Prev shift based shifting
        if prev_y_shift is not None:
            for _, kp2_ in enumerate(kp2):
                kp2_.pt = (kp2_.pt[0], kp2_.pt[1] - prev_y_shift)

        if moving_roi != (-1, -1, -1, -1):  # If roi, use roi for moving crop
            x1, y1, x2, y2 = moving_roi
            moving_img = moving_img[y1:y2, x1:x2, :]
            kp1_shift_flag = True

        kp1, des1 = self.orb.detectAndCompute(moving_img, None)

        if kp1_shift_flag:  # Reversing ROI based shift for fixed
            for _, kp1_ in enumerate(kp1):
                kp1_.pt = (kp1_.pt[0] + moving_roi[0], kp1_.pt[1] + moving_roi[1])

        if kp2_shift_flag:  # Reversing ROI based shift for moving
            for _, kp2_ in enumerate(kp2):
                kp2_.pt = (kp2_.pt[0] + fixed_roi[0], kp2_.pt[1] + fixed_roi[1])

        if self.show_flag:
            fixed_kp = cv2.drawKeypoints(fixed_img, kp1, None, color=(0, 255, 0))
            moving_kp = cv2.drawKeypoints(moving_img, kp2, None, color=(0, 255, 0))
            show(fixed_kp, win="fixed_kp", time=30, destroy=False)
            show(moving_kp, win="moving_kp", time=30, destroy=False)

        flann = cv2.BFMatcher()
        src_points = None
        dst_points = None
        good_matches = []
        if des1 is not None and des2 is not None:
            matches = flann.knnMatch(des1, des2, k=2)

            if x_y_diff_based:
                src_points, dst_points, good_matches = self.x_y_diff_based(kp1, kp2, matches)

            elif homography_prev is not None:
                src_points, dst_points, good_matches = self.get_homography_based_inliers(kp1, kp2, matches, homography_prev, vertical_only)

            elif essent_mat_based:
                src_points, dst_points, good_matches = self.essent_mat_based(kp1, kp2, matches)

            else:
                src_points, dst_points, good_matches = self.lowes_ratio_based(kp1, kp2, matches)

        if src_points is not None and dst_points is not None:
            mat = self.get_transformation_matrix(src_points, dst_points)
            moved = self.get_transformed_img(moving_img, fixed_img.shape[0], fixed_img.shape[1], mat)
            if mat is not None:
                if self.print_flag:
                    print("**current y shift", mat[1][2])

                # Reversing Prev shift based shifting
                if mat is not None and prev_y_shift is not None:
                    mat[1][2] += prev_y_shift

        else:
            if self.print_flag:
                print("registration failed!")
            moved = None
            mat = None

        if self.show_flag and len(good_matches) > 0:
            fixed_org = deepcopy(fixed_img)
            moving_org = deepcopy(moving_img)

            if mat is not None:
                if fixed_roi != (-1, -1, -1, -1):
                    x1, y1, x2, y2 = fixed_roi
                    fixed = fixed_org[y1:y2, x1:x2, :]
                else:
                    fixed = fixed_org
                moved = cv2.warpPerspective(moving_img, mat, (fixed.shape[1], fixed.shape[0]))
                fused_image = fuse(fixed, moved)
                show(fused_image, win="fused_image", time=30, destroy=False)

            res = np.empty(
                (
                    max(moving_org.shape[0], fixed_org.shape[0]),
                    moving_org.shape[1] + fixed_org.shape[1],
                    3,
                ),
                dtype=np.uint8,
            )

            im_matches = cv2.drawMatches(moving_org, kp1, fixed_org, kp2, good_matches, res)
            show(im_matches, win="im matches", time=0, destroy=False)

        return moved, mat, kp1, des1

    def lowes_ratio_based(self, kp1, kp2, matches):
        """Filter matches using the Lowe's ratio test"""
        good_matches = []
        src_points = None
        dst_points = None
        for (m, n) in matches:
            if m.distance < self.ratio_thresh * n.distance:
                good_matches.append(m)

        if len(good_matches) > self.min_matches:
            src_points = np.array([kp1[m.queryIdx].pt for m in good_matches], dtype=np.float32).reshape((-1, 1, 2))
            dst_points = np.array([kp2[m.trainIdx].pt for m in good_matches], dtype=np.float32).reshape((-1, 1, 2))

        return src_points, dst_points, good_matches

    def x_y_diff_based(self, kp1, kp2, matches):
        """Get matches based on x and y differences"""
        good_matches = []
        src_points = None
        dst_points = None
        for (m, n) in matches:
            if m.distance < self.ratio_thresh * n.distance:
                mx = kp1[m.queryIdx].pt[0]
                my = kp1[m.queryIdx].pt[1]
                nx = kp2[n.trainIdx].pt[0]
                ny = kp2[n.trainIdx].pt[1]
                x_diff = abs(nx - mx)
                y_diff = ny - my

                if x_diff < 20 and 300 > y_diff > -300:
                    if self.print_flag:
                        print("x_y_diff_based DIFFERENCES: ", x_diff, y_diff)
                    good_matches.append(m)

        if len(good_matches) > self.min_matches:
            src_points = np.array([kp1[m.queryIdx].pt for m in good_matches], dtype=np.float32).reshape((-1, 1, 2))
            dst_points = np.array([kp2[m.trainIdx].pt for m in good_matches], dtype=np.float32).reshape((-1, 1, 2))

        return src_points, dst_points, good_matches

    def get_homography_based_inliers(self, kp1, kp2, matches, homography_prev, vertical_only):
        """Distance threshold to identify inliers with homography check"""
        matched1 = []
        matched2 = []
        good_matches = []
        inliers1 = []
        inliers2 = []
        inlier_threshold = 100
        x_thresh = 30
        y_thresh = 100
        src_points = None
        dst_points = None

        for (m, n) in matches:
            if m.distance < self.ratio_thresh * n.distance:
                matched1.append(kp1[m.queryIdx])
                matched2.append(kp2[m.trainIdx])

        for i, m in enumerate(matched1):
            kpt0 = np.ones((3, 1), dtype=np.float64)
            kpt0[0:2, 0] = m.pt
            kpt1 = np.dot(homography_prev, kpt0)
            kpt2 = kpt1 / kpt1[2, 0]

            if vertical_only:
                x_diff = abs(kpt1[0][0]) - abs(matched2[i].pt[0])
                y_diff = abs(kpt1[1][0]) - abs(matched2[i].pt[1])

                if abs(y_diff) < y_thresh or abs(x_diff) < x_thresh:
                    dist = 0
                else:
                    dist = np.inf
            else:
                dist = math.sqrt(pow(kpt2[0, 0] - matched2[i].pt[0], 2) + pow(kpt2[1, 0] - matched2[i].pt[1], 2))

            if dist < inlier_threshold:
                good_matches.append(cv2.DMatch(len(inliers1), len(inliers2), 0))
                inliers1.append(matched1[i])
                inliers2.append(matched2[i])

        if len(good_matches) > self.min_matches:
            src_points = np.array([inliers1[m.queryIdx].pt for m in good_matches], dtype=np.float32).reshape((-1, 1, 2))
            dst_points = np.array([inliers2[m.trainIdx].pt for m in good_matches], dtype=np.float32).reshape((-1, 1, 2))

        return src_points, dst_points, good_matches

    def essent_mat_based(self, kp1, kp2, matches, camera_mat=None):
        """Filter keypoints based on Motion estimation from two images (from matching points in two images)"""
        src_points = None
        dst_points = None
        good_matches = []
        # place matched opencv keypoints' coordinaites in an array of [x,y] positions
        a_mkp1 = np.array([list(kp1[m.queryIdx].pt) for (m, _) in matches])
        a_mkp2 = np.array([list(kp2[m.trainIdx].pt) for (m, _) in matches])

        if camera_mat is None:
            camera_mat = np.eye(3)
            camera_mat[0, 0] = 7.070912000000e02  # focal x
            camera_mat[1, 1] = 7.070912000000e02  # focal y
            camera_mat[0:2, 2] = [6.018873000000e02, 1.831104000000e02]  # principal point [cx, cy]

        # estimate Essential matrix, then decompose it in order to recover R and t
        e_mat, mask = cv2.findEssentialMat(a_mkp1, a_mkp2, camera_mat, method=cv2.RANSAC)
        print(f"Estimated essential matrix: {e_mat}")
        print(f"Number of inliers after RANSAC = {np.count_nonzero(mask)}")
        nbinliers, rot, trans, mask2 = cv2.recoverPose(e_mat, a_mkp1, a_mkp2, camera_mat, mask=mask.copy())
        print(f"Estimated rotation: {rot}")
        print(f"Estimated translation: {trans}")
        print(f"Number of inliers after rot, trans estimation: {nbinliers}")

        # lists of inliers kp
        if nbinliers > self.min_matches:
            src_points = a_mkp1[np.all(mask2 == 1, axis=1)]
            dst_points = a_mkp2[np.all(mask2 == 1, axis=1)]

        return src_points, dst_points, good_matches

    def get_optical_flow_kp(self, fixed_img, moving_img, kp1):
        """Optical flow based keypoint detection"""
        # Parameters for lucas kanade optical flow
        lk_params = {"winSize": (15, 15),
                    "maxLevel": 2,
                    "criteria": (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)}
        # Create some random colors
        color = np.random.randint(0, 255, (100, 3))
        fixed_gray = cv2.cvtColor(fixed_img, cv2.COLOR_BGR2GRAY)
        moving_gray = cv2.cvtColor(moving_img, cv2.COLOR_BGR2GRAY)
        # calculate optical flow
        kp2, s_t, _ = cv2.calcOpticalFlowPyrLK(fixed_gray, moving_gray, kp1, None, **lk_params)
        # Select good points
        if kp2 is not None:
            kp2 = kp2[s_t==1]
            kp1 = kp1[s_t==1]

        if self.show_flag:
            # draw the tracks
            mask = np.zeros_like(fixed_img)
            for i, (new, old) in enumerate(zip(kp2, kp1)):
                a, b = new.ravel()
                c, d = old.ravel()
                mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), color[i].tolist(), 2)
                frame = cv2.circle(moving_img, (int(a), int(b)), 5, color[i].tolist(), -1)
            img = cv2.add(frame, mask)
            cv2.imshow('frame', img)

        # compute the descriptors with ORB
        kp1, des1 = self.orb.compute(fixed_img, kp1)
        kp2, des2 = self.orb.compute(moving_img, kp2)

        return kp1, kp2, des1, des2

class TestKeypointRegistration(unittest.TestCase):
    """Unit test for keypoint registration"""

    @classmethod
    def setUpClass(cls):
        cls.fixed_img_ = cv2.imread(os.path.join("samples", "kitti_fixed.jpg"))
        cls.moving_img_ = cv2.imread(os.path.join("samples", "kitti_moving.jpg"))
        cls.reg_obj = KeypointRegister(os.path.join("samples", "keypoint_config.yaml"), False, True)

    @classmethod
    def write_and_assert(cls, moved, mat, out_mat):
        """Common func for writing and asserting the results"""
        fused_img = fuse(cls.fixed_img_, moved)
        cv2.imwrite(os.path.join("samples", "test_results", "keypoint_moved.jpg"), moved)
        cv2.imwrite(os.path.join("samples", "test_results", "keypoint_fused.jpg"), fused_img)
        assert np.array_equal(np.int_(mat), np.int_(out_mat)), "Output matrix not matching with expected result"

    def test_lowes_based(self):
        """Test default keypoint register method based on lowe's ratio"""
        moved, mat, _, _ = self.reg_obj.register(self.fixed_img_, self.moving_img_)
        out_mat = np.array([[ 1.04136419e+00,  1.97502596e-02, -2.97142582e+01],
                            [-7.11924428e-04,  9.86491677e-01,  1.53473420e+00],
                            [-1.39546873e-05,  1.32628574e-05,  1.00000000e+00]], dtype=np.float32)
        self.write_and_assert(moved, mat, out_mat)

    # def test_optical_flow_based(self):
    #     """Test deafult keypoint register method by calc kp based on optical flow"""
    #     moved, mat, _, _ = self.reg_obj.register(self.fixed_img_, self.moving_img_, get_optical_flow_kp=True)
    #     out_mat = np.array([[ 1.04136419e+00,  1.97502596e-02, -2.97142582e+01],
    #                         [-7.11924428e-04,  9.86491677e-01,  1.53473420e+00],
    #                         [-1.39546873e-05,  1.32628574e-05,  1.00000000e+00]], dtype=np.float32)
    #     self.write_and_assert(moved, mat, out_mat)

    def test_homography_based(self):
        """Test keypoint register by giving previous homography as input"""
        homography_prev = np.array([[ 1.04136419e+00,  1.97502596e-02, -2.97142582e+01],
                                    [-7.11924428e-04,  9.86491677e-01,  1.53473420e+00],
                                    [-1.39546873e-05,  1.32628574e-05,  1.00000000e+00]], dtype=np.float32)
        moved, mat, _, _ = self.reg_obj.register(self.fixed_img_, self.moving_img_, homography_prev=homography_prev)
        out_mat = np.array([[ 9.63149826e-01, -1.31592114e-01,  1.46818159e+01],
                            [-1.62480253e-03,  9.28897398e-01,  3.35277754e+00],
                            [-4.55273903e-05, -1.47193654e-04,  1.00000000e+00]], dtype=np.float32)
        self.write_and_assert(moved, mat, out_mat)

    def test_essen_mat_based(self):
        """Test keypoint register method based on essential matrix filtering"""
        moved, mat, _, _ = self.reg_obj.register(self.fixed_img_, self.moving_img_, essent_mat_based=True)
        out_mat = np.array([[ 7.40648530e-01, -1.49664953e-01,  8.91383389e+01],
                            [-2.40459453e-02,  8.06348418e-01,  2.06352391e+01],
                            [-1.88989793e-04, -2.57981689e-04,  1.00000000e+00]], dtype=np.float32)
        self.write_and_assert(moved, mat, out_mat)

    def test_x_y_diff_based(self):
        """Test deafult keypoint register method based on x y difference"""
        moved, mat, _, _ = self.reg_obj.register(self.fixed_img_, self.moving_img_, x_y_diff_based=True)
        out_mat = np.array([[ 8.54971292e-01, -1.97295218e-01,  5.84401682e+01],
                            [-1.39831576e-02,  8.57069858e-01,  1.45545988e+01],
                            [-1.09177623e-04, -2.36510452e-04,  1.00000000e+00]], dtype=np.float32)
        self.write_and_assert(moved, mat, out_mat)

if __name__ == "__main__":
    test_obj = TestKeypointRegistration()
