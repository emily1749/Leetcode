# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def insert(node, value):
            if node == None:
                return TreeNode(value)
            if node.val<value:
                node.right = insert(node.right, value)
            else:
                node.left = insert(node.left, value)
            
            return node
        
        return insert(root, val)