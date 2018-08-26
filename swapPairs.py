"""
Given 1->2->3->4, you should return the list as 2->1->4->3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # if size of list is 0 or 1
        if head == None or head.next == None:
            return head

        # does the swap
        new_node = head.next
        nxt = new_node.next

        new_node.next = head

        head.next = self.swapPairs(nxt)

        return new_node
