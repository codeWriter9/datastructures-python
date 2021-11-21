# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.strings.Palindrome import Palindrome


class TestStack(unittest.TestCase):

    def test_valid_palindrome_not_null(self):
        self.assertIsNotNone(Palindrome())

    def test_valid_palindrome(self):
        self.assertTrue(Palindrome.is_palindrome("malayalam"))
        self.assertTrue(Palindrome.is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(Palindrome.is_palindrome("Sanjay"))
        self.assertFalse(Palindrome.is_palindrome("race a car"))
        self.assertTrue(Palindrome.is_palindrome(" "))

