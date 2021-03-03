class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array = [1 for _ in range(len(nums))]
        maximum = 1
        for i in range(1, len(nums)):
            max_count = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    max_count = max(array[j] + 1, max_count)
            
            array[i] = max_count
            maximum = max(array[i], maximum)
            
        # maximum = 0
        # for numb in array:
        #     maximum = max(numb, maximum)
        return maximum