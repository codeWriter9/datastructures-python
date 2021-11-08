# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.dp.MaxSubArray import MaxSubArray


class TestStack(unittest.TestCase):

    def test_max_sub_array_not_null(self):
        self.assertIsNotNone(MaxSubArray())

    def test_max_sub_array(self):
        self.assertEqual(6, MaxSubArray.max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(23, MaxSubArray.max_sub_array([5, 4, -1, 7, 8]))
