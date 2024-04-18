"""Contins binarry search algorithms."""
import unittest


def binary_search(input_arr, x):
    "Returns the index of x in the given array input_arr, or -1 if not found."
    low = 0
    high = len(input_arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if input_arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half
        elif input_arr[mid] > x:
            high = mid - 1
        # means x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1


def binary_search_lower(input_arr, x):
    """Returns the index of the next lowest number of given x."""
    low = 0
    high = len(input_arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if input_arr[mid] < x:
            if (mid + 1) <= high and input_arr[mid + 1] > x or mid == high:
                return mid
            low = mid + 1
        # If x is smaller, ignore right half
        elif input_arr[mid] > x:
            if input_arr[mid] == input_arr[low]:
                return mid
            high = mid - 1
        # means x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1


def binary_search_upper(input_arr, x):
    """Returns the index of the next greatest number of given x"""
    low = 0
    low1 = 0
    high = len(input_arr) - 1
    high1 = len(input_arr) - 1
    mid = (high + low) // 2
    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if input_arr[mid] < x:
            if input_arr[mid] == input_arr[high1]:
                return mid
            low = mid + 1
        # If x is smaller, ignore right half
        elif input_arr[mid] > x:
            if (mid - 1) >= low1 and input_arr[mid - 1] < x or mid == low1:
                return mid
            high = mid - 1
        # means x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1

class TestAlgoUtils(unittest.TestCase):
    """unit test case for a set of functions related to algorithms"""

    @classmethod
    def setUpClass(cls):
        cls.arr_ = [2, 3, 4, 10, 40]

    @classmethod
    def tearDownClass(cls):
        print("teardown")

    def test_binary_search(self):
        """It asserts that the function correctly returns the index of the element being searched for in the array.
        If the element is not found, the test fails."""
        x = 10
        result = binary_search(self.arr_, x)
        if result != -1:
            print("Element is present at index", str(result))
        else:
            print("Element is not present in array")
        assert result == 3

    def test_binary_search_lower(self):
        """It asserts that the function correctly returns the index of the
        largest element in the array that is less than or equal to the element being searched for.
        If there is no such element in the array, the test fails."""
        x = 2
        result = binary_search_lower(self.arr_, x)
        if result != -1:
            print("Element is present at index", str(result))
        else:
            print("Element is not present in array")
        assert result == 0

    def test_binary_search_upper(self):
        """It asserts that the function correctly returns the index of the
        smallest element in the array that is greater than or equal to the element being searched for.
        If there is no such element in the array, the test fails"""
        x = 3.5
        result = binary_search_upper(self.arr_, x)
        if result != -1:
            print("Element is present at index", str(result))
        else:
            print("Element is not present in array")
        assert result == 2


if __name__ == "__main__":
    test_obj = TestAlgoUtils()
    test_obj.setUpClass()
    test_obj.test_binary_search()
    test_obj.test_binary_search_lower()
    test_obj.test_binary_search_upper()
