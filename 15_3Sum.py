class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        print(nums)
        result = []
        for integer in range(len(nums)):
            left = integer+1
            right = len(nums)-1
            target = nums[integer]*-1
            if integer ==0 or nums[integer-1] != nums[integer]:
                while left < right:
                    two_sum = nums[left] + nums[right]
                    if two_sum == target:
                        result.append([nums[integer], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left< right and nums[left] == nums[left - 1]:
                            left += 1
                    elif two_sum < target:
                        left+=1
                    elif two_sum > target:
                        right -= 1
        return result