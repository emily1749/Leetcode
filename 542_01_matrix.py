class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        height = len(matrix)
        width = len(matrix[0])
        
        def bfs(i, j):
            levels = 0
            seen = set()
            queue = collections.deque()
            queue.append((i, j))
            while len(queue)>0:
                level_queue = queue
                queue=collections.deque()
                while len(level_queue) > 0:
                    current = level_queue.popleft()
                    seen.add(current)
                    curr_i, curr_j = current[0], current[1]
                    if matrix[curr_i][curr_j] == 0: return levels
                    for r,c in ((curr_i-1, curr_j), (curr_i+1, curr_j), (curr_i, curr_j+1), (curr_i, curr_j-1)):
                        if 0<=r<len(matrix) and 0<=c<len(matrix[0]) and (r, c) not in seen:
                            queue.append((r, c))
                    # if curr_i-1>=0 and (curr_i-1, curr_j) not in seen:
                    #     queue.append((curr_i-1, curr_j))
                    # if curr_i+1<len(matrix) and (curr_i+1, curr_j) not in seen:
                    #     queue.append((curr_i+1, curr_j))
                    # if curr_j-1>=0 and (curr_i, curr_j-1) not in seen:
                    #     queue.append((curr_i, curr_j-1))
                    # if curr_j+1<len(matrix[0]) and (curr_i, curr_j+1) not in seen:
                    #     queue.append((curr_i, curr_j+1))
                levels+=1
                
            return levels
            
        
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 1:
                    matrix[i][j] = bfs(i, j)
                    
        return matrix