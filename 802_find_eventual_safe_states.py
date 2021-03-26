class Solution(object):
    def eventualSafeNodes(self, graph):

        def is_cycle(curr):
            if colors[curr] == 2:
                return False
            if colors[curr] == 1:
                return True
            colors[curr] = 1
            for neighbor in graph[curr]:
                if is_cycle(neighbor):
                    return True
            colors[curr] = 2
            return False
            
        
        colors = [0]*len(graph)
        for i in range(len(graph)):
            if colors[i] == 0:
                is_cycle(i)
        return [node for node in range(len(colors)) if colors[node] == 2]
# class Solution(object):
#     def eventualSafeNodes(self, graph):
#         """
#         :type graph: List[List[int]]
#         :rtype: List[int]
#         """
#         # WHITE, GREY, BLACK = 1, 2, 3
#         colors = [0]*len(graph)
        
#         def dfs(curr):
#             if colors[curr] != 0:
#                 return
#             colors[curr] = 1
#             for neighbor in graph[curr]:
#                 # if graph[neighbor] == 2:
#                 #     continue
#                 dfs(neighbor)
#             colors[curr] = 2
        
#         for i in range(len(graph)):
#             if colors[i] == 0:
#                 dfs(i)
#         print(colors)
#         return 
    
    
#         seen = set()
#         result = []
#         current_seen = defaultdict(int)
#         cycle = set()
        
#         def dfs(curr):
#             if current_seen[curr] == 2: 
#                 continue
#             current_seen[curr] = 1
#             for neighbor in graph[curr]:
#                 if current_seen[neighbor] == 1:
#                     cycle.update(current_seen)
#                     break
#                 dfs(neighbor)
#             current_seen[curr] = 2
        
#         for i in range(len(graph)):
#             if i not in seen:
#                 current_seen = set()
#                 dfs(i)
#                 seen.update(current_seen)
#         for i in range(len(graph)):
#             if i not in cycle:
#                 result.append(i)
#         return result