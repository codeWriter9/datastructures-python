from datastructures.tree.binaryTree.BinarySearchTree import BinarySearchTree
from datastructures.tree.binaryTree.BinaryTreeNode   import BinaryTreeNode
from datastructures.tree.binaryTree.BinaryTree       import BinaryTree

class AVLTree(BinarySearchTree):

    def __init__(self, root:BinaryTreeNode):
         super().__init__(root)

    def balance_factor(self, current=None):
        if self.root is None:
            return 0
        else :
            left_height = self._height(self.root.left)
            right_height = self._height(self.root.right)
            return left_height - right_height

    def rotate_right(self, current):
        if current and current.left:
            pivot = current.left
            current.left = pivot.right
            pivot.right = current
            return pivot
        else:
            return None

    def rotate_left(self, current):
        if current and current.right:
            pivot = current.right
            current.right = pivot.left
            pivot.left = current
            return pivot
        else:
            return None