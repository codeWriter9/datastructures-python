


class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @classmethod
    def with_data(cls, data) -> 'BinaryTreeNode':
        return cls(data)

    @classmethod
    def with_data_and_children(cls, data, left, right) -> 'BinaryTreeNode':
        return cls(data, left, right)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, BinaryTreeNode):
            return self.data == other.data
        return False

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(self.data)

    def __repr__(self): 
        if self.data:
            return 'BinaryTreeNode: {}'.format(str(self.data))
        else :
            return 'BinaryTreeNode'