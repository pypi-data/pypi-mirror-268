""" Keyboard utilities"""
import unittest
from pynput import keyboard


class KeyboardListen:
    """A class that listens to keyboard events"""

    def __init__(self) -> None:
        """initialising key listener"""
        self.listener = None
        self.key = None

    def on_press(self, key):
        """ A callback function that is called when a key is pressed"""
        if hasattr(key, "char"):
            print(f"alphanumeric key {key.char} pressed")  # .format(key.char))
            self.key = key.char
        else:
            print(f"special key {key} pressed")  # .format(key))
            self.key = key

    def on_release(self, key):
        """ A callback function that is called when a key is released"""
        print(f"{key} released")
        # if key == keyboard.Key.esc:
        if key:
            # Stop listener
            return False
        return True

    def wait_for_click(self):
        """ Waits for the user to press a key and returns the key"""
        # ...or, in a non-blocking fashion:
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        print("waiting for keyboard click...")
        self.listener.join()
        print("return key:", self.key)
        return self.key


class TestKeyBoardUtils(unittest.TestCase):
    """Testing Keyboard utilities"""

    def test_keyboard_listen(self):
        """testing key board listen"""
        key_check = KeyboardListen()
        key = key_check.wait_for_click()
        print("got key:", key)


if __name__ == "__main__":
    test_obj = TestKeyBoardUtils()
    test_obj.test_keyboard_listen()
