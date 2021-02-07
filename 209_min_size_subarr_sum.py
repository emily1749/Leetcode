class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i=0
        min_count = float("inf")
        total_sum = 0
        
        for j in range(len(nums)):
            total_sum+=nums[j]
                
            if total_sum>=target:
                while total_sum>=target:
                    min_count = min(min_count, j-i+1)
                    total_sum-=nums[i]
                    i+=1
                # i-=1
                # total_sum+=nums[i]
               

            
        if min_count == float("inf"):
            min_count = 0
        return min_count