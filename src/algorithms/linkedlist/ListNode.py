from typing import List


class ListNode:

    def __init__(self, x):
        self.x = x
        self.next = None

    def print_node(self):
        print(self.x)
        if self.next:
            self.next.print_node()

    @classmethod
    def node(cls, x: int):
        return cls(x)

    @classmethod
    def nodes(cls, arr: List):
        head = cls(arr[0])
        prev = head
        for index in range(1, len(arr)):
            current = cls(arr[index])
            prev.next = current
            prev = current
        return head

    def to_list(self, _list_: [] or None = None) -> []:
        if not _list_:
            _list_ = []
        _list_.append(self.x)
        if self.next:
            return self.next.to_list(_list_)
        else:
            return _list_

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, ListNode):
            return self.x == other.x
        return False

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(self.x)

    def __repr__(self):
        """Overrides the default implementation"""
        return str(self.x)
