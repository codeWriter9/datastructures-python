from typing import Optional

from algorithms.linkedlist.ListNode import ListNode


class ReverseNode:

    def __init__(self):
        pass

    @staticmethod
    def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        save = None
        while current:
            prev = save
            save = current
            current = current.next
            save.next = prev
        return save

    @staticmethod
    def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        reversed_list = ReverseNode.reverse_list_recursive(head.next)
        head.next.next = head  # Tricky part --- Point the rest of list back to head
        head.next = None
        return reversed_list

    def __repr__(self):
        """Overrides the default implementation"""
        return 'ReverseNode'
