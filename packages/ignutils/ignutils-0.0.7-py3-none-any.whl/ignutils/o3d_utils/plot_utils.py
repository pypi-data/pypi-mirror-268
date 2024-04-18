"""Plot Utils"""
import open3d as o3d


def get_pcd_from_color_depth(color_img, depth_img, intrinsic_matrix, show=False):
    """Given a color image and a depth image, and intrinsic matrix of a camera, this function returns a point cloud
    representation of the 3D scene captured by the camera"""
    color_raw = o3d.geometry.Image(color_img)
    depth_raw = o3d.geometry.Image(depth_img)
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw)
    intrinsic_params = o3d.camera.PinholeCameraIntrinsic(width=640, height=400, fx=intrinsic_matrix[0][0], fy=intrinsic_matrix[1][1], cx=intrinsic_matrix[0][2], cy=intrinsic_matrix[1][2])
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, intrinsic_params)

    if show:
        o3d.visualization.draw_geometries([pcd])
    return pcd


def xyz_to_pcd(points, show=True):
    """plot 3d points
    Args:
        points (np.array): array of xyz points
    Returns:
        open3d point cloud: point cloud data to visualize
    """
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    if show:
        o3d.visualization.draw_geometries([pcd])
    return [pcd]
