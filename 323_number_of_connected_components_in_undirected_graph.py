class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if edges == None: return 0
        
        graph = defaultdict(list)
        # adjacency list
        for edge in edges:
            a, b = edge[0], edge[1]
            graph[a].append(b)
            graph[b].append(a)
        print(graph)
        
        def dfs(vertex):
            for neighbor in graph[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        seen = set()
        count = 0
        
        for vertex in graph:
            if vertex not in seen:
                print(vertex)
                seen.add(vertex)
                dfs(vertex)
                count += 1
        unseen_nodes = n-len(seen)
        return count + unseen_nodes