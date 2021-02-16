# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
       
        if root== None: return root
        
        result = []
        
        def traverse(node):
            if node.left: traverse(node.left)
            result.append(node.val)
            if node.right: traverse(node.right)
            
        traverse(root)
        
        for i in range(len(result)-1):
            if result[i]>=result[i+1]:
                return False
        return True