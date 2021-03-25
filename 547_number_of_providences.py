class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        adj_list = {}
        for i in range(len(isConnected)):
            adj_list[i] = []
            for j in range(len(isConnected[0])):
                if i==j: continue
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)
        queue = collections.deque()
        count = 0
        seen = set()
        for node in adj_list:
            if node in seen: continue
            queue.append(node)
            seen.add(node)
            while len(queue)>0:
                current = queue.popleft()
                for neighbor in adj_list[current]:
                    if neighbor not in seen:
                        queue.append(neighbor)
                        seen.add(neighbor)
            count += 1
    
        return count