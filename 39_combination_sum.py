class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(remaining, current_combo, start):
            if remaining == 0:
                result.append(list(current_combo))
                return
            elif remaining < 0:
                return
            for i in range(start, len(candidates)):
                current_combo.append(candidates[i])
                backtrack(remaining-candidates[i], current_combo, i)
                current_combo.pop()
        backtrack(target, [], 0)
        return result