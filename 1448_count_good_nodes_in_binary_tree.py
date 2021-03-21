# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_stack = []
        result = []
        def dfs(node):
            if len(max_stack) == 0 or max_stack[-1]<= node.val:
                max_stack.append(node.val)
                result.append(node.val)
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
            if max_stack[-1] == node.val:
                max_stack.pop()
        dfs(root)
        return len(result)
    # time: O(N) go throuhg every node
    # space: O(N) for the max_stack and the height of recursion stack
        