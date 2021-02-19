# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def check_balance(node):
            if node == None: 
                return -1, True
            left_height, balance = check_balance(node.left)   
            if balance == False:
                return 0, False
            right_height, balance = check_balance(node.right)
            if balance == False:
                return 0, False
            height = max(left_height, right_height)+1
            if abs(right_height-left_height)<2:
                balance = True
            else:
                balance = False
            return height, balance
            
        
        
        return check_balance(root)[1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def check_balance(node):
#             if node == None:
#                 return -1, True
#             left, is_balanced = check_balance(node.left)
#             if not is_balanced: return 0, False
#             right, is_balanced = check_balance(node.right)
#             if not is_balanced: return 0, False
            
#             print(left)
#             print(right)
#             height = 1+max(left, right)
#             if abs(left-right)<2: chk_balanced = True
#             return height, chk_balanced
            
        
#         if root == None: return True
        
#         return check_balance(root)[1]