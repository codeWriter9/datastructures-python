from datastructures.tree.binaryTree.BinaryTreeNode import BinaryTreeNode
from datastructures.tree.binaryTree.BinaryTree     import BinaryTree

class BinarySearchTree(BinaryTree):

    def __init__(self, root:BinaryTreeNode):
         super().__init__(root)

    @classmethod
    def from_list(cls, lst) -> 'BinarySearchTree':
        if lst and len(lst) > 0:
            bst = cls(BinaryTreeNode.with_data(lst[0]))
            for data in lst[1:]:
                bst.insert(bst.root, BinaryTreeNode.with_data(data))
            return bst
        else :
            return cls(None)

    def insert(self, current, node):
        if current:
            if  node.data > current.data and current.right is None:
                current.right = node
            elif  node.data <= current.data and current.left is None:
                current.left = node
            elif node.data > current.data:
                self.insert(current.right, node)
            else :
                self.insert(current.left, node)
        else :
            pass

    def in_order(self):
        return super()._in_order(super()._root())