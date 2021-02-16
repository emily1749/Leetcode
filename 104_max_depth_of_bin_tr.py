# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        
        queue, count = collections.deque([root]), 0
        
        while queue:
            lvl_length = len(queue)
            
            for i in range(lvl_length):
                current = queue.popleft()
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
            
            count += 1
        
        return count