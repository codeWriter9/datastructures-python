# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from datastructures.linkedlist.Node import Node


class TestNode(unittest.TestCase):

    def test_node(self):
        self.assertIsNotNone(Node('data'))


    def test_node_next_element(self):
        n1 = Node('data')
        self.assertIsNone(n1.next_element)


    def test_node_next_element2(self):
        n1 = Node('data')
        n2 = Node('more_data')
        n1.next_element = n2
        self.assertIsNotNone(n1.next_element)


    def test_node_equality_string(self):
        self.assertEqual(Node('data'), Node('data'))


    def test_node_equality_integer(self):
        self.assertEqual(Node(1), Node(1))

if __name__ == '__main__':
    unittest.main()
