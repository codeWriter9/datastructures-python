class DeleteNode:

    def __init__(self):
        pass

    @staticmethod
    def delete_node(node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        save = None
        while node and node.next:
            node.x = node.next.x
            save = node
            node = node.next
        save.next = None

    def __repr__(self):
        """Overrides the default implementation"""
        return 'DeleteNode'
