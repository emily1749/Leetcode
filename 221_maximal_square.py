class Solution(object):
    def check_square(self, i, j, result, matrix):
            if matrix[i][j] == "0":
                return 0
            
            elif int(matrix[i][j]) > 0:
                minimum_squares = float("inf")
                minimum_squares = min(minimum_squares, int(result[i-1][j]))
                minimum_squares = min(minimum_squares, int(result[i-1][j-1]))
                minimum_squares = min(minimum_squares, int(result[i][j-1]))
                return minimum_squares+1
            
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []: return 0
        
           
                
        height = len(matrix)
        width = len(matrix[0])
        result = [[False for _ in range(width)] for _ in range(height)]
        for i in range(width):
            result[0][i] = matrix[0][i]
        for j in range(height):
            result[j][0] = matrix[j][0]
        

        index = 1
        while index<height and index<width:
            if index<height:
                for i in range(index, height):
                    result[i][index] = self.check_square(i, index, result, matrix)
            if index<width:
                for j in range(index, width):
                    result[index][j] = self.check_square(index, j, result, matrix)
            index += 1
        
        max_squares = 0
        
        for i in range(height):
            for j in range(width):
                max_squares = max(max_squares, int(result[i][j]))
       
        max_squares = int(max_squares) * int(max_squares)
        return max_squares