# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Precondition: node is not the tail of the LinkedList
        # Take next nodes value
        node.val = node.next.val
        # Skip over next node
        node.next = node.next.next