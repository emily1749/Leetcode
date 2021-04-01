import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = nums[:k]
        heapq.heapify(pq)
        for i in range(k, len(nums)):
            heapq.heappush(pq, nums[i])
            heapq.heappop(pq)
            
        return pq[0]