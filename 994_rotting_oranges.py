class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        width = len(grid[0])
        height = len(grid)
        rotten = collections.deque()
        rotten_level = collections.deque()
        not_rotten = set()
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 2: rotten_level.append((i,j))
                elif grid[i][j] == 1: not_rotten.add((i, j))
        
        rotten.append(rotten_level)
        count = 0
        while len(rotten) > 0 and len(not_rotten) > 0:
            curr_level = rotten.popleft()
            rotten_level = collections.deque()
            while len(curr_level) > 0 and len(not_rotten) > 0:
                curr = curr_level.popleft()
                # print('here')
                # print(curr)
                curr_i = curr[0]
                curr_j = curr[1]
                if curr_i-1>=0 and (curr_i-1, curr_j) in not_rotten:
                    not_rotten.remove((curr_i-1, curr_j))
                    rotten_level.append((curr_i-1, curr_j))
                if curr_i+1<height and (curr_i+1, curr_j) in not_rotten:
                    not_rotten.remove((curr_i+1, curr_j))
                    rotten_level.append((curr_i+1, curr_j))
                if curr_j-1>=0 and (curr_i, curr_j-1) in not_rotten:
                    print('here')
                    not_rotten.remove((curr_i, curr_j-1))
                    rotten_level.append((curr_i, curr_j-1))
                if curr_j+1<width and (curr_i, curr_j+1) in not_rotten:
                    not_rotten.remove((curr_i, curr_j+1))
                    rotten_level.append((curr_i, curr_j+1))
            # print(not_rotten)
            if len(rotten_level) ==0 and len(rotten) == 0 and len(not_rotten) > 0: return -1
            # print(rotten_level)
            # print(rotten)
            # print(len(rotten_level))
            # print(len(rotten))
            rotten.append(rotten_level)
            count += 1
            
        return count