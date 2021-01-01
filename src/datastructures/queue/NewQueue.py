from datastructures.queue.Queue import Queue
from datastructures.queue.QueueUtil import QueueUtil
from datastructures.stack.Stack import Stack
# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.get_top()  //Returns top element
# Helper Functions => stack.is_empty() & stack.isFull() //returns boolean


class NewQueue:
    def __init__(self):
        self.main_stack = Stack()
        self.temp_stack = Stack()

        # Inserts Element in the Queue
    def enqueue(self, value):
        if self.main_stack.top() is None:
            self.main_stack.push(value)
        else :
            while self.main_stack.top() is not None:
                self.temp_stack.push(self.main_stack.pop())
            self.main_stack.push(value)
            while self.temp_stack.top() is not None:
                self.main_stack.push(self.temp_stack.pop())


        # Removes Element From Queue
    def dequeue(self):
        if self.main_stack.top() is None:
            return None
        elif self.main_stack.top() >= 1:
            return self.main_stack.pop()
