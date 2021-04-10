class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.board = [[False for _ in range(n)] for _ in range(n)]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1: move = "X"
        elif player == 2: move = "O"
        
        self.board[row][col] = move
        # print(self.board)
        if self.check_win(row, col, move):
            return player
        return 0
        
    def check_win(self, row, col, move):
        if self.check_diag(move) or self.check_row(row, move) or self.check_col(col, move):
            return True
        return False
        
    def check_diag(self, move):
        count_left = 0
        count_right = 0
        for i in range(self.n):
            if self.board[i][i] == move: count_left += 1
            if self.board[i][self.n-i-1] == move: count_right += 1
                
        return count_left == self.n or count_right == self.n
    
        # for i in range(self.n):
        #     if not self.board[i][i] == move: return False
        # return True
    
    def check_row(self, row, move):
        for i in range(self.n):
            if not self.board[row][i] == move: return False
        return True
    
    def check_col(self, col, move):
        for i in range(self.n):
            if not self.board[i][col] == move: return False
        return True
    
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)