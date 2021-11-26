from typing import Optional

from algorithms.linkedlist.ListNode import ListNode


class Palindrome:

    def __init__(self):
        pass

    @staticmethod
    def is_palindrome(head: Optional[ListNode]) -> bool:
        current, _arr_ = head, []
        while current:
            _arr_.append(current.x)
            current = current.next
        current = Palindrome.reverse(head)
        index = 0
        while current:
            if current.x != _arr_[index]:
                print("current.x=" + str(current.x) + "|_arr_[index]=" + str(_arr_[index]) + "|index=" + str(index))
                return False
            index = index + 1
            current = current.next
        return True

    @staticmethod
    def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        reversed_list = Palindrome.reverse(head.next)
        head.next.next = head  # Tricky part --- Point the rest of list back to head
        head.next = None
        return reversed_list

    def __repr__(self):
        """Overrides the default implementation"""
        return 'Palindrome'
