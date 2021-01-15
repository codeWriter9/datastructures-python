# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from datastructures.tree.binaryTree.BinaryTreeNode import BinaryTreeNode




class TestBinaryTreeNode(unittest.TestCase):


    def test_binary_tree_node_single(self):
        self.assertIsNotNone(BinaryTreeNode(1))
        self.assertIsNotNone(BinaryTreeNode.with_data(1))
        self.assertIsNotNone(BinaryTreeNode.with_data_and_children(1, None, None))

    def test_binary_tree_node(self):
        self.assertIsNotNone(BinaryTreeNode(1))
        self.assertIsNotNone(BinaryTreeNode.with_data(1))
        self.assertIsNotNone(BinaryTreeNode.with_data_and_children(2, BinaryTreeNode(1), BinaryTreeNode(3)))

    def test_binary_tree_node_equality(self):
        self.assertEqual(BinaryTreeNode(1), BinaryTreeNode(1))
        self.assertEqual(BinaryTreeNode(1), BinaryTreeNode.with_data_and_children(1, None, None))

    def test_binary_tree_node_inequality(self):
        self.assertNotEqual(BinaryTreeNode(1), BinaryTreeNode(2))
        self.assertNotEqual(BinaryTreeNode(1), BinaryTreeNode.with_data_and_children(2, None, None))
