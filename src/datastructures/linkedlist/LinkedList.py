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
