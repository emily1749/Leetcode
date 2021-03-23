# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        def preorder(node, curr_combo):
            if node.val != None: curr_combo.append(str(node.val))
            if node.left: preorder(node.left, curr_combo)
            if node.right: preorder(node.right, curr_combo)
            if node.left == None and node.right == None:
                result.append(int("".join(curr_combo)))
            curr_combo.pop()
        
        preorder(root, [])
        print(result)
        ans = 0
        for numb in result:
            ans += numb
        return ans