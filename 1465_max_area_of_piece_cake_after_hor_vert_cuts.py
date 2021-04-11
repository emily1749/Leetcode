class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        #need the max cut of horizontal
        #need the max cut of vertical
        max_v, max_h = 0, 0
        horiz = [0] + sorted(horizontalCuts) + [h]
        #[0, 1, 2, 4, 5]
        ver = [0] + sorted(verticalCuts) + [w]
        for i in range(1, len(horiz)): 
            max_h = max(max_h, horiz[i]-horiz[i-1])
        for i in range(1, len(ver)):
            max_v = max(max_v, ver[i] - ver[i-1])
        return max_h * max_v % 1000000007