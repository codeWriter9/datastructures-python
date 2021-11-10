# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.array.RemoveDuplicates import RemoveDuplicates


class TestStack(unittest.TestCase):

    def test_remove_duplicates_not_null(self):
        self.assertIsNotNone(RemoveDuplicates())

    def test_remove_duplicates(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected = [0, 1, 2, 3, 4, 0, 1, 1, 2, 3, 3]
        k = RemoveDuplicates.remove_duplicates(nums)
        for i in range(0, k, 1):
            assert nums[i] == expected[i]
