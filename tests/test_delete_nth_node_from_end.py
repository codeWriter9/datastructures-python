# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.linkedlist.DeleteNthNodeFromEnd import DeleteNthNodeFromEnd
from algorithms.linkedlist.ListNode import ListNode


class TestStack(unittest.TestCase):

    def test_delete_node_not_null(self):
        self.assertIsNotNone(ListNode(0))
        self.assertIsNotNone(DeleteNthNodeFromEnd())

    def test_delete_node(self):
        """
                head
        """
        head = ListNode.nodes([0, 1, 2, 3])
        self.assertEqual([1, 2, 3], DeleteNthNodeFromEnd.remove_nth_from_end(head, 4).to_list())
        """
                middle
        """
        head = ListNode.nodes([0, 1, 2, 3])
        self.assertEqual([0, 1, 3], DeleteNthNodeFromEnd.remove_nth_from_end(head, 2).to_list())
        """
                end
        """
        head = ListNode.nodes([0, 1, 2, 3])
        self.assertEqual([0, 1, 2], DeleteNthNodeFromEnd.remove_nth_from_end(head, 1).to_list())
