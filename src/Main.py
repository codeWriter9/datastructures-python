from datastructures.linkedlist.LinkedList import LinkedList
from datastructures.linkedlist.Node import Node

class Main:
    def __init__(self):
        pass


    def run():
        pass

def insert_at_tail(lst, value):
    head = lst.get_head()
    if lst.is_empty():
        lst.head_node = Node(value)
    else:
        node = Node(value)
        current = lst.head_node
        while current.next_element is not None:
            current = current.next_element
        current.next_element = node
    return


def search(lst, value):
    if not lst.is_empty():
        current = lst.get_head()
        while current is not None:
            if current.data == value:
                return True
            else:
                current = current.next_element
    return False


def delete(lst, value):
    if not lst.is_empty():
        current = lst.get_head()
        previous = None
        while current is not None:
            if current.data == value:
                if previous is None:
                    lst.head_node = current.next_element
                else :
                    previous.next_element = current.next_element
                return True
            else:
                previous = current
                current = current.next_element
    return False

def length(lst):
    if not lst.is_empty():
        len = 0
        current = lst.get_head()
        while current is not None:
            current = current.next_element
            len = len + 1
        return len
    else :
        return 0


def reverse(lst):
    if lst:
        head = lst.get_head()
        current = head
        previous = None
        next = None
        while current:
            next = current.next_element # save the remainder
            current.next_element = previous  # save the previous as the next node
            previous = current # current is the new previous
            current = next # ready pointer to next
            lst.head_node = previous
    return lst


def detect_loop(lst):
    if lst:
        slow = lst.get_head()
        fast = None if lst.get_head() == None else lst.get_head().next_element
        while slow and fast:
            if slow.data == fast.data:
                return True
            else:
                slow = slow.next_element
                fast = None if fast.next_element == None else fast.next_element.next_element
    return False


if __name__ == '__main__':
    lst = LinkedList()
    lst.insert_at_tail(1).insert_at_tail(2).insert_at_tail(3).insert_at_tail(4)
    print(detect_loop(lst))
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.next_element = n2
    n2.next_element = n3
    n3.next_element = n1
    lst.head_node = n1
    print(detect_loop(lst))
