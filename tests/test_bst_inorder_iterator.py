# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from datastructures.tree.binaryTree.BinaryTreeNode      import BinaryTreeNode
from datastructures.tree.binaryTree.BinarySearchTree    import BinarySearchTree
from datastructures.tree.binaryTree.BSTInorderIterator  import InorderIterator



class TestInorderIterator(unittest.TestCase):


    def test_binary_tree_node_empty(self):
        self.assertIsNotNone(InorderIterator(None))

    def test_inorder_using_iterator(self):
        bst = BinarySearchTree.from_list([100,50,200,25,125,350])
        iter = InorderIterator(bst.bst_root())
        result = ""
        while iter.hasNext():
            ptr = iter.getNext()
            print(ptr)
            result += str(ptr.data) + " "
        self.assertEqual(result, "25 50 100 125 200 350 ")