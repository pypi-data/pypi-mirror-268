""" auto ui record and playback for testing desktop applications"""
import argparse
import collections
import json
import os
import subprocess
import logging
import time

import pyautogui
import Xlib.display
from pynput.keyboard import Controller as KeyboardController
from pynput import keyboard as keyboard_monitor
from pynput import mouse as mouse_monitor
from pynput.keyboard import Key
from pynput.mouse import Button
from pynput.mouse import Controller as MouseController
from pyvirtualdisplay import Display
from loguru import logger
from ignutils.autoui_utils.autogui_utils import compare_mse, compare_img_size
from ignutils.file_utils import remove_directory
from ignutils.clone_utils import CloneRepo


class Recplayback:
    """Record and Playback"""

    # python = sys.executable
    mouse = MouseController()
    keyboard = KeyboardController()
    Box = collections.namedtuple("Box", "left top width height")

    def __init__(self, recordname, db_name, displaysize, commandline, check):
        self.count = 0
        self.screenshot_path = self.create_screenshot_directory(db_name, args.recordname)
        logger.success(displaysize)
        self.recordname = recordname
        self.exit_flag = False
        self.storage = []
        self.screen_width = int(displaysize[0])
        self.screen_height = int(displaysize[1])
        self.application_flag = False
        self.region = self.Box(left=0, top=0, width=self.screen_width, height=self.screen_height)
        self.move_record_flag = True
        self.mouse_listener = None
        self.keyboard_listener = None
        self.proc = None

    def create_screenshot_directory(self, folder_name, recodname):
        """Create a directory"""
        self.screenshot_path = os.path.join("autogui_db", folder_name, recodname)
        if os.path.isdir("autogui_db"):
            print("autogui_db")
        else:
            os.makedirs("autogui_db", exist_ok=False)
        if os.path.isdir(self.screenshot_path):
            print("isExist", self.screenshot_path)
            remove_directory(self.screenshot_path)
        os.makedirs(self.screenshot_path, exist_ok=False)
        print("create", self.screenshot_path)
        return self.screenshot_path

    def get_sample_videos(self, dst_path="workspace/sample_videos", pull_flag=True):
        """Download sample videos"""
        git_url = "https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db"
        db_branch = "herzog_sample_videos"
        CloneRepo(git_url, db_branch, dst_path, stash_flag=pull_flag, pull_flag=pull_flag, access_token_name="DB_CLONE_TOKEN")

    def subprocess_logger(self, proc, text):
        """Process log"""
        while True:
            output = proc.stdout.readline()
            if output == b"" and proc.poll() is not None:
                logger.info("app exited break")
                break
            if output:
                out = output.decode()
                logger.info(out, end="")
                if text in out:
                    break
            if self.exit_flag:
                break
            time.sleep(0.1)

    def on_keyboard_press(self, key):
        """keyboard Press event"""
        try:
            json_object = {"action": "key_press", "key": key.char, "_time": time.time()}
            self.storage.append(json_object)
        except AttributeError:
            if key == keyboard_monitor.Key.f6:
                with open(f"autogui_db/record_screen/{self.recordname}/record.json", "w", encoding="UTF-8") as outfile:
                    json.dump(self.storage, outfile)
                self.exit_flag = True
                pos = pyautogui.position()
                # print("pos",pos.x)
                # subprocess.call(["xdotool", "mousemove", f"{pos.x+1}", f"{pos.y+1}"])
                # self.mouse.move=(pos.x+1,pos.y+1)
                self.mouse_listener.stop()
                return False

            json_object = {"action": "key_press", "key": str(key), "_time": time.time()}
            self.storage.append(json_object)

    def on_keybaord_release(self, key):
        """keyboard release"""
        try:
            json_object = {"action": "key_release", "key": key.char, "_time": time.time()}
        except AttributeError:
            json_object = {"action": "key_release", "key": str(key), "_time": time.time()}
        self.storage.append(json_object)

    def on_mouse_move(self, x, y):
        """Mouse move"""
        if self.exit_flag:
            return False
        if self.move_record_flag:
            if len(self.storage) >= 1:
                if self.storage[-1]["action"] != "moved":
                    json_object = {
                        "action": "moved",
                        "x": x,
                        "y": y,
                        "_time": time.time(),
                    }
                    self.storage.append(json_object)
                elif self.storage[-1]["action"] == "moved" and time.time() - self.storage[-1]["_time"] > 0.02:
                    json_object = {
                        "action": "moved",
                        "x": x,
                        "y": y,
                        "_time": time.time(),
                    }
                    self.storage.append(json_object)
            else:
                json_object = {"action": "moved", "x": x, "y": y, "_time": time.time()}
                self.storage.append(json_object)
        else:
            if len(self.storage) >= 1:
                if (self.storage[-1]["action"] == "mouse_press" and self.storage[-1]["button"] == "Button.left") or (self.storage[-1]["action"] == "moved" and time.time() - self.storage[-1]["_time"] > 0.02):
                    json_object = {
                        "action": "moved",
                        "x": x,
                        "y": y,
                        "_time": time.time(),
                    }
                    self.storage.append(json_object)
        # return True

    def mouse_callback(self, x, y, button, mouse_press):
        """Mouse Click event handler"""
        if self.exit_flag:
            return False
        # print("mouse_press",mouse_press)
        if mouse_press:
            if str(button) == "Button.right":
                crop_img = pyautogui.screenshot(region=(x - 50, y - 50, 100, 100))
                crop_img.save(os.path.join(self.screenshot_path, f"screen{str(self.count).zfill(3)}.jpg"))
                print(str(button))
                self.count += 1
        json_object = {
            "action": "mouse_press" if mouse_press else "mouse_release",
            "button": str(button),
            "x": x,
            "y": y,
            "_time": time.time(),
        }
        self.storage.append(json_object)
        if len(self.storage) > 1:
            print("-", json_object["button"])

    def on_mouse_scroll(self, x, y, dx, dy):
        """Mouse scroll event handler"""
        json_object = {
            "action": "scroll",
            "vertical_direction": int(dy),
            "horizontal_direction": int(dx),
            "x": x,
            "y": y,
            "_time": time.time(),
        }
        self.storage.append(json_object)

    def get_recording_data(self):
        """retun test json data"""
        name_of_recording = "autogui_db/record_screen/" + self.recordname + "/record.json"
        # number_of_plays = 1 #int(sys.argv[2])
        with open(name_of_recording, encoding="utf-8") as json_file:
            data = json.load(json_file)
        return data

    def get_special_keys(self, input_key):
        """Special Keys"""
        key_list = {
            "Key.shift": Key.shift,
            "Key.tab": Key.tab,
            "Key.caps_lock": Key.caps_lock,
            "Key.ctrl": Key.ctrl,
            "Key.alt": Key.alt,
            "Key.cmd": Key.cmd,
            "Key.cmd_r": Key.cmd_r,
            "Key.alt_r": Key.alt_r,
            "Key.ctrl_r": Key.ctrl_r,
            "Key.shift_r": Key.shift_r,
            "Key.enter": Key.enter,
            "Key.backspace": Key.backspace,
            "Key.f19": Key.f19,
            "Key.f18": Key.f18,
            "Key.f17": Key.f17,
            "Key.f16": Key.f16,
            "Key.f15": Key.f15,
            "Key.f14": Key.f14,
            "Key.f13": Key.f13,
            "Key.media_volume_up": Key.media_volume_up,
            "Key.media_volume_down": Key.media_volume_down,
            "Key.media_volume_mute": Key.media_volume_mute,
            "Key.media_play_pause": Key.media_play_pause,
            "Key.f6": Key.f6,
            "Key.f5": Key.f5,
            "Key.right": Key.right,
            "Key.down": Key.down,
            "Key.left": Key.left,
            "Key.up": Key.up,
            "Key.page_up": Key.page_up,
            "Key.page_down": Key.page_down,
            "Key.home": Key.home,
            "Key.end": Key.end,
            "Key.delete": Key.delete,
            "Key.space": Key.space,
            "Key.esc": Key.esc,
        }
        return key_list[input_key]

    def playback(self, virtual_display):
        """It will start process and playback the mouse and
        keyboard events from the recorded json"""

        full_screen_play_path = os.path.join(self.screenshot_path, "fullscreen.jpg")
        full_screen_play = pyautogui.screenshot()
        full_screen_play.save(full_screen_play_path)
        fullscreen_record_path = os.path.join("autogui_db/record_screen", self.recordname, "fullscreen.jpg")
        is_compare = compare_img_size(fullscreen_record_path, full_screen_play_path)
        assert is_compare, "initial screen size not matching"
        match = True
        record = self.get_recording_data()
        first_press = True
        for index, obj in enumerate(record):
            action, _time = obj["action"], obj["_time"]
            try:
                next_movement = record[index + 1]["_time"]
                pause_time = next_movement - _time
            except IndexError as e:
                pause_time = 1
            pause_time = min(0.2, pause_time)

            if action == "key_press" or action == "key_release":
                key = obj["key"] if "Key." not in obj["key"] else self.get_special_keys(input_key=obj["key"])
                if action == "key_press":
                    print("key:", key)
                    if key == Key.esc:
                        if virtual_display is False:
                            self.keyboard.press(key)
                            self.keyboard.release(key)
                        else:
                            subprocess.call(["xdotool", "key", "Escape"])
                        time.sleep(0.1)
                    else:
                        if virtual_display is False:
                            self.keyboard.press(key)
                        else:
                            if key == Key.enter:
                                subprocess.call(["xdotool", "keydown", "KP_Enter"])
                            else:
                                subprocess.call(["xdotool", "keydown", f"{key}"])
                else:
                    if key != Key.esc:
                        if virtual_display is False:
                            self.keyboard.release(key)
                        else:
                            if key == Key.enter:
                                subprocess.call(["xdotool", "keyup", "KP_Enter"])
                            else:
                                subprocess.call(["xdotool", "keyup", f"{key}"])
                        time.sleep(pause_time)
            else:
                move_for_scroll = True
                x, y = obj["x"], obj["y"]
                if action == "scroll" and index > 0 and (record[index - 1]["action"] == "mouse_press" or record[index - 1]["action"] == "mouse_release"):
                    if x == record[index - 1]["x"] and y == record[index - 1]["y"]:
                        move_for_scroll = False
                if virtual_display:
                    subprocess.call(["xdotool", "mousemove", f"{x}", f"{y}"])
                else:
                    self.mouse.position = (x, y)
                if action == "mouse_press" or action == "mouse_release" or action == "scroll" and move_for_scroll is True:
                    time.sleep(0.1)
                if action == "mouse_press":
                    if virtual_display:
                        if obj["button"] == "Button.left":
                            subprocess.call(["xdotool", "mousedown", "1"])
                        else:
                            recorded_path = os.path.join(
                                "autogui_db",
                                "record_screen",
                                self.recordname,
                                f"screen{str(self.count).zfill(3)}.jpg",
                            )
                            detected_path = os.path.join(
                                self.screenshot_path,
                                f"screen{str(self.count).zfill(3)}.jpg",
                            )
                            # while True:
                            if first_press:
                                mintime = 120
                                first_press = False
                            else:
                                mintime = 5
                            start = time.time()
                            im_screen = pyautogui.locateOnScreen(
                                recorded_path,
                                minSearchTime=mintime,
                                grayscale=True,
                                confidence=0.9,
                            )
                            logger.info(f"Locate time:{time.time() - start}")
                            im_3 = pyautogui.screenshot(region=im_screen)
                            im_3.save(detected_path)
                            logger.info(f"im_screen:{im_screen}")
                            match = compare_mse(detected_path, recorded_path)
                            logger.info(f"match-{self.count}:{match}")
                            if match is False:
                                logger.info(f"screen{str(self.count).zfill(3)}.jpg not match with recorded")
                                break
                            self.count += 1
                            subprocess.call(["xdotool", "mousedown", "3"])
                    else:
                        self.mouse.press(Button.left if obj["button"] == "Button.left" else Button.right)
                elif action == "mouse_release":
                    if virtual_display:
                        if obj["button"] == "Button.left":
                            subprocess.call(["xdotool", "mouseup", "1"])
                        else:
                            subprocess.call(["xdotool", "mouseup", "3"])
                    else:
                        self.mouse.release(Button.left if obj["button"] == "Button.left" else Button.right)

                elif action == "scroll":
                    horizontal_direction, vertical_direction = (
                        obj["horizontal_direction"],
                        obj["vertical_direction"],
                    )
                    if virtual_display:
                        if vertical_direction == 1:
                            subprocess.call(["xdotool", "click", "4"])
                        elif vertical_direction == -1:
                            subprocess.call(["xdotool", "click", "5"])
                    else:
                        self.mouse.scroll(horizontal_direction, vertical_direction)
                time.sleep(pause_time)

        if match is True:
            logger.info("match passed!")
        else:
            logger.error("proc_log:", self.proc)
        assert match is True, "match failed"

    def run(self, commandline, visible, virtual_display, is_play, check):
        """virtual display properties"""

        gui_display_size = pyautogui.size()
        pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ["DISPLAY"])
        logger.info(f"Virtual Display:{gui_display_size}")
        logger.info(f"User screen size:{self.screen_width, self.screen_height}")
        if virtual_display:
            logging.getLogger("easyprocess").setLevel(logging.INFO)
            with Display(
                visible=visible,
                backend="xephyr",
                size=(self.screen_width, self.screen_height),
            ) as display:
                logger.success("started vr")
                commandline = commandline.split()
                self.proc = subprocess.Popen(commandline, env=os.environ, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                if check is not None:
                    self.subprocess_logger(self.proc, text=check)
                if is_play:
                    self.playback(virtual_display)
                    display.stop()
                else:
                    self.record()
                    display.stop()
        else:
            commandline = commandline.split()
            self.proc = subprocess.Popen(commandline, env=os.environ, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if check is not None:
                self.subprocess_logger(self.proc, text=check)
            if is_play:
                self.playback(virtual_display)
            else:
                self.record()

    def record(self):
        """Start recording"""
        full_screen = pyautogui.screenshot()
        full_screen.save(os.path.join(self.screenshot_path, "fullscreen.jpg"))
        self.keyboard_listener = keyboard_monitor.Listener(on_press=self.on_keyboard_press, on_release=self.on_keybaord_release)
        self.mouse_listener = mouse_monitor.Listener(
            on_click=self.mouse_callback,
            on_scroll=self.on_mouse_scroll,
            on_move=self.on_mouse_move,
        )
        self.keyboard_listener.start()
        self.mouse_listener.start()
        logger.info("To exit, close the test application, press f6 and move mouse")
        while True:
            output = self.proc.stdout.readline()
            if output == b"" and self.proc.poll() is not None:
                logger.info("app exited, press f6 and move mouse")
                break
            if self.exit_flag:
                break
            if output:
                out = output.decode()
                logger.info(out)

        self.mouse_listener.join()
        self.keyboard_listener.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r",
        "--recordname",
        default="test_infer",
        type=str,
        help="enter the name of the recorded test ",
    )
    parser.add_argument(
        "-cmd",
        "--commandline",
        default="main.py -l workspace/sample_videos/set1/left/19991231_202610_NF_Passenger_Rear.mp4 -r workspace/sample_videos/set1/right/20211109_030954_NF_DriverRear.mp4 -loc workspace/sample_videos/set1/locations.csv -cam CAM_set1 -sfl 0 -sfr 30 -d -fc 15  -id -gps -p",
        type=str,
        help="command line to run the application you want to test",
    )
    parser.add_argument(
        "-v",
        "--visible",
        default=True,
        nargs="?",
        const=True,
        help="To show image during test",
    )
    parser.add_argument(
        "-vr",
        "--virtual_display",
        default=False,
        nargs="?",
        const=True,
        help="Use virtual display for server test",
    )
    parser.add_argument(
        "-pl",
        "--playback",
        default=False,
        nargs="?",
        const=True,
        help="Play or record",
    )
    parser.add_argument(
        "-ds",
        "--displaysize",
        default="1920x1080",
        type=str,
        help="enter size of the display",
    )
    parser.add_argument(
        "-check",
        "--logcheck",
        default=None,
        type=str,
        help="Log to check for before starting rec/playback",
    )
    args = parser.parse_args()
    print(args)
    if args.playback:
        play_back = Recplayback(args.recordname, db_name="playback_screen", displaysize=args.displaysize.split("x"), commandline=args.commandline, check=args.logcheck)
        play_back.run(args.commandline, args.visible, args.virtual_display, is_play=args.playback, check=args.logcheck)
    else:
        rec_playback = Recplayback(args.recordname, db_name="record_screen", displaysize=args.displaysize.split("x"), commandline=args.commandline, check=args.logcheck)
        rec_playback.run(args.commandline, args.visible, args.virtual_display, is_play=args.playback, check=args.logcheck)
