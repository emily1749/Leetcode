# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None: return 0
        previous = {0: 1}
        self.count = 0
        def preorder(node, current_sum):
            current_sum+=node.val
            if current_sum - sum in previous:
                self.count += previous[current_sum-sum]
            previous[current_sum] = previous.get(current_sum, 0) + 1
            if node.left: preorder(node.left, current_sum)
            if node.right: preorder(node.right, current_sum)
            previous[current_sum] -= 1
        preorder(root, 0)
        return self.count