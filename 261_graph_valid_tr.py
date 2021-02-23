class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
         
        if len(edges) != n - 1: return False

        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        parent = {0: -1}
        queue = collections.deque([0])

        while queue:
            node = queue.popleft()
            for neighbour in adj_list[node]:
                if neighbour == parent[node]:
                    continue
                if neighbour in parent:
                    return False
                parent[neighbour] = node
                queue.append(neighbour)

        return len(parent) == n
#         if len(edges) != n-1: return False
#         #create adjacency matrix
#         adj_matrix = defaultdict(list)
#         for edge in edges:
#             first, second = edge[0], edge[1]
#             # if edge not in adj_matrix:
#             adj_matrix[first].append(second)
#         print(adj_matrix)
        
#         parent = {0: -1}
#         queue = collections.deque([0])
        
#         while queue:
#             node = queue.popleft()
#             for neighbor in adj_matrix[node]:
#                 if neighbor == parent[node]:
#                     continue
#                 if neighbor in parent:
#                     return False
#                 parent[neighbor] = node
#                 queue.append(neighbor)
        
#         return len(parent) == n
                