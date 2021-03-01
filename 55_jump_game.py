class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #TOP DOWN
        
        
        #BOTTOM UP
        if len(nums)<=1: return True
        prev = 1
        for i in range(len(nums)):
            if prev < 1:
                return False
            prev = max(prev-1, nums[i])
        
        return True
    
    #space - O(1)
    #time - O(N)