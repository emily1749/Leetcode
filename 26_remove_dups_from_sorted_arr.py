class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1: return len(nums)
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                curr_idx = i
                next_idx = i+1
                prev = nums[i-1]
                while next_idx < len(nums):
                    while next_idx<len(nums) and nums[next_idx] == prev:
                        next_idx += 1
                    if next_idx == len(nums): return curr_idx
                    nums[curr_idx] = nums[next_idx]
                    prev = nums[curr_idx]
                    curr_idx+=1
                    next_idx +=1
                return curr_idx
        return len(nums)