# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from datastructures.tree.binaryTree.AVLTree          import AVLTree
from datastructures.tree.binaryTree.BinarySearchTree import BinarySearchTree
from datastructures.tree.binaryTree.BinaryTreeNode   import BinaryTreeNode
from datastructures.tree.binaryTree.BinaryTree       import BinaryTree


class TestAVLTree(unittest.TestCase):

    def test_avl_tree(self):
        self.assertIsNotNone(AVLTree(BinaryTreeNode.with_data_and_children(1, None, None)))

    def test_avl_tree_height(self):
        self.assertEqual(AVLTree(None).height(), 0)
        avl_tree = AVLTree(BinaryTreeNode.with_data_and_children(1, None, None))
        self.assertIsNotNone(avl_tree)
        self.assertEqual(avl_tree.height(), 1)
        avl_tree = AVLTree(BinaryTreeNode.with_data_and_children(2, BinaryTreeNode(1), BinaryTreeNode(3)))
        self.assertIsNotNone(avl_tree)
        self.assertEqual(avl_tree.height(), 2)

    def test_avl_tree_balance_factor(self):
        self.assertEqual(AVLTree(None).balance_factor(), 0)
        avl_tree = AVLTree(BinaryTreeNode.with_data_and_children(1, None, None))
        self.assertIsNotNone(avl_tree)
        self.assertEqual(avl_tree.balance_factor(), 0)
        avl_tree = AVLTree(BinaryTreeNode.with_data_and_children(2, BinaryTreeNode(1), BinaryTreeNode(3)))
        self.assertIsNotNone(avl_tree)
        self.assertEqual(avl_tree.balance_factor(), 0)
        avl_tree = AVLTree(BinaryTreeNode.with_data_and_children(2, BinaryTreeNode(1), None))
        self.assertIsNotNone(avl_tree)
        self.assertEqual(avl_tree.balance_factor(), 1)
        avl_tree = AVLTree(BinaryTreeNode.with_data_and_children(2, None, BinaryTreeNode(3)))
        self.assertIsNotNone(avl_tree)
        self.assertEqual(avl_tree.balance_factor(), -1)
