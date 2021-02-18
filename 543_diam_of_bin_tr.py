# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def calc_height(node):
            if node == None:
                return 0
            left = calc_height(node.left)
            right = calc_height(node.right)
            curr_nodes = left+right+1
            self.max_depth = max(self.max_depth, curr_nodes)
            return max(left, right) + 1
        self.max_depth = 0

        if root == None: return 0
        
        calc_height(root)
        return self.max_depth - 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         self.best = 1
#         def depth(root):
#             if not root: return 0
#             ansL = depth(root.left)
#             ansR = depth(root.right)
#             self.best = max(self.best, ansL + ansR + 1)
#             return 1 + max(ansL, ansR)

#         depth(root)
#         return self.best - 1
        
#         stack = []
#         # max_left = 0
#         # max_right = 0
        
#         current = root
#         # stack.append(current)
#         # max_left = 1

#         while True
#             if current is not None:
#                 stack.append(current)
#                 current = current.left
                
#             elif stack:
#                 max_
#                 current = stack.pop()
#                 current = current.right
            
#             else:
#                 break