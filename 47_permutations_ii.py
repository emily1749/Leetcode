class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # count = Counter({numb: 0 for numb in nums})
        # for numb in nums:
        #     count[numb] += 1
        # # print(count)
        result = []
        def backtrack(nums, combo, count):
            if len(combo) == len(nums):
                
                result.append(combo[:])
                return
            for num in count:
                print(count)
                # if already in it continue
                if count[num] == 0:
                    continue
                
                combo.append(num)
                count[num] -= 1
                backtrack(nums, combo, count)
                count[num] += 1
                combo.pop()
        
        backtrack(nums, [], Counter(nums))
        return result