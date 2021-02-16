
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue, result = collections.deque([root]), []
        while queue:
            level_length = len(queue)
            sum = 0
            for i in range(level_length):
                current = queue.popleft()
                sum+=current.val
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
            result.append(sum/float(level_length))
        
        return result