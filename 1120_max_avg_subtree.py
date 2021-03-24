# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        if root == None: return 0
        self.avg_max = 0
        def calc_avg(node):
            if node == None:
                return 0, 0, 0
            avgL, total_nodesL, total_sumL = calc_avg(node.left)
            avgR, total_nodesR, total_sumR = calc_avg(node.right)
            total_sum = float(total_sumL + total_sumR + node.val)
            total_nodes = total_nodesL + total_nodesR + 1
            curr_avg = float(total_sum/total_nodes)
            self.avg_max = max(self.avg_max, curr_avg)
            return curr_avg, total_nodes, total_sum
        
        calc_avg(root)
        return self.avg_max