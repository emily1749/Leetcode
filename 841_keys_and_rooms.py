class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        queue = collections.deque([0])
        seen = {0}
        while queue:
            current_key = queue.popleft()
            for keys in rooms[current_key]:
                if keys not in seen:
                    seen.add(keys)
                    queue.append(keys)
            if len(seen) == len(rooms):
                return True
            
        return False
