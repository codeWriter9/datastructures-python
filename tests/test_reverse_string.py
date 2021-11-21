# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.strings.ReverseString import ReverseString


class TestStack(unittest.TestCase):

    def test_reverse_string_not_null(self):
        self.assertIsNotNone(ReverseString())

    def test_reverse_string(self):
        name = ['J', 'o', 'h', 'n']
        ReverseString.reverse_string(name)
        self.assertEqual(['n', 'h', 'o', 'J'], name)

    def test_reverse_string_0(self):
        name = ['F', 'u', 'l', 'c', 'r', 'u', 'm']
        ReverseString.reverse_string(name)
        self.assertEqual(['m', 'u', 'r', 'c', 'l', 'u', 'F'], name)

    def test_reverse_string_1(self):
        name = []
        ReverseString.reverse_string(name)
        self.assertEqual([], name)
