class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height, width = len(grid), len(grid[0])
        seen = set()
        max_island = 0
        self.count = 0
        def dfs(i, j):
            seen.add((i, j))
            self.count += 1
            for r, c in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0<=r<height and 0<=c<width and grid[r][c] == 1 and (r,c) not in seen:
                    dfs(r, c)
            
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1 and (i, j) not in seen:
                    self.count = 0
                    dfs(i, j)
                    max_island = max(max_island, self.count)
        
        return max_island