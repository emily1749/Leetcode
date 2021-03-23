# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root == None: return None
        # dummy = TreeNode()
        # prev = dummy
        stack = [root]
        dummy = TreeNode()
        prev = dummy
        while len(stack)>0:
            current = stack.pop()
            prev.right = current
            prev.left = None
            prev = current
            if current.right: stack.append(current.right)
            if current.left: stack.append(current.left)
        return dummy.right
#             curr = node                
#             temp_right, temp_left = node.right, node.left
#             if node.left: curr.right = node.left
#             if not node.left and node.right: curr.right = node.right
#             node.left = None
#             if temp_left: preorder(temp_left)
#             if temp_right: preorder(temp_right)
#             return node
            
            # if node == None:
            #     return None
            # temp_right, temp_left = node.right, node.left
            # # node.right = node.left
            # node.left = None
            # node.right = preorder(temp_left)
            # preorder(temp_right)
            # return node
        # preorder(root)
        # return root