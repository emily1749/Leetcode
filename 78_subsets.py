class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(subset, index):
            if index == len(nums):
                result.append(subset[:])
                return
            # for i in range(index, len(nums)):
            subset.append(nums[index])
            backtrack(subset, index+1)
            subset.pop()
            backtrack(subset, index+1)
        
        backtrack([], 0)
        return result
            