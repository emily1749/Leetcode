
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None: return root
        
        queue = collections.deque([root])
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                current = queue.popleft()
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
                if current.left or current.right:
                    current.left, current.right = current.right, current.left
                
        return root