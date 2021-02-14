class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i = len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]:
                # j = i + 1
                # while j < len(nums):           
            i-=1
        if i == -1: 
            nums.reverse()
            return
        j = i+1
        while j<len(nums) and nums[j]>nums[i]:
            j += 1
        
        j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        l, r = i+1, len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
            
        # nums = nums[:i+1] + nums[i+1:j].reverse() + nums[j:]
        return
        

        # i = j = len(nums)-1
        # while i > 0 and nums[i-1] >= nums[i]:
        #     i -= 1
        # if i == 0:   # nums are in descending order
        #     nums.reverse()
        #     return 
        # k = i - 1    # find the last "ascending" position
        # while nums[j] <= nums[k]:
        #     j -= 1
        # nums[k], nums[j] = nums[j], nums[k]  
        # l, r = k+1, len(nums)-1  # reverse the second part
        # while l < r:
        #     nums[l], nums[r] = nums[r], nums[l]
        #     l +=1 ; r -= 1