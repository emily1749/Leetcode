class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(subset, index):
            if index == len(nums):
                # subset.sort()
                if subset not in result:
                    result.append(subset[:])
                return
            # for i in range(index, len(nums)):
            subset.append(nums[index])
            backtrack(subset, index+1)
            subset.pop()
            backtrack(subset, index+1)
            
        nums.sort()
        backtrack([], 0)
        return result
#         result = []
#         counter = Counter(nums)
#         counter = [[number, counter[number]] for number in counter]
        
#         def backtrack(index, combo, counter):
#             if index == len(nums):
#                 result.append(combo[:])
#                 return
#             if counter[index][1]>0:
#                 counter[index][0] -= 1
#                 combo.append(counter[index][0])
#                 backtrack(index, combo, counter)
#                 combo.pop()
#                 backtrack(index, combo, counter)