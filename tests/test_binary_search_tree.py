# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from datastructures.tree.binaryTree.BinarySearchTree    import BinarySearchTree
from datastructures.tree.binaryTree.BSTInorderIterator  import InorderIterator
from datastructures.tree.binaryTree.BinaryTreeNode      import BinaryTreeNode
from datastructures.tree.binaryTree.BinaryTree          import BinaryTree


class TestBinarySearchTree(unittest.TestCase):

    def test_binary_tree(self):
        self.assertIsNotNone(BinarySearchTree(BinaryTreeNode.with_data_and_children(1, None, None)))

    def test_binary_tree_height(self):
        self.assertEqual(BinarySearchTree(None).height(), 0)
        bst = BinarySearchTree(BinaryTreeNode.with_data_and_children(1, None, None))
        self.assertIsNotNone(bst)
        self.assertEqual(bst.height(), 1)
        bst = BinarySearchTree(BinaryTreeNode.with_data_and_children(2, BinaryTreeNode(1), BinaryTreeNode(3)))
        self.assertIsNotNone(bst)
        self.assertEqual(bst.height(), 2)

    def test_inorder_using_iterator(self):
        bst = BinarySearchTree.from_list([100,50,200,25,125,350])
        iter = InorderIterator(bst.bst_root())
        result = ""
        while iter.hasNext():
            ptr = iter.getNext()
            print(ptr)
            result += str(ptr.data) + " "
        self.assertEqual(result, "25 50 100 125 200 350 ")

    def test_inorder_succesor(self):
        bst = BinarySearchTree.from_list([100,50,200,25,125,350,75])
        self.assertEqual(bst.inorder_successor(75).data, 100)

    def test_inorder_succesor_tree_null(self):
        bst = BinarySearchTree(None)
        self.assertEqual(bst.inorder_successor(75), None)
