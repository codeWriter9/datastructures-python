# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from datastructures.linkedlist.LinkedList import LinkedList
from datastructures.linkedlist.Node import Node


class TestlinkList(unittest.TestCase):

    def test_link_list(self):
        self.assertIsNotNone(LinkedList())


    def test_linklist_head_none(self):
        sample_list = LinkedList()
        self.assertIsNone(sample_list.get_head())


    def test_is_empty(self):
        sample_list = LinkedList()
        self.assertTrue(sample_list.is_empty())


    def test_insert_at_tail(self):
        sample_list = LinkedList()
        sample_list.insert_at_tail(1).insert_at_tail(2).insert_at_tail(3).insert_at_tail(4)
        self.assertEqual(sample_list.get_head(), Node(1))


    def test_search(self):
        sample_list = LinkedList()
        sample_list.insert_at_tail(1).insert_at_tail(2).insert_at_tail(3).insert_at_tail(4)
        self.assertFalse(sample_list.search(0))
        self.assertTrue(sample_list.search(1))
        self.assertTrue(sample_list.search(2))
        self.assertTrue(sample_list.search(3))
        self.assertTrue(sample_list.search(4))
        self.assertFalse(sample_list.search(5))
        self.assertFalse(sample_list.search(6))


if __name__ == '__main__':
    unittest.main()