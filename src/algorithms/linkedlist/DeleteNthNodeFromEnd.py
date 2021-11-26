from algorithms.linkedlist.ListNode import ListNode
from typing import Optional


class DeleteNthNodeFromEnd:

    def __init__(self):
        pass

    @staticmethod
    def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current, length = head, 0
        while current:
            current = current.next
            length = length + 1
        actual = length - n + 1
        if actual == 1:
            return head.next
        current = head
        save = None
        while actual > 1:
            save = current
            current = current.next
            actual = actual - 1
        if current:
            save.next = current.next
        else:
            save.next = None
        return head

    def __repr__(self):
        """Overrides the default implementation"""
        return 'DeleteNthNodeFromEnd'