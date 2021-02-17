# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        
        
        def check_symmetry(left_root, right_root):
            if left_root == None and right_root == None:
                return True
            if not left_root == None and not right_root == None and left_root.val == right_root.val:
                # if left_root.left.val == right_root.right.val and left_root.right.val == right_root.left.val:
                return check_symmetry(left_root.left, right_root.right) and check_symmetry(left_root.right, right_root.left)
            return False
        
        if root == None: return True
        
        return check_symmetry(root.left, root.right)
        
        
        
#         queue = collections.deque([root])
        
#         while queue:
#             level = []
#             level_length = len(queue)
#             for i in range(level_length):
#                 current = queue.popleft()
#                 level.append(current.val if current.val else 0)
#                 if current.left or current.right: 
#                     queue.append((current.left if current.left else 0)
#                     queue.append(current.right if current.right else 0)
            
#             i=0
#             j= level_length-1
#             while i<int(level_length/2):
#                 if not level[i] == level[j]:
#                     return False
                
#                 i+=1
#                 j-=1
                
#         return True