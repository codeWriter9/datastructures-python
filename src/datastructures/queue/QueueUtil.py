from datastructures.queue.Queue import Queue
from datastructures.stack.Stack import Stack


class QueueUtil:

    def __init__(self):
        pass

    def reverseK(self, queue, k):
        stack = Stack()
        anotherQueue = Queue()
        if queue and not queue.is_empty():
            if k < queue.size() and k > 0:
                for counter in range(1, k + 1):
                    stack.push(queue.dequeue())
                while stack.top():
                    anotherQueue.enqueue(stack.pop())
                while queue.front():
                    anotherQueue.enqueue(queue.dequeue())
                return anotherQueue
        return None
