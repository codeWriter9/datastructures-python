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


    def test_delete(self):
        sample_list = LinkedList()
        sample_list.insert_at_tail(1).insert_at_tail(2).insert_at_tail(3).insert_at_tail(4)
        sample_list.delete(1)
        self.assertEqual(sample_list.get_head(), Node(2))


    def test_length(self):
        sample_list = LinkedList()
        sample_list.insert_at_tail(1).insert_at_tail(2).insert_at_tail(3).insert_at_tail(4)
        self.assertEqual(sample_list.length(), 4)
        sample_list.delete(1)
        self.assertEqual(sample_list.length(), 3)


    def test_reverse(self):
        sample_list = LinkedList()
        sample_list.insert_at_tail(1).insert_at_tail(2).insert_at_tail(3).insert_at_tail(4)
        self.assertEqual(sample_list.get_head(), Node(1))
        sample_list.reverse()
        self.assertEqual(sample_list.get_head(), Node(4))


    def test_detect_loop(self):
        sample_list = LinkedList()
        sample_list.insert_at_tail(1).insert_at_tail(2).insert_at_tail(3).insert_at_tail(4)
        self.assertFalse(sample_list.detect_loop())
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n1.next_element = n2
        n2.next_element = n3
        n3.next_element = n1
        sample_list.head_node = n1
        self.assertTrue(sample_list.detect_loop())


    def test_mid_point(self):
        sample_list = LinkedList()
        self.assertEqual(sample_list.find_mid(), None)
        sample_list.insert_at_tail(1).insert_at_tail(2).insert_at_tail(3).insert_at_tail(4)
        self.assertEqual(sample_list.find_mid(), Node(2))
        sample_list.insert_at_tail(5)
        self.assertEqual(sample_list.find_mid(), Node(3))


    def test_mid_point2(self):
        sample_list = LinkedList()
        sample_list.insert_at_tail(1)
        self.assertEqual(sample_list.find_mid(), Node(1))
        sample_list.insert_at_tail(2)
        self.assertEqual(sample_list.find_mid(), Node(1))
        sample_list.insert_at_tail(3)
        self.assertEqual(sample_list.find_mid(), Node(2))


if __name__ == '__main__':
    unittest.main()
