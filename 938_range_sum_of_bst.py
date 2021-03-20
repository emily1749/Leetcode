# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        #DFS
        self.summation = 0
        def traverse(node):
            if node.val >= low and node.val <= high:
                self.summation += node.val
            if node.left and node.val >= low: traverse(node.left)
            if node.right and node.val <= high: traverse(node.right)
        traverse(root)
        return self.summation
        
        #BFS
#         if root == None: return 0
#         queue = collections.deque([root])
        
#         summation = 0
#         while len(queue) > 0:
#             current = queue.popleft()
#             if current.left: queue.append(current.left)
#             if current.right: queue.append(current.right)
#             if current.val >= low and current.val <= high:
#                 summation += current.val
#         return summation
    
        #RECURSION
#         def add_sums(node):
#             if node == None:
#                 return 0
#             node_sums = add_sums(node.left) + add_sums(node.right)
#             if node.val >= low and node.val <= high:
#                 node_sums += node.val
#             return node_sums
#         return add_sums(root)
    
    #time O(N)
    #space O(height)