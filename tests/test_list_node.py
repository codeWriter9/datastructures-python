# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from algorithms.linkedlist.ListNode import ListNode


class TestStack(unittest.TestCase):

    def test_list_node_not_null(self):
        self.assertIsNotNone(ListNode(0))

    def test_list_node(self):
        head = ListNode.nodes([0, 1, 2, 3])
        self.assertIsNotNone(head)
        self.assertEqual([0, 1, 2, 3], head.to_list())

