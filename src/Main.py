from datastructures.linkedlist.LinkedList import LinkedList
from datastructures.linkedlist.Node       import Node
from datastructures.stack.Stack           import Stack
from datastructures.queue.Queue           import Queue

from datastructures.tree.binaryTree.AVLTree             import AVLTree
from datastructures.tree.binaryTree.BinarySearchTree    import BinarySearchTree
from datastructures.tree.binaryTree.BinaryTreeNode      import BinaryTreeNode
from datastructures.tree.binaryTree.BinaryTree          import BinaryTree
from datastructures.tree.binaryTree.BSTInorderIterator  import InorderIterator


class Main:

    def __init__(self):
        pass

    def run():
        pass

    def inorder_using_iterator(self, root):
        iter = InorderIterator(root)
        result = ""
        while iter.hasNext():
            ptr = iter.getNext()
            print(ptr)
            result += str(ptr.data) + " "
        return result

    def rotate_right(self, root):
        pivot = root.left
        root.left = pivot.right
        pivot.right = root
        return pivot

    def rotate_left(self, root):
        pivot = root.right
        root.right = pivot.left
        pivot.left = root
        return pivot


if __name__ == '__main__':
    main = Main()
    avl = AVLTree(BinaryTreeNode(1))
    for node in range(2, 11, 1):
        avl.insert(avl.bst_root(), BinaryTreeNode(node))
    print(avl.in_order())
