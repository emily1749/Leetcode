# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return None
        
        result, queue = [], collections.deque()
        queue.append(root)
        while queue:
            queue_length = len(queue)
            level = []
            for i in range(queue_length):
                current = queue.popleft()
                level.append(current.val)
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
            result.append(level)
            
        return result[::-1]