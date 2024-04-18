"""To handle basic open3d and point cloud based registration functions"""
import os
import copy
import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt

np.set_printoptions(precision=1, suppress=True)


def get_rgbd_image(color_img_path, depth_img_path, show_flag=False):
    """To get RGBD image from raw color image and depth image
    Args:
        color_img_path (str): path for the color image
        depth_img_path (str): path for the depth image
        show_flag (bool, optional): to show the color and depth image from rgbd object. Defaults to False.
    Returns:
        open3d.geometry.RGBDImage : RGBD image (pair of color and depth image with same view and resolution)
    """
    color_raw = o3d.io.read_image(color_img_path)
    depth_raw = o3d.io.read_image(depth_img_path)
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw)
    if show_flag:
        plt.subplot(1, 2, 1)
        plt.title("Redwood grayscale image")
        plt.imshow(rgbd_image.color)
        plt.subplot(1, 2, 2)
        plt.title("Redwood depth image")
        plt.imshow(rgbd_image.depth)
        plt.show()
    return rgbd_image


def get_pcd_from_rgbd(rgdb_img, intrinsic_matrix=None, show_flag=False):
    """To get the point cloud data from the RGBD image
    Args:
        rgdb_img (open3d.geometry.RGBDImage): RGBD image object
        intrinsic_params (open3d.camera.PinholeCameraIntrinsic, ndarray): PinholeCameraIntrinsic class stores intrinsic camera matrix, and image height and width.. Defaults to None.
        show_flag (bool, optional): to show the point cloud image. Defaults to False.
    Returns:
        open3d.geometry.PointCloud: point cloud data
    """
    if intrinsic_matrix is None:
        intrinsic_params = o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault
    else:
        intrinsic_params = o3d.camera.PinholeCameraIntrinsic(width=640, height=400, fx=intrinsic_matrix[0][0], fy=intrinsic_matrix[1][1], cx=intrinsic_matrix[0][2], cy=intrinsic_matrix[1][2])
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgdb_img, o3d.camera.PinholeCameraIntrinsic(intrinsic_params))
    # Flip it, otherwise the pointcloud will be upside down
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    if show_flag:
        o3d.visualization.draw_geometries([pcd])
    return pcd


def draw_registration_result(source, target, transformation_matrix):
    """To visualize the point cloud registration output
    Args:
        source (open3d.geometry.PointCloud): source point cloud data
        target (open3d.geometry.PointCloud): target point cloud data
        transformation_matrix (numpy.ndarray): The 4x4 transformation matrix to transform source to target
    """
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation_matrix)
    o3d.visualization.draw_geometries([source_temp, target_temp])


def evaluate_registration(source, target, distance_threshold=0.02, transform_matrix=None, show_flag=False):
    """To evaluate registration of source and target point cloud data
    Args:
        source (open3d.geometry.PointCloud): source pcd data
        target (open3d.geometry.PointCloud): target pcd data
        distance_threshold (float, optional): Maximum correspondence points-pair distance. Defaults to 0.02.
        transform_matrix (numpy.ndarray, optional): The 4x4 transformation matrix to transform source to target. Defaults to None.
        show_flag (bool, optional): to show the point cloud image. Defaults to False.
    Returns:
        open3d.pipelines.registration.RegistrationResult: registration result metrics
    """
    if show_flag:
        draw_registration_result(source, target, transform_matrix)
    evaluation = o3d.pipelines.registration.evaluate_registration(source, target, distance_threshold, transform_matrix)
    print(evaluation)
    return evaluation


def apply_icp_registration(source, target, distance_threshold=0.02, transform_matrix=None, transform_method=None, show_flag=False):
    """To apply ICP (Iterative Closest Point) registration given a source, target pcd data and transformation matrix
    Args:
        source (open3d.geometry.PointCloud): source pcd data
        target (open3d.geometry.PointCloud): target pcd dataw
        distance_threshold (float, optional): Maximum correspondence points-pair distance. Defaults to 0.02.
        transform_matrix (numpy.ndarray, optional): The 4x4 transformation matrix to transform source to target. Defaults to None.
        transform_method (open3d.pipelines.registration.TransformationEstimation, optional): Transformation Estimation method. Defaults to None.
        show_flag (bool, optional): to show the point cloud image. Defaults to False.

    Returns:
        open3d.pipelines.registration.RegistrationResult: registration result metrics
    """
    reg_out = o3d.pipelines.registration.registration_icp(source, target, distance_threshold, transform_matrix, transform_method)

    print(reg_out)
    print("Transformation is:")
    print(reg_out.transformation)
    print("")

    if show_flag:
        draw_registration_result(source, target, reg_out.transformation)
    return reg_out

def main():
    """Main Function"""
    if 0:  # Example based on open3d data
        # Get Sample Redwood dataset paths from open3d data
        redwood_rgbd = o3d.data.SampleRedwoodRGBDImages()
        color_img_path = redwood_rgbd.color_paths[0]
        depth_img_path = redwood_rgbd.depth_paths[0]
        rgbd_img = get_rgbd_image(color_img_path, depth_img_path)
        point_cloud_data = get_pcd_from_rgbd(rgbd_img)

        # Get Sample icp point cloud dataset paths from open3d data
        demo_icp_pcds = o3d.data.DemoICPPointClouds()
        source_path = demo_icp_pcds.paths[0]
        target_path = demo_icp_pcds.paths[1]
        source_pcd = o3d.io.read_point_cloud(source_path)
        target_pcd = o3d.io.read_point_cloud(target_path)

        trans_init = np.asarray([[0.862, 0.011, -0.507, 0.5], [-0.139, 0.967, -0.215, 0.7], [0.487, 0.255, 0.835, -1.4], [0.0, 0.0, 0.0, 1.0]])
        print("Initial alignment")
        reg_evaluation = evaluate_registration(source_pcd, target_pcd, transform_matrix=trans_init, show_flag=False)
        print("Apply point-to-point ICP")
        transform_method = o3d.pipelines.registration.TransformationEstimationPointToPoint()
        registration_res = apply_icp_registration(source_pcd, target_pcd, transform_matrix=trans_init, transform_method=transform_method, show_flag=False)
        print("Apply point-to-plane ICP")
        transform_method = o3d.pipelines.registration.TransformationEstimationPointToPlane()
        registration_res = apply_icp_registration(source_pcd, target_pcd, transform_matrix=trans_init, transform_method=transform_method, show_flag=False)

    if 1:  # Example with custom data
        # Reading from the example folder
        color_paths = []
        depth_paths = []
        for root, dirs, files in os.walk(os.path.abspath("./examples/rgb/")):
            for file in files:
                color_paths.append(os.path.join(root, file))
        for root, dirs, files in os.walk(os.path.abspath("./examples/depth/")):
            for file in files:
                depth_paths.append(os.path.join(root, file))
        color_img_path = color_paths[0]
        depth_img_path = depth_paths[0]
        rgbd_img = get_rgbd_image(color_img_path, depth_img_path)
        source_pcd = get_pcd_from_rgbd(rgbd_img)

        color_img_path = color_paths[1]
        depth_img_path = depth_paths[1]
        rgbd_img = get_rgbd_image(color_img_path, depth_img_path)
        target_pcd = get_pcd_from_rgbd(rgbd_img)

        # Starting with unit transformation matrix
        trans_init = np.asarray([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]])
        print("Initial alignment")
        reg_evaluation = evaluate_registration(source_pcd, target_pcd, transform_matrix=trans_init, show_flag=False)
        print("Apply point-to-point ICP")
        transform_method = o3d.pipelines.registration.TransformationEstimationPointToPoint()
        registration_res = apply_icp_registration(source_pcd, target_pcd, transform_matrix=trans_init, transform_method=transform_method, show_flag=False)



if __name__ == "__main__":
    main()
    