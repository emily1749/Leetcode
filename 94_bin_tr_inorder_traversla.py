# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        stack = []
        result = []
        current = root
        while not(current == None and len(stack)==0):
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.val)
            current = current.right
            
        return result
        
        
        
        
        
        
        
        
#         stack = []
#         result = []
#         stack.append(root)
#         current = root
#         # while len(stack)>0 and current != None:
#         while (len(stack) != 0 or current != None):
#             while current.left:
#                 current = current.left
#                 stack.append(current)
#             # if stack:
#             current = stack.pop()
#             result.append(current.val)
#             # if current.right:
#             current = current.right
#                 # stack.append(current)
        
#         return result
            
        
#         stack = []
#         current = root
#         stack.append(root)
#         result = []
#         while True:
#             if current.left:
#                 current = current.left
#                 stack.append(current)
#             elif stack:
#                 current = stack.pop()
#                 result.append(current.val)
#                 if current.right:
#                     current = current.right
#                     stack.append(current)
#             elif current.right:
#                 current = current.right
#                 stack.append(current)
#             else:
#                 break
        
#         return result