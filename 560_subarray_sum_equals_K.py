class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maps = {0:1}
        sums = 0
        res = 0
        for i in nums:
            sums += i
            if sums-k in maps:
                res += maps[sums-k]
            maps[sums] = maps.get(sums,0) + 1
        return res

    
       # counts = defaultdict(int)
        # counts[0] = 1
        # total_sum = 0
        # count = 0
        # for i in range(len(nums)):
        #     total_sum += nums[i]
        #     if total_sum - k in counts:
        #         count += counts[total_sum-k]
        #         counts[total_sum] += 1
        #     else:
        #         counts[total_sum] = 1
        # return count
        
        
        #brute force
        # count = 0
        # for i in range(len(nums)):
        #     total = 0
        #     for j in range(i, len(nums)):
        #         total += nums[j]
        #         if total == k:
        #             count +=1
        # return count