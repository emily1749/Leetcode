# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """

        
        def check_path(node, target, path):
            if node == None: return
            
            current_sum = target-node.val
            path.append(node.val)

            if not node.left and not node.right and current_sum == 0:
                result.append(path[::])
                
            else:
                check_path(node.left, current_sum, path) 
                check_path(node.right, current_sum, path)
                
            path.pop()
        
        result = []
            
        check_path(root, targetSum, [])
        return result