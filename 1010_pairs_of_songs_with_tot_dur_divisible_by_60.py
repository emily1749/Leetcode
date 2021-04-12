class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        hash_remaining = defaultdict(int)
        total = 0
        for i in range(len(time)):
            remaining_needed = 60 - (time[i]%60)
            if remaining_needed == 60: remaining_needed = 0
            if remaining_needed in hash_remaining:
                total += hash_remaining[remaining_needed]
            hash_remaining[time[i]%60] += 1
        return total
    #time: O(N)
    #space:O(N)