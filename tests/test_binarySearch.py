# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.array.BinarySearch import BinarySearch


class TestStack(unittest.TestCase):

    def test_array_binarySearchNotNull(self):
        self.assertIsNotNone(BinarySearch())

    def test_array_BinarySearch(self):
        self.assertEqual(2, BinarySearch.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
        self.assertEqual(-1, BinarySearch.search([-1, 0, 3, 5, 9, 12], 2))
