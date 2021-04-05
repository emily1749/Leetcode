class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, max_count, curr_count = 0, 0, 0
        while i<len(nums):
            curr_count = 0
            while i < len(nums) and nums[i] == 1:
                curr_count += 1
                i += 1
            max_count = max(max_count, curr_count)
            i+=1
        return max_count