class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        array = triangle[len(triangle)-1]
        
        for i in range(len(triangle)-2, -1, -1):
            print(i)
            for j in range(len(triangle[i])):
                minimum = min(triangle[i][j]+array[j], triangle[i][j]+array[j+1])
                array[j] = minimum
        
        return array[0]