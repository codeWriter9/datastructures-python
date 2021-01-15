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


if __name__ == '__main__':
    main = Main()
    bt = BinarySearchTree.from_list([100,50,200,25,125,350])
    print(main.inorder_using_iterator(bt.bst_root()))
    #print(main.inorder_using_iterator(bt2.bst_root()))

