class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        width = len(grid[0])
        seen = set()
        def dfs(i, j):
            if i<0 or i>=height or j<0 or j>=width or (i, j) in seen or grid[i][j] == 0:
                return
            seen.add((i, j))
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            
        for i in range(height):
            if grid[i][0] == 1: dfs(i, 0)
            if grid[i][width-1] == 1: dfs(i, width-1)
        for j in range(width):
            if grid[0][j] == 1: dfs(0, j)
            if grid[height-1][j] == 1: dfs(height-1, j)
        count = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1 and (i, j) not in seen:
                    count += 1
        return count