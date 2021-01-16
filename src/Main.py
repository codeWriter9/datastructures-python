from datastructures.linkedlist.LinkedList import LinkedList
from datastructures.linkedlist.Node       import Node
from datastructures.stack.Stack           import Stack
from datastructures.queue.Queue           import Queue

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
    two = BinaryTreeNode(2)
    four = BinaryTreeNode(4)
    seven = BinaryTreeNode(7)
    three = BinaryTreeNode.with_data_and_children(3, two, four)
    bt = BinarySearchTree(BinaryTreeNode.with_data_and_children(5, three, seven))
    print(main.inorder_using_iterator(bt.bst_root()))
    pivot = main.rotate_right(bt.bst_root())
    print(main.inorder_using_iterator(pivot))
    pivot = main.rotate_left(pivot)
    print(main.inorder_using_iterator(pivot))
