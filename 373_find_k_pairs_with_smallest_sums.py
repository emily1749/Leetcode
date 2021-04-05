class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2: return []
        h = []
        
        # pair combination
        for i in range(len(nums1)):
            heapq.heappush(h, (nums1[i] + nums2[0], i, 0))

        # return k smallest pairs
        res = []
        while h and k > 0:
            small, i, j = heapq.heappop(h)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
            k -= 1
        
        return res
#         nums = []
#         for num1 in nums1:
#             for num2 in nums2:
#                 nums.append((-(num1+num2), [num1, num2]))
#         heap = nums[:k]
#         heapq.heapify(heap)
#         for i in range(k, len(nums)):
#             heapq.heappushpop(heap, nums[i])
        
#         return [num[1] for num in heap]