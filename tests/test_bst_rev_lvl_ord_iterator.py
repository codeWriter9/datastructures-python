# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from datastructures.tree.binaryTree.BinaryTreeNode            import BinaryTreeNode
from datastructures.tree.binaryTree.BinarySearchTree          import BinarySearchTree
from datastructures.tree.binaryTree.BSTReverseLvlOrdIterator  import ReverseLvlOrdIterator



class TestReverseLevelOrderIterator(unittest.TestCase):


    def test_binary_tree_node_empty(self):
        self.assertIsNotNone(ReverseLvlOrdIterator(None))

    def test_reverse_level_order_using_iterator(self):
        pass
        '''
        bst = BinarySearchTree.from_list([100,50,200,25,75,350])
        iter = ReverseLvlOrdIterator(bst.bst_root())
        result = ""
        while iter.hasNext():
            ptr = iter.getNext()
            print(ptr)
            result += str(ptr.data) + " "
        self.assertEqual(result, "25 75 350 50 200 100")
        '''