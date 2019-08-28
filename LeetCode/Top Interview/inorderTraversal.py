# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        curnode = root
        while True:
            if curnode:
                stack.append(curnode)
                curnode = curnode.left
            elif stack:
                curnode = stack.pop()
                res.append(curnode.val)
                curnode = curnode.right
            else:
                break
        return res