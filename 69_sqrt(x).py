class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0 
        r = x
        #res = float("inf")
        while l<=r:
            m = (l+r)/2
            powd = m*m
            if powd == x:
                return m
            if powd > x:
                r = m-1
            else:
                #res = m
                l = m+1
        return l-1