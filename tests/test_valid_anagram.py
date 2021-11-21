# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.strings.Anagram import Anagram


class TestStack(unittest.TestCase):

    def test_valid_anagram_not_null(self):
        self.assertIsNotNone(Anagram())

    def test_valid_anagram(self):
        self.assertTrue(Anagram.is_anagram("anagram", "nagaram"))
        self.assertFalse(Anagram.is_anagram("rat", "car"))
