# class Solution(object):
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

# class Solution(object):
def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        my_hash = {}
        for numb in nums:
            if numb not in my_hash:
                my_hash[numb] = 1
        
        result = []
        for i in range(1, len(nums)+1):
            if i not in my_hash:
                result.append(i)
                
        return result