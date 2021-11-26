# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.linkedlist.Palindrome import Palindrome
from algorithms.linkedlist.ListNode import ListNode


class TestStack(unittest.TestCase):

    def test_palindrome_list_not_null(self):
        self.assertIsNotNone(ListNode(0))
        self.assertIsNotNone(Palindrome())

    def test_palindrome_list(self):
        self.assertEqual([4, 3, 2, 1, 0], Palindrome.reverse(ListNode.nodes([0, 1, 2, 3, 4])).to_list())
        self.assertEqual([1, 2, 2, 1], Palindrome.reverse(ListNode.nodes([1, 2, 2, 1])).to_list())
        self.assertTrue(Palindrome.is_palindrome(ListNode.nodes([1, 2, 2, 1])))
        self.assertTrue(Palindrome.is_palindrome(ListNode.nodes([1, 2, 3, 2, 1])))
        self.assertFalse(Palindrome.is_palindrome(ListNode.nodes([0, 1, 2, 3, 4, 5])))
