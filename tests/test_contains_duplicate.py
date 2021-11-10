# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.array.ContainsDuplicate import ContainsDuplicate


class TestStack(unittest.TestCase):

    def test_contains_duplicates_not_null(self):
        self.assertIsNotNone(ContainsDuplicate())

    def test_contains_duplicates(self):
        self.assertTrue(ContainsDuplicate.containsDuplicate([1, 1, 2, 3, 3, 4, 5]))
        self.assertFalse(ContainsDuplicate.containsDuplicate([1, 2, 3, 4, 5]))
