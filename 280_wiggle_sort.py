class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if i%2 == 0:
                if nums[i+1]<nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                if nums[i+1]>nums[i]:
                    nums[i], nums[i+1]=nums[i+1], nums[i]
            
#         heap = nums[:len(nums)/2]
#         heapq.heapify(heap)
#         index = 0
#         for i in range(len(nums)/2, len(nums)):
#             nums[index] = heapq.heappushpop(heap, nums[i])
#             index += 2
#         index = 1
#         while len(heap)>0:
#             nums[index] = heapq.heappop(heap)
#             index += 2
            
        