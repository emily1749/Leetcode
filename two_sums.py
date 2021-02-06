class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myHash = {}
        for idx, numb in enumerate(nums):
            if numb in myHash:
                return [myHash[numb], idx]
            else:
                myHash[target-numb] = idx
        
        
        