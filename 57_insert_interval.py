class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
        result = []
        result.append(intervals[0])
        interval_idx = 1
        while interval_idx < len(intervals):
            result_idx = len(result)-1
            if intervals[interval_idx][0]<=result[result_idx][1]:
                first =  min(intervals[interval_idx][0], result[result_idx][0])
                second = max(intervals[interval_idx][1], result[result_idx][1])
                result[result_idx] = [first, second]
                interval_idx += 1
                
            else:
                result.append(intervals[interval_idx])
                interval_idx += 1
                
        return result