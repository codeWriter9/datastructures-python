# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.array.PlusOne import PlusOne


class TestStack(unittest.TestCase):

    def test_plus_one_not_null(self):
        self.assertIsNotNone(PlusOne())

    def test_plus_one(self):
        self.assertEqual([1], PlusOne.plus_one([0]))
        self.assertEqual([1, 0], PlusOne.plus_one([9]))
        self.assertEqual([1, 2, 4], PlusOne.plus_one([1, 2, 3]))
        self.assertEqual([1, 0, 0, 0], PlusOne.plus_one([9, 9, 9]))
        self.assertEqual([1, 1, 2], PlusOne.plus_one([1, 1, 1]))
        self.assertEqual([2, 0, 0], PlusOne.plus_one([1, 9, 9]))

