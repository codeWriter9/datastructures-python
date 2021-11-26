# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.linkedlist.ReverseNode import ReverseNode
from algorithms.linkedlist.ListNode import ListNode


class TestStack(unittest.TestCase):

    def test_reverse_list_not_null(self):
        self.assertIsNotNone(ListNode(0))
        self.assertIsNotNone(ReverseNode())

    def test_reverse_list(self):
        """
        More than 1 element
        """
        head = ListNode.nodes([0, 1, 2, 3])
        self.assertEqual([3, 2, 1, 0], ReverseNode.reverse_list(head).to_list())
        """
        Empty
        """
        head = None
        self.assertEqual(None, ReverseNode.reverse_list(None))
        """
        1 element
        """
        head = ListNode.nodes([0])
        self.assertEqual([0], ReverseNode.reverse_list(head).to_list())

    def test_reverse_list_recursive(self):
        """
        More than 1 element
        """
        head = ListNode.nodes([0, 1, 2, 3])
        self.assertEqual([3, 2, 1, 0], ReverseNode.reverse_list_recursive(head).to_list())
        """
        Empty
        """
        head = None
        self.assertEqual(None, ReverseNode.reverse_list_recursive(None))
        """
        1 element
        """
        head = ListNode.nodes([0])
        self.assertEqual([0], ReverseNode.reverse_list_recursive(head).to_list())
