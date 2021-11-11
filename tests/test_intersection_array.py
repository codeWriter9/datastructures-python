# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.array.IntersectionArray import IntersectionArray


class TestStack(unittest.TestCase):

    def test_intersection_array_not_null(self):
        self.assertIsNotNone(IntersectionArray())

    def test_intersection_array(self):
        # self.assertEqual([2, 2], IntersectionArray.intersect([1, 2, 2, 1], [2, 2]))
        # self.assertEqual([4, 9], IntersectionArray.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
        self.assertEqual([1], IntersectionArray.intersect([3, 1, 2], [1, 1]))
