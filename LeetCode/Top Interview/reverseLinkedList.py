# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            # Create a pointer to the next node
            nxt = head.next
            # Set the new nodes next to previous
            head.next = prev
            # Set previous node to head
            prev = head
            # Move to next node
            head = nxt
        return prev