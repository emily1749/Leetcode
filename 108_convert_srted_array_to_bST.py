# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        # root.val = nums[middle]

        # while left<=right:
        def build_tree(left, right):
            if left>right: return None
            middle = left + int((right-left)/2)
            root = TreeNode(nums[middle])
            root.left = build_tree(left, middle-1)
            root.right = build_tree(middle+1, right)
            return root
        
        left = 0
        right = len(nums)-1
      
        return build_tree(left, right)