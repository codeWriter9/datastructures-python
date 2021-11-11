# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.array.RotateArray import RotateArray


class TestStack(unittest.TestCase):

    def test_rotate_array_not_null(self):
        self.assertIsNotNone(RotateArray())

    def test_rotate_array(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        RotateArray.rotate(array, 3)
        self.assertEqual([5, 6, 7, 1, 2, 3, 4], array)
        array = [-1, -100, 3, 99]
        RotateArray.rotate(array, 2)
        self.assertEqual([3, 99, -1, -100], array)
