# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        
        count, queue = 1, collections.deque()
        queue.append(root)
        while queue:
            length = len(queue)
            for i in range(length):
                current = queue.popleft()
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
                if not current.right and not current.left: return count
            
            count += 1
            
        return count