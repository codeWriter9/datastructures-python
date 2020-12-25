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

if __name__ == '__main__':
    lst = LinkedList()
    lst.insert_at_tail(1).insert_at_tail(2).insert_at_tail(3).insert_at_tail(4)
    lst.print_list()
    print(search(lst, 1))
    print(search(lst, 2))
    print(search(lst, 3))
    print(search(lst, 4))
    print(search(lst, 0))
    print(search(lst, 5))
