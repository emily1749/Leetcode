# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        self.summation = 0
        def sum_left(node):
            if node.left and not node.left.left and not node.left.right:
                self.summation += node.left.val
            if node.left: sum_left(node.left)
            if node.right: sum_left(node.right)
        sum_left(root)
        return self.summation