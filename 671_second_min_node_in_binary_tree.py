# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        first_min = root.val
        second_min = float("inf")
        queue = collections.deque([root])
        while len(queue)>0:
            current = queue.popleft()
            if current.val != first_min:
                second_min = min(second_min, current.val)
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)
        if second_min == float("inf"): return -1
        return second_min