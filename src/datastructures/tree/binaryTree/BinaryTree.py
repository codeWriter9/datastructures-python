from datastructures.tree.binaryTree.BinaryTreeNode import BinaryTreeNode

class BinaryTree:

    def __init__(self, root:BinaryTreeNode):
        self.root = root

    def __repr__(self): 
        if self.root:
            return 'Node: {}'.format(self.data.string)
        else :
            return 'None'

    def max_depth(self, current):
        if current.left is None and current.right is None:
            return 1
        else :
            return 1 + max(self.max_depth(current.left), self.max_depth(current.right))

    def height(self):
        if self.root:
            if self.root.left is None and self.root.right is None:
                return 1
            else :
                return 1 + max(self.max_depth(self.root.left), self.max_depth(self.root.right))
        else :
            return 0

    def in_order(self, current):
        if current:
            if current.left:
                self.in_order(current.left)
            print(current)
            if current.right:
                self.in_order(current.right)