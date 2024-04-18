"""
Functions for automatic testing of ui.
"""

import time
import os
import cv2
import pyautogui as gui
import numpy as np
from loguru import logger
# from ignutils.registration.motion2D2D import find_match_


def compare_imgs(imgp1, imgp2, thresh=0.99):
    """compare two images for being same or not"""
    img1 = cv2.imread(imgp1)
    img2 = cv2.imread(imgp2)
    if img1.shape == img2.shape:
        diff = img1 - img2
        print("diff:", diff)
        count = np.count_nonzero(diff)
        if count < img1.shape[0] * img1.shape[1] * thresh:
            return True
        print("compare imgs diff count:", count)
    print("compare imgs shape mismatch shape:", img1.shape, img2.shape)
    return False


def compare_img_size(imgp1, imgp2):
    """compare two images for same shape"""
    img1 = cv2.imread(imgp1)
    img2 = cv2.imread(imgp2)
    logger.info(f"shape recorded:{img1.shape}")
    logger.info(f"shape playback:{img2.shape}")
    if img1.shape == img2.shape:
        return True
    return False


# def get_image_position_orb(img_path):
#     """orb based image matching and return xy location on screen"""

#     im1 = cv2.imread(img_path)
#     im2 = gui.screenshot("screenshots/screen.png")
#     im2 = np.array(im2)
#     m, dst_pts = find_match_(im1, im2)
#     if dst_pts:
#         return np.mean(dst_pts)
#     return None


def compare_mse(image1, image2, thresh=30):
    """mse based image similarity comparison"""
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    # convert the images to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    try:
        mse, diff = calc_mse(img1, img2)
        logger.info(f"MSE Value:{mse}")
        return bool(mse < thresh)
    except Exception as e:
        logger.error(f"MSE Error:{e}")


def calc_mse(img1, img2):
    """mean squared error"""
    h, w = img1.shape
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff**2)
    mse = err / (float(h * w))
    return mse, diff


def get_image_position(img_path, region, confidence=0.99, timeout=20):
    """Return the image position on find the matching image before the specified timeout."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        x_y = gui.locateOnScreen(img_path, confidence, region=region)
        if x_y is not None:
            return x_y
        time.sleep(1)
    return None


def wait_click(img_path, key=None, timeout=5, confidence=0.6):
    """wait for finding img clip in window, mouse click at position,
    press the key too if any is given.
    key - None, 'esc',
    """
    os.makedirs("screenshots", exist_ok=True)
    pos = get_image_position(img_path, timeout=timeout, confidence=confidence)
    if pos is not None:
        print(f"{os.path.basename(img_path)} detected!")
        pos = gui.center(pos)
        im1 = gui.screenshot("screenshots/screen.png", region=(pos.x - 50, pos.y - 50, 100, 100))
        # gui.hotkey('ctrl', 'shift')
        gui.click(pos.x, pos.y)
        if key:
            gui.press(key)
    else:
        raise Exception(f"{os.path.basename(img_path)} not found...")
    return pos


def testfirefox():
    """Demo of firefox testing"""
    screenWidth, screenHeight = gui.size()
    gui.moveTo(10, screenHeight)
    gui.click()
    gui.typewrite("Firefox", interval=0.25)
    gui.press("enter")
    time.sleep(3)
    gui.keyDown("alt")
    gui.press(" ")
    gui.press("x")
    gui.keyUp("alt")
    gui.click(250, 22)
    gui.click(371, 51)
    gui.typewrite("https://medium.com/financeexplained")
    gui.press("enter")


if __name__ == "__main__":
    if 0:
        testfirefox()
    if 1:
        compare_mse("/home/sarank/ign_utils/Projects/LR_Stitcher/playback_screen/test_infer1/screen000.png", "/home/sarank/ign_utils/Projects/LR_Stitcher/record_screen/test_infer1/screen000.png")
