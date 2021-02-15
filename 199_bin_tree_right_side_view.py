# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root == None: return root
        
        queue = collections.deque()
        level = collections.deque()
        queue.append(root)
        result = []
        while queue:
            result.append(queue[len(queue)-1].val)
            level = queue
            level_length = len(level)
            queue = deque([])
            for i in range(level_length):
                current = level.popleft()
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
            
        return result