class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest_sum = float("inf")
        nums = sorted(nums)
        final_total = 0
        for i in range(len(nums) -2):
            left = i+1
            right = len(nums)-1
            
            while left<right:
                total = nums[i] + nums[left] + nums[right]
                current_sum = target - total
                if closest_sum > abs(current_sum):
                    closest_sum = abs(current_sum)
                    final_total = total
                if total > target:
                    right -= 1
                else:
                # if target - total < 0:
                    left += 1
        
        return final_total