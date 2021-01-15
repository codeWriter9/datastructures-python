from datastructures.stack.Stack           import Stack


class InorderIterator:
    def __init__(self, root):
        self.stck = Stack()
        self.populate_stack(root)

# hasNext returns False if there are no more elements in stack to be popped
    def hasNext(self):
        if self.stck and not self.stck.is_empty() :
            return True
        else :
            return False

# getNext returns null if there are no more elements in tree
    def getNext(self):
        if self.stck:
            r_val = self.stck.pop()
            if r_val:
                temp = r_val.right;
                self.populate_stack(temp)
                return r_val
        return None

    def populate_stack(self, root):
        if root:
            while root:
                self.stck.push(root)
                root = root.left
