class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums == None: return 0
        
        result = [0]*(len(nums)+2)
        
        for i in range(2, len(nums)+2):
            result[i] = max(nums[i-2]+result[i-2], result[i-1])
        
        return result[len(nums)+1]