# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.linkedlist.DeleteNode import DeleteNode
from algorithms.linkedlist.ListNode import ListNode


class TestStack(unittest.TestCase):

    def test_delete_node_not_null(self):
        self.assertIsNotNone(ListNode(0))
        self.assertIsNotNone(DeleteNode())

    def test_delete_node(self):
        head = ListNode.nodes([0, 1, 2, 3])
        DeleteNode.delete_node(head.next.next)
        self.assertEqual([0, 1, 3], head.to_list())
        """
        head
        """
        head = ListNode.nodes([0, 1, 2, 3])
        DeleteNode.delete_node(head)
        self.assertEqual([1, 2, 3], head.to_list())

