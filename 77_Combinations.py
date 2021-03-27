class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(combo, start):
            if len(combo) == k:
                result.append(combo[:])
                return
            for i in range(start, n):
                combo.append(i+1)
                backtrack(combo, i+1)
                combo.pop()
        backtrack([], 0)
        return result