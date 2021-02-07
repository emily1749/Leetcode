class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for integer in nums:
            if nums[abs(integer)-1]>0:
                nums[abs(integer)-1] = nums[abs(integer)-1]*-1
        
        result = []
        for i in range(len(nums)):
            if nums[i]>0:
                result.append(i+1)
        return result