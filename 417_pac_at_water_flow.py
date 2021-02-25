class Solution(object):
    def pacificAtlantic(self, matrix):
        
        if matrix == []: return []
        
        height = len(matrix)
        width = len(matrix[0])
        
        pacific = [[False for _ in range(width)] for _ in range(height)]
        atlantic = [[False for _ in range(width)] for _ in range(height)]
        
        def dfs(matrix, row, col, result, previous):
            if row<0 or col<0 or row>=len(matrix) or col>=len(matrix[0]) or result[row][col] or matrix[row][col]<previous:
                return
            
            result[row][col] = True
            dfs(matrix, row+1, col, result, matrix[row][col])
            dfs(matrix, row-1, col, result, matrix[row][col])
            dfs(matrix, row, col-1, result, matrix[row][col])
            dfs(matrix, row, col+1, result, matrix[row][col])
        print(pacific)
        for i in range(width):
            dfs(matrix, 0, i, pacific, matrix[0][i])
            dfs(matrix, height-1, i, atlantic, matrix[height-1][i])
        # print(atlantic)
        print(pacific)
        for i in range(height):
            dfs(matrix, i, 0, pacific, matrix[i][0])
            dfs(matrix, i, width-1, atlantic, matrix[i][width-1])
        
        result = []
        
        for row in range(height):
            for col in range(width):
                if atlantic[row][col] and pacific[row][col]:
                    result.append([row, col])
                    
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# class Solution(object):
#     def pacificAtlantic(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[List[int]]
#         """
        
        
        
#         if not matrix:
#             return []
        
        
#         def dfs(i, j, matrix, OC, pre):
#             """
#             :type i: int
#             :type j: int
#             :type matrix: List[List[int]]
#             :type OC: List[List[boolean]]
#             :type pre: int
#             :rtype None
#             """

#             # base case:
#             if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or OC[i][j] or matrix[i][j]<pre:
#                 return

#             # recursive rule:
#             OC[i][j] = True
#             dfs(i+1, j, matrix, OC, matrix[i][j])
#             dfs(i-1, j, matrix, OC, matrix[i][j])
#             dfs(i, j-1, matrix, OC, matrix[i][j])
#             dfs(i, j+1, matrix, OC, matrix[i][j])
            
#         m = len(matrix)
#         n = len(matrix[0])
#         P = [[False]*n for i in xrange(m)]
#         A = [[False]*n for i in xrange(m)]
#         res = []
#         for i in xrange(m): 
#             dfs(i, 0, matrix, P, 0)     # start from first col for P
#             dfs(i, n-1, matrix, A, 0)   # start from last col for A
#         print(P)
#         print(A)
#         for j in xrange(n): 
#             dfs(0, j, matrix, P, 0)     # start from first row for P
#             dfs(m-1, j, matrix, A, 0)   # start from last row for A
#         for i in xrange(m):
#             for j in xrange(n):
#                 if P[i][j] and A[i][j]:
#                     res.append([i,j])
#         return res
    
        

# class Solution(object):
#     def __init__(self):
#         self.result = []
    
#     def pacificAtlantic(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[List[int]]
#         """
        
#         if matrix == []: return []
        
#         height = len(matrix)
#         width = len(matrix[0])
        
#         pacific = [[False for _ in range(width)] for _ in range(height)]
#         atlantic = [[False for _ in range(width)] for _ in range(height)]
        
           
#         def dfs(matrix, row, col, prev, result):
#             # out of bounds
#             if row<0 or col<0 or row>=len(matrix) or col>=len(matrix[0]) or result[row][col] or matrix[row][col]<prev:
#                 return
                    
#             #call dfs
#             result[row][col] = True
#             dfs(matrix, row+1, col, matrix[row][col], result)
#             dfs(matrix, row-1, col, matrix[row][col], result)
#             dfs(matrix, row, col+1, matrix[row][col], result)
#             dfs(matrix, row, col-1, matrix[row][col], result)
            
        
#         # pacific = ()
#         # atlantic = ()
        
#         for i in range(width):
#             dfs(matrix, 0, i, matrix[0][i], pacific)
#             dfs(matrix, height-1, i, matrix[height-1][i], atlantic)

#             # dfs(matrix, 0, i, matrix[0][i], [[False for _ in range(width)] for _ in range(height)])
#             # pacific+=((row, col)),
#             # dfs(matrix, height-1, i, matrix[height-1][i], [[False for _ in range(width)] for _ in range(height)])
#             # atlantic+=((row, col)),
#         # print(result)
#         for j in range(height):
#             dfs(matrix, j, 0, matrix[0][i], pacific)
#             dfs(matrix, j, width-1, matrix[height-1][i], atlantic)
#         #     row, col = dfs(matrix, j, 0, matrix[j][0], [[False for _ in range(width)] for _ in range(height)])
#         #     pacific+=((row, col)),
#         #     row, col = dfs(matrix, j, width-1, matrix[j][width-1], [[False for _ in range(width)] for _ in range(height)])
#         #     atlantic+=((row, col)),
#         print(pacific)
#         print(atlantic)
#         result = []
#         pacific[0][width-1] = True
#         pacific[height-1][0] = True
#         atlantic[0][width-1] = True
#         atlantic[height-1][0] = True
#         for row in range(height):
#             for col in range(width):
#                 if pacific[row][col] and atlantic[row][col]:
#                     result.append([row, col])
                    
#         return result
        
        
# #         # # pacific+=atlantic
# #         # print(pacific)
# #         # list(pacific)
# #         # print(list(pacific))
# #         # res = list(set(atlantic).intersection(set(pacific))) 

# #         # return res
        
# #         # return result