# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.array.TwoSum import TwoSum


class TestStack(unittest.TestCase):

    def test_two_sum_not_null(self):
        self.assertIsNotNone(TwoSum())

    def test_two_sum(self):
        self.assertEqual([0, 1], TwoSum.two_sum([2, 7, 11, 15], 9))
        self.assertEqual([1, 2], TwoSum.two_sum([3, 2, 4], 6))
        self.assertEqual([0, 1], TwoSum.two_sum([3, 3], 6))

