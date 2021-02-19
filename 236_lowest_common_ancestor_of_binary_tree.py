# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def search(node, p, q):
            if node == None:
                return False, False
            l_p_bool, l_q_bool = search(node.left, p, q)
            r_p_bool, r_q_bool = search(node.right, p, q)
            p_bool = False
            q_bool = False
            if (node.val == p.val or l_p_bool or r_p_bool): p_bool = True
            if (node.val == q.val or l_q_bool or r_q_bool): q_bool = True
                    
            if p_bool and q_bool:
                if self.solution_flag:
                    return True, True
                else:
                    self.solution_flag = True
                    self.solution = node
                    return True, True
            else: 
                return p_bool, q_bool
            
        self.solution_flag = False
        self.solution = None
        search(root, p, q)
        return self.solution