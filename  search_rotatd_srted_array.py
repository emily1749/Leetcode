class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
         
        while(left<=right):
            middle = int((left+right)/2)
            if nums[middle]==target:
                return middle
            if nums[left]<=nums[middle]:
                if(nums[left]<=target and target<=nums[middle]):
                    #target on left side
                    right = middle-1
                else:
                    #target on right side
                    left = middle+1
            else:
                if(nums[middle]<=target and target<=nums[right]):
                    left = middle+1
                else:
                    right = middle-1
        
        return -1