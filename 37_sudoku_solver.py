class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def find_next():
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] == ".":
                        return i, j
            return -1, -1
        
        def check_sudoku():
            r, c = find_next()
            if r == -1 and c == -1: return True
            for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if check_valid(r, c, num):
                    board[r][c] = num
                    if check_sudoku():
                        return True
                    board[r][c] = "."
            return False
        
        def check_valid(r, c, num):
            #checks horizontal, vertical, small grid
            box_r  = r - r%3
            box_c = c - c%3
            if check_col(c, num) and check_row(r, num) and check_box(box_r, box_c, num):
                return True
            return False
        
        def check_col(c, num):
            for i in range(len(board)):
                if board[i][c] == num:
                    return False
            return True
            
        def check_row(r, num):
            for j in range(len(board[0])):
                if board[r][j] == num:
                    return False
            return True
        
        def check_box(box_r, box_c, num):
            for i in range(box_r, box_r+3):
                for j in range(box_c, box_c+3):
                    if board[i][j] == num:
                        return False
            return True
    
        check_sudoku()