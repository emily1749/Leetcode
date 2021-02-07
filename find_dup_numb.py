class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for integer in nums:
            print(integer)
            if nums[abs(integer)-1]<0:
                return abs(integer)
            else:
                nums[abs(integer)-1] = nums[abs(integer)-1]*-1