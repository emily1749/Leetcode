class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1]
        for i in range(1, len(nums)):
            element = result[i-1]
            element *= nums[i-1]
            result.append(element)

        product = 1
        for i in range(len(nums)-2, -1, -1):
            product *= nums[i+1]
            result[i] = result[i]*product
        
        return result
            