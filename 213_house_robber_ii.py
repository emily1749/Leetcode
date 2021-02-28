class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None: return 0
        if len(nums) == 1: return nums[0]
#         result = [0]*(len(nums)+2)
#         if len(nums)<1:
#             result[0] = nums[0]
#         else:
#             result[0] = nums[len(nums)-2]
#         result[1] = nums[len(nums)-1]
        prev = 0
        prev_prev = 0
        first_max = 0
        for i in range(len(nums)-1):
            # result[i] = max(nums[i-2]+result[i-2], result[i-1])
            first_max = max(nums[i]+prev_prev, prev)
            prev_prev = prev
            prev = first_max
        prev = 0
        prev_prev = 0
        second_max = 0
        for i in range(1, len(nums)):
            second_max = max(nums[i]+prev_prev, prev)
            prev_prev = prev
            prev = second_max
            
        return max(first_max, second_max)