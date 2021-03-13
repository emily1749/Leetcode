class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        
        while l<r:
            # print("left")
            # print(l)
            # print("right")
            # print(r)
            m = int(l + ((r-l)/2))
            if nums[m] == target:
                return m
            if nums[r] < nums[m]:
                if target<nums[m] and target>=nums[l]:
                    r = m-1
                else:
                    l = m+1
            if nums[r] > nums[m]:
                if target<=nums[r] and target> nums[m]:
                    l = m+1
                else:
                    r = m-1
        
        if nums[l] == target:
            return l
        else:
            return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         left = 0
#         right = len(nums)-1
         
#         while(left<=right):
#             middle = int((left+right)/2)
#             if nums[middle]==target:
#                 return middle
#             if nums[left]<=nums[middle]:
#                 if(nums[left]<=target and target<=nums[middle]):
#                     #target on left side
#                     right = middle-1
#                 else:
#                     #target on right side
#                     left = middle+1
#             else:
#                 if(nums[middle]<=target and target<=nums[right]):
#                     left = middle+1
#                 else:
#                     right = middle-1
        
#         return -1