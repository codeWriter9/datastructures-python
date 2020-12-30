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

    def find_mid(self):
        if self.get_head():
            count = 0
            stop = 0
            current = self.get_head()
            if self.length() % 2 == 0:
                stop = self.length() / 2 - 1
            else :
                stop = int(self.length() / 2)
            while count != stop:
                count = count + 1
                current = current.next_element
            return current
        return None

    def remove_duplicates(self):
        visited = []
        if self.get_head():
            current = self.get_head()
            previous = None
            while current:
                if current.data not in visited:
                    visited.append(current.data)
                    previous = current
                    current = current.next_element
                elif previous: # previous is not None
                    previous.next_element = current.next_element
                    current = current.next_element
                else:
                    self.head_node = current.next_element
        return self

    def union(self, list2):
        if self and self.get_head():
            if list2 and list2.get_head():
                current = self.get_head()
                previous = current
                while current:
                    previous = current
                    current = current.next_element
                previous.next_element = list2.get_head()
                self.remove_duplicates()
                return self
            else :
                return self
            return self
        elif list2 and list2.get_head():
            return list2
        return LinkedList()

    def intersection(self, list2):
        length1 = 0
        length2 = 0
        if self and self.get_head():
            length1 = self.length()
        if list2 and list2.get_head():
            length2 = list2.length()
        if length1 == 0 or length2 == 0 :
            return LinkedList()
        intersection = LinkedList()
        current = self.get_head()
        while current:
            if list2.search(current.data):
                intersection.insert_at_tail(current.data)
            current = current.next_element
        return intersection

    def find_nth(self, n):
        if self.get_head():
            length = self.length()
            current = self.get_head()
            counter = 1
            while current and counter !=  (length - n + 1):
                counter = counter + 1
                current = current.next_element
            if not current:
                return -1
            return current.data
        return -1
