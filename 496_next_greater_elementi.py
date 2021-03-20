class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = [-1] * len(nums1)
        nums1_indexes = {}
        for i in range(len(nums1)):
            nums1_indexes[nums1[i]] = i
        stack = []
        for num in nums2:
            # if len(stack) == 0 or num <= stack[-1]:
            #     stack.append(num)
            # elif num <= stack[-1]:
            #     stack.append(num)
            while len(stack) > 0 and num > stack[-1]:
                if stack[-1] in nums1_indexes:
                    result[nums1_indexes[stack[-1]]] = num
                stack.pop()
            stack.append(num)
        return result
        #O(len(num1) + len(num2))
        #O(len(num1) + len(num2))
        
        
        #brute force
        # result = []
        # for i in range(len(nums1)):
        #     next_greater = float("inf")
        #     index = nums2.index(nums1[i])
        #     for j in range(index, len(nums2)):
        #         if nums2[j] > nums1[i]:
        #             next_greater = nums2[j]
        #             result.append(next_greater)
        #             break
        #     if next_greater == float("inf"):
        #         result.append(-1)
            # else:
            #     result.append(next_greater)
        
        # return result