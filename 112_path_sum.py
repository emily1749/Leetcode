# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs(node, running_sum, target_sum):
            running_sum += node.val

            if not node.left and not node.right:
                if running_sum == target_sum: return True
                return False

            if node.left:
                if dfs(node.left, running_sum, target_sum):
                    return True
                
            if node.right:
                if dfs(node.right, running_sum, target_sum):
                    return True
            
        if root == None: return root
            
        if dfs(root, 0, targetSum):
            return True
        return False