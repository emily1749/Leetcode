# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        
        def calc_path(node, path):
            # if node == None:
            #     return
            path.append(str(node.val))
            if not node.left and not node.right:
                result.append("->".join(path))
            if node.left: calc_path(node.left, path)
            if node.right: calc_path(node.right, path)
            path.pop()
            # result.append("->".join(path))
            
        calc_path(root, []) 
        return result