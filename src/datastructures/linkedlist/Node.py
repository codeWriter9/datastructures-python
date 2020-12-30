


class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Node):
            return self.data == other.data
        return False


    def __hash__(self):
        """Overrides the default implementation"""
        return hash(self.data)