from datastructures.linkedlist.Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node is None):  # Check whether the head is None
            return True
        else:
            return False

    # Supplementary print function
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    def insert_at_tail(self, value):
        head = self.get_head()
        if self.is_empty():
            self.head_node = Node(value)
        else:
            node = Node(value)
            current = self.head_node
            while current.next_element is not None:
                current = current.next_element
            current.next_element = node
        return self

    def search(self, value):
        if not self.is_empty():
            current = self.get_head()
            while current is not None:
                if current.data == value:
                    return True
                else:
                    current = current.next_element
        return False

    def delete(self, value):
        if not self.is_empty():
            current = self.get_head()
            previous = None
            while current is not None:
                if current.data == value:
                    if previous is None:
                        self.head_node = current.next_element
                    else :
                        previous.next_element = current.next_element
                    return True
                else:
                    previous = current
                    current = current.next_element
        return False

    def length(self):
        if not self.is_empty():
            len = 0
            current = self.get_head()
            while current is not None:
                current = current.next_element
                len = len + 1
            return len
        else :
            return 0

    def reverse(self):
        if self.get_head():
            head = self.get_head()
            current = head
            previous = None
            next = None
            while current:
                next = current.next_element # save the remainder
                current.next_element = previous  # save the previous as the next node
                previous = current # current is the new previous
                current = next # ready pointer to next
                self.head_node = previous
        return self

    def detect_loop(self):
        if self.get_head():
            slow = self.get_head()
            fast = None if self.get_head() == None else self.get_head().next_element
            while slow and fast:
                if slow.data == fast.data:
                    return True
                else:
                    slow = slow.next_element
                    fast = None if fast.next_element == None else fast.next_element.next_element
        return False