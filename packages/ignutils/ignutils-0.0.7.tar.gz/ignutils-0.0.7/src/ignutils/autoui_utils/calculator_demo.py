""" Calculator testing demo"""
import os
import time

import pyautogui
import Xlib.display
from easyprocess import EasyProcess
from pyvirtualdisplay import Display

from ignutils.mouse_utils import MouseListen
from ignutils.keyboard_utils import KeyboardListen
from ignutils.autoui_utils.autogui_utils import compare_imgs

PATH = os.path.dirname(os.path.abspath(__file__))


def main(manual_click=False, visible=False):
    """Demo calculator ui test"""
    screen_w = 1920
    screen_h = 1080
    os.makedirs("screens", exist_ok=True)

    display = Display(visible=visible, backend="xephyr", size=(screen_w, screen_h))
    display.start()
    pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ["DISPLAY"])
    print("Screen size:", pyautogui.size())

    proc = EasyProcess(["gnome-calculator"])  # start()
    proc.start()
    proc.sleep(1)

    im1 = pyautogui.screenshot()
    im1.save("screens/ui_screen1.png")

    # Get mouse click
    if manual_click:
        mouse_check = MouseListen()
        pos = mouse_check.wait_for_mouse()
        x1, y1 = pos[0], pos[1]
    else:
        x1, y1 = 1630, 337

    # replay mouse click
    # pos = pyautogui.position()
    pyautogui.moveTo(x=10, y=10, duration=0.2)
    pyautogui.moveTo(x=x1, y=y1, duration=0.2)
    pyautogui.click()

    # Get keyboard click
    if manual_click:
        key_check = KeyboardListen()
        key = key_check.wait_for_click()
        print("got key:", key)
    else:
        key = "1"

    # replay keyboard click
    pyautogui.press(key)

    # Crop click roi from pre screenshot
    area = (x1 - 50, y1 - 50, x1 + 50, y1 + 50)
    cropped_img = im1.crop(area)
    # cropped_img.show()
    cropped_img.save("screens/pre_mouse_click.png")

    # Locating roi image
    pre_click_imgp = os.path.join(PATH, "pre_mouse_click1.png")
    loc = pyautogui.locateOnScreen(pre_click_imgp, minSearchTime=2, confidence=0.99)
    print("located:", loc)

    im3 = pyautogui.screenshot(region=loc)
    im3.save("screens/located.png")

    pos = pyautogui.center(loc)
    print("pos:", pos)
    pyautogui.moveTo(x=pos.x, y=pos.y)
    pyautogui.click()

    im2 = pyautogui.screenshot()
    im2.save("screens/ui_screen2.png")
    match = compare_imgs(pre_click_imgp, "screens/located.png", thresh=0.99)
    print("match:", match)
    assert match, "screens should match"

    time.sleep(1)

    proc.stop()
    display.stop()


if __name__ == "__main__":
    main(manual_click=False, visible=False)
