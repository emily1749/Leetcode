# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        adj_list = defaultdict(list)
        def build_adj_list(node):
            if node.left:
                adj_list[node.val].append(node.left.val)
                adj_list[node.left.val].append(node.val)
                build_adj_list(node.left)
            if node.right:
                adj_list[node.val].append(node.right.val)
                adj_list[node.right.val].append(node.val)
                build_adj_list(node.right)
        build_adj_list(root)
        
        count = 0
        result = []
        visited = set()
        queue = collections.deque([target.val])
        while queue:
            level = queue
            queue = collections.deque()
            for node in level:
                if count == K:
                    result.append(node)
                visited.add(node)
                for current in adj_list[node]:
                    if current not in visited:
                        queue.append(current)
            count += 1
            if count > K:
                break
                
        return result
