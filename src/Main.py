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

if __name__ == '__main__':
    lst = LinkedList()
    lst.insert_at_tail(1).insert_at_tail(2).insert_at_tail(3).insert_at_tail(4)
    lst.print_list()
    print(length(lst))
    lst.delete(2)
    lst.print_list()
    print(length(lst))
