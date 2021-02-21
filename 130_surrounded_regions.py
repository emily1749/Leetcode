# class Solution(object):
#     def solve(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: None Do not return anything, modify board in-place instead.
#         """
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
            
        def bfs(board, row, col):
            if board[row][col] != 'O':
                return
            
            board[row][col] = 'Z'
            
            if row+1<len(board): bfs(board, row+1, col)
            if row-1>=0: bfs(board, row-1, col)
            if col+1<len(board[0]): bfs(board, row, col+1)
            if col-1>=0: bfs(board, row, col-1)
                
                
                
        height = len(board)
        width = len(board[0])
        
        #check top row, bottom row
        for i in range(width):
            if board[0][i] == 'O':
                bfs(board, 0, i)
            if board[height-1][i]== 'O':
                bfs(board, height-1, i)
        #check left and right columns
        for i in range(height):
            if board[i][0] == 'O':
                bfs(board, i, 0)
            if board[i][width-1] == 'O':
                bfs(board, i, width-1)
        for row in range(height):
            for col in range(width):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == 'Z':
                    board[row][col] = 'O'
        return board
            