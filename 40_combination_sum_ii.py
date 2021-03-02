class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(remaining, combo, curr, counter):
            if remaining == 0:
                # combo.sort()
                # if combo not in result:
                result.append(combo[:])
                return
            if remaining < 0:
                return
            for next_curr in range(curr, len(counter)):
                # print(next_curr)
                # print(counter)
                # print(counter[next_curr])
                number, count = counter[next_curr][0], counter[next_curr][1]
                if count>0:
                    combo.append(number)
                    counter[next_curr][1]-= 1
                    backtrack(remaining-number, combo, next_curr, counter)
                    counter[next_curr][1] += 1
                    combo.pop()
                
        candidates.sort()
        counter = Counter(candidates)
        counter = [[c, counter[c]] for c in counter]
        # print(counter)
        
        
        backtrack(target, [], 0, counter)
        return result