class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        items = []
        for point in points:
            items.append((-(point[0]**2 + point[1]**2)**.5, point))
        heap = items[:K]
        heapq.heapify(heap)
        for i in range(K, len(items)):
            heapq.heappushpop(heap, items[i])
        return [item[1] for item in heap]
        