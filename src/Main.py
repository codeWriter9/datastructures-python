from datastructures.linkedlist.LinkedList import LinkedList
from datastructures.linkedlist.Node import Node

class Main:
    def __init__(self):
        pass


    def run():
        pass


def remove_duplicates(lst):
    visited = []
    if lst and lst.get_head():
        current = lst.get_head()
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
                lst.head_node = current.next_element
    return lst

if __name__ == '__main__':
    main = Main()
    sample_list = LinkedList()
    remove_duplicates(sample_list).print_list()
    sample_list.insert_at_tail(1).insert_at_tail(2).insert_at_tail(3).insert_at_tail(4)
    remove_duplicates(sample_list).print_list()
    sample_list.insert_at_tail(1).insert_at_tail(2).insert_at_tail(3).insert_at_tail(4)
    sample_list.print_list()
    remove_duplicates(sample_list).print_list()
