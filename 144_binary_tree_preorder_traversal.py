# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None: return None
        
        stack = []
        res = []
        cur = root
        while not cur == None:
            res.append(cur.val)
            while cur.left:
                stack.append(cur)
                cur = cur.left
                res.append(cur.val)
            
            while cur.right == None and len(stack)>0:
                cur = stack.pop()
            cur = cur.right
        
        return res