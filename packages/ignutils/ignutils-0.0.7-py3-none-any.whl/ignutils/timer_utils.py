"""To do tic toc to check time spent."""

import time
import unittest

class Timer:
    """Get time in seconds, also provide tic-toc for checking execution time for process"""

    def __init__(self): # removed unused argument - ref_time=None
        self.tictime = {}

    def tic(self, index=0):
        """start time of index item"""
        self.tictime[index] = time.time()

    def toc(self, index=0, text="Time elapsed:", precision=6):
        """toc"""
        diff = time.time() - self.tictime[index]
        print(f"{text}{index} : " + str(round(diff, ndigits=precision)) + " seconds")
        return diff


class TestTimer(unittest.TestCase):
    """Test method"""

    def test_tic_toc(self):
        """Testing tic toc"""
        tc = Timer()
        tc.tic(2)
        time.sleep(1)
        diff = tc.toc(2, text="Time elapsed")
        assert round(diff) == 1, "Time difference is not 1 second"


if __name__ == "__main__":
    test_obj = TestTimer()
    test_obj.test_tic_toc()
