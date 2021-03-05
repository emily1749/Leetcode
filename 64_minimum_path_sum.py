class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == []: return 0
        
        width, height = len(grid[0]), len(grid)
        array = [False for _ in range(width)]
        array[0] = grid[0][0]
        
        for j in range(1, width):
            array[j] = array[j-1]+grid[0][j]
                    
        for i in range(1, height):
            prev = array[0] + grid[i][0]
            array[0] = prev
            for j in range(1, width):
                minimum = min(prev, array[j])
                integer = minimum + grid[i][j]
                array[j], prev = integer, integer
        
        return array[width-1]