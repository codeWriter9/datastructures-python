from datastructures.linkedlist.LinkedList import LinkedList
from datastructures.linkedlist.Node import Node
from datastructures.stack.Stack import Stack
from datastructures.queue.Queue import Queue


class Main:
    def __init__(self):
        pass


    def run():
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


if __name__ == '__main__':
    main = Main()
    queue = Queue()
    for counter in range(1, 11):
        queue.enqueue(counter)
    anotherQueue = main.reverseK(queue, 5)
    print([x for x in anotherQueue.queue_list ])
    queue = Queue()
    anotherQueue = main.reverseK(queue, 5)
    print(anotherQueue)
    for counter in range(1, 11):
        queue.enqueue(counter)
    anotherQueue = main.reverseK(queue, 22)
    print(anotherQueue)
    queue = Queue()
    for counter in range(1, 11):
        queue.enqueue(counter)
    anotherQueue = main.reverseK(queue, -4)
    print(anotherQueue)

