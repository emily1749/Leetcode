class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for numb in nums:
            if nums[abs(numb)-1]<0:
                result.append(abs(numb))
            else:
                nums[abs(numb)-1] = nums[abs(numb)-1]*-1
            
        return result