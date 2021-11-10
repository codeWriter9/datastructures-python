# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.array.SingleNumber import SingleNumber


class TestStack(unittest.TestCase):

    def test_single_number_not_null(self):
        self.assertIsNotNone(SingleNumber())

    def test_single_number(self):
        self.assertEqual(2, SingleNumber.single_number([1, 1, 2, 3, 3, 4, 4]))
        self.assertEqual(1, SingleNumber.single_number([1, 2, 2, 3, 3]))

