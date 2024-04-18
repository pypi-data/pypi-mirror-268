"""
    Extract images from a rosbag.
    Download sample rosbag file from: https://ignitariumtech-my.sharepoint.com/personal/mohammed_k_ignitarium_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fmohammed_k_ignitarium_com%2FDocuments%2FLidar_expe_setup%2Fcamera_data%2F2022-07-22-15-11-10%2Ebag&parent=%2Fpersonal%2Fmohammed_k_ignitarium_com%2FDocuments%2FLidar_expe_setup%2Fcamera_data&ga=1
    python read_rosbag.py --bag_file 2022-07-22-15-11-10.bag --output_dir output/ --image_topic '/rgb_stereo_publisher/color/image'
    python read_rosbag.py --bag_file 2022-07-22-15-11-10.bag --output_dir output/ --image_topic '/rgb_stereo_publisher/stereo/depth'
"""

import os
import argparse

import cv2
import rosbag
from cv_bridge import CvBridge


def bag_to_images(bag_file, output_dir, image_topic, resize=False):
    """Extract a folder of images from a rosbag.
    Args:
        bag_file (bag_file): Input ROS bag
        output_dir (str): Output directory
        image_topic (str): single image topic or list of topics
        resize (bool): resize the extracted image
    """
    print(f"Extract images from {bag_file} on topic {image_topic} into {output_dir}")
    # Create output directory if doesnt exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    bag = rosbag.Bag(bag_file, "r")
    bridge = CvBridge()
    print("Total Duration:", bag.get_end_time() - bag.get_start_time(), "sec")

    # print all the topics info
    topics = bag.get_type_and_topic_info()[1].keys()
    print(f"\nAvailable topics in bag file are:{topics}")

    # Total frames in topic
    total_frames = bag.get_message_count(image_topic)
    print(f"\nTotal frames in bag file are:{total_frames}")

    # Info about each topic types
    # types=[]
    # for i in range(0,len(bag.get_type_and_topic_info()[1].values())):
    #     types.append(bag.get_type_and_topic_info()[1].values())
    # print("\nTypes are: {}".format(types))

    for topic, msg, t in bag.read_messages(topics=[image_topic]):
        print(f"Size of the image: W {msg.width} x H {msg.height}")
        print(f"Encoding of the frames: {msg.encoding}")
        break

    basename = os.path.splitext(os.path.basename(bag_file))[0]
    count = 0

    for topic, msg, t in bag.read_messages(topics=[image_topic]):
        cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
        if resize:
            cv_img = cv2.resize(cv_img, (640, 400))
        p = os.path.join(output_dir, basename)
        p = p + f"_{count:05}" + ".jpg"
        cv2.imwrite(os.path.join(output_dir, f"frame{count:06}.png"), cv_img)
        print("Wrote image {count}")
        count += 1

    bag.close()
    print("extracted images")
    # return

def argument_parser():
    """Argument Parser"""
    parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")
    parser.add_argument("--bag_file", help="Input ROS bag.")
    parser.add_argument("--output_dir", help="Output directory.")
    parser.add_argument("--image_topic", help="single image topic or list of topics")
    return parser.parse_args()

def main():
    """Main Function"""
    args = argument_parser()
    bag_file = args.bag_file
    output_dir = args.output_dir
    image_topic = args.image_topic
    bag_to_images(bag_file, output_dir, image_topic, resize=True)


if __name__ == "__main__":
    main()
    