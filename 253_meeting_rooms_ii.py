class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals)
        heap = [intervals[0][1]]
        heapq.heapify(heap)
        for i in range(1, len(intervals)):
            if intervals[i][0] < heap[0]:
                heapq.heappush(heap, intervals[i][1])
            else:
                heapq.heappop(heap)
                heapq.heappush(heap,intervals[i][1])
        return len(heap)