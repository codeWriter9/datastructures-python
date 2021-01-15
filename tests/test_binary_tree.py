# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from datastructures.tree.binaryTree.BinarySearchTree import BinarySearchTree
from datastructures.tree.binaryTree.BinaryTreeNode   import BinaryTreeNode
from datastructures.tree.binaryTree.BinaryTree       import BinaryTree


class TestBinaryTree(unittest.TestCase):

    def test_binary_tree(self):
        self.assertIsNotNone(BinaryTree(BinaryTreeNode.with_data_and_children(1, None, None)))

    def test_binary_tree_height(self):
        self.assertEqual(BinaryTree(None).height(), 0)
        bt = BinaryTree(BinaryTreeNode.with_data_and_children(1, None, None))
        self.assertIsNotNone(bt)
        self.assertEqual(bt.height(), 1)
        bt = BinaryTree(BinaryTreeNode.with_data_and_children(2, BinaryTreeNode(1), BinaryTreeNode(3)))
        self.assertIsNotNone(bt)
        self.assertEqual(bt.height(), 2)

    def test_binary_search_tree(self):
        self.assertIsNotNone(BinarySearchTree(BinaryTreeNode.with_data_and_children(1, None, None)))
        self.assertIsNotNone(BinarySearchTree.from_list(None))

    def test_binary_search_tree_balanced(self):
        bt = BinarySearchTree(None)
        self.assertIsNotNone(bt)
        self.assertTrue(bt.is_balanced())
        bt = BinarySearchTree(BinaryTreeNode.with_data_and_children(1, None, None))
        self.assertIsNotNone(bt)
        self.assertTrue(bt.is_balanced())
        bt = BinarySearchTree(BinaryTreeNode.with_data_and_children(2, BinaryTreeNode(1), BinaryTreeNode(3)))
        self.assertIsNotNone(bt)
        self.assertTrue(bt.is_balanced())

    def test_binary_search_tree_unbalanced(self):
        bt = BinarySearchTree(BinaryTreeNode.with_data_and_children(3, BinaryTreeNode.with_data_and_children(2, BinaryTreeNode(1), BinaryTreeNode(0)), None))
        self.assertIsNotNone(bt)
        self.assertFalse(bt.is_balanced())