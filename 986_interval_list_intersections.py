class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        a_idx = 0
        b_idx = 0
        result = []
        while a_idx < len(firstList) and b_idx< len(secondList):
            a_start, a_end = firstList[a_idx]
            b_start, b_end = secondList[b_idx]
            start = max(a_start, b_start)
            end = min(a_end, b_end)
            if start <= end:
                result.append([start, end])
            if a_end<b_end:
                a_idx+=1
            else:
                b_idx+=1
        return result
            
            