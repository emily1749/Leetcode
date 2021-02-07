class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        top = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        left = 0
        roundIdx = 0
        
        while top<=bottom and right>=left:
            index = roundIdx%4
            if index==0:
                #top left to right
                for i in range(left, right+1):
                    result.append(matrix[top][i])
                top+=1
            
            elif index==1:
                #right top to bottom
                for i in range(top, bottom+1):
                    result.append(matrix[i][right])
                right-=1
                
            elif index==2:
                #bottom right to left
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom-=1
                
            else:
                #left bottom to top
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left+=1
                
            roundIdx+=1
            
        return result