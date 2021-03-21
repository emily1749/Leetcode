# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.result = None
        self.min_diff = float("inf")
        def find_value(node):
            curr_diff = abs(node.val - target)
            if self.min_diff > curr_diff:
                self.min_diff = curr_diff
                self.result = node.val
            if target<node.val and node.left:
                find_value(node.left)
            elif target>node.val and node.right:
                find_value(node.right)
            
        find_value(root)
        return self.result
    
    
                # curr_diff = abs(node.val - target)
            # left_diff, right_diff = float("inf"), float("inf")
            # if node.left: left_diff = abs(node.left.val - target)
            # if node.right: right_diff = abs(node.right.val - target)
            # # print(curr_diff)
            # # print(left_diff)
            # # print(right_diff)
            # minimum = min(curr_diff, min(left_diff, right_diff))
            # if minimum == curr_diff: 
            #     self.result = node.val
            #     return
            # elif minimum == left_diff:
            #     find_value(node.left)
            # elif minimum == right_diff:
            #     find_value(node.right)