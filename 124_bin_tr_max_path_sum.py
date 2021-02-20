# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth_max = float('-inf')

        def find_max(node):
            # global depth_max
            if node == None:
                return 0
            left_max = max(find_max(node.left), 0)
            right_max = max(find_max(node.right), 0)
            height_max = max(left_max+node.val, right_max+node.val)
            self.depth_max = max(self.depth_max, right_max + left_max + node.val)
            return height_max
        

        find_max(root)
        return self.depth_max
        
          