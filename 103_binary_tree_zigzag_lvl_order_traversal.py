# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        
        if root == None: return None
        result, temp, queue, flag = [], [], deque(), 1
        queue.append(root)
        
        while queue:
            # length = len(queue)
            for i in range(len(queue)):
                current = queue.popleft()
                temp.append(current.val)
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
            result.append(temp[::flag])
            temp = []
            flag*=-1
        return result
            
            
        
    
    
#         if root == None:
#             return None
        
#         idx = 0
#         queue = []
#         result = []
#         queue.append(root)
#         while len(queue)>0:
#             level_queue = queue
#             queue = []
#             level_result = []
#             while len(level_queue)>0:
#                 current = level_queue.pop(0)
#                 level_result.append(current.val)
#                 if current.left:
#                     queue.append(current.left)
#                 if current.right:
#                     queue.append(current.right)
          
#             result.append(level_result)
            
#             if idx % 2 == 1:
                
            
#             idx +=1
        
#         return result 
        
        
        
        
        
        
#         if root == None:
#             return None
        
#         idx = 0
#         queue = []
#         result = []
#         queue.append(root)
#         while len(queue)>0:
#             level_queue = queue
#             queue = []
#             level_result = []
#             while len(level_queue)>0:
#                 current = level_queue.pop(0)
#                 level_result.append(current.val)
#                 if idx % 2 == 1:
#                     #left then right
#                     if current.left:
#                         queue.append(current.left)
#                     if current.right:
#                         queue.append(current.right)
#                 else:
#                     #right then left
#                     if current.right:
#                         queue.append(current.right)
#                     if current.left:
#                         queue.append(current.left)
#             idx+=1
#             result.append(level_result)
        
#         return result