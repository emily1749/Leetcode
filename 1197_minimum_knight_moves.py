class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        queue = collections.deque([(0, 0, 0)])
        seen = set()
        seen.add((0, 0))
        # seen.append((0, 0))
        # steps = -1
        while len(queue)>0:
            # curr = queue.popleft()
            i, j, steps = queue.popleft()
            if i == x and j == y: return steps
            # seen.add((i, j))
            dires = [(i-1,j-2),(i-2,j-1),(i-2,j+1),(i-1,j+2),(i+1,j-2),(i+2,j-1),(i+1,j+2),(i+2,j+1)] 
            for r, c in dires:
                if (r, c) not in seen:
                    seen.add((r, c))
                    queue.append((r, c, steps+1))
            # # level = queue
            # # queue = collections.deque()
            # # steps += 1
            # while len(level)>0:
            #     curr = level.popleft()
            #     i, j = curr[0], curr[1]
            #     if i == x and j == y: return steps
            #     seen.add(curr)
            #     for r, c in [(i+2, j+1), (i+1, j+2), (i+2, j-1), (i+1, j-2), (i-1, j-2), (i-2, j-1), (i-2, j+1), (i-1, j+2)]:
            #         if (r, c) not in seen:
            #             queue.append((r, c))
        