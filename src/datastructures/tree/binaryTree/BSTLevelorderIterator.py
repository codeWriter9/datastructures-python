from datastructures.queue.Queue           import Queue


class LevelOrderIterator:
    def __init__(self, root):
        self.queue = Queue()
        self.populate_queue(root)

# hasNext returns False if there are no more elements in queue to be popped
    def hasNext(self):
        if self.queue and not self.queue.is_empty() :
            return True
        else :
            return False

# getNext returns null if there are no more elements in tree
    def getNext(self):
        if self.queue:
            current = self.queue.dequeue()
            if current:
                left = current.left;
                right = current.right;
                self.populate_queue(left)
                self.populate_queue(right)
                return current
        return None

    def populate_queue(self, current):
        if current:
            self.queue.enqueue(current)
