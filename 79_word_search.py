class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, i, j, word_idx):
            # print(board)
            if word_idx > len(word) or i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j] != word[word_idx]:
                return False
            
            if word_idx == len(word)-1:
                return True
            tmp = board[i][j]
            board[i][j] = 0
            
            result = dfs(board, i-1, j, word_idx+1) or dfs(board, i+1, j, word_idx+1) or dfs(board, i, j-1, word_idx+1) or dfs(board, i, j+1, word_idx+1)
            
            board[i][j] = tmp
            
            return result
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(board, i, j, 0):
                        return True
        
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def dfs(board, i, j, word_idx):
#             if word_idx == len(word)-1:
#                 return True
#             board[i][j] == 0
#             print(board)
#             if i-1>=0 and board[i-1][j] == word[word_idx+1]:
#                 #up
#                 dfs(board, i-1, j, word_idx+1)
#             elif i+1<len(board) and board[i+1][j] == word[word_idx+1]:
#                 #down
#                 dfs(board, i+1, j, word_idx+1)
#             elif j+1<len(board[0]) and board[i][j+1] == word[word_idx+1]:
#                 #right
#                 dfs(board, i, j+1, word_idx+1)
#             elif j-1>=0 and board[i][j-1] == word[word_idx+1]:
#                 #left
#                 dfs(board, i, j-1, word_idx+1)
#             return False
        
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == word[0]:
#                     if dfs(copy.deepcopy(board), i, j, 0):
#                         return True
        
#         return False
        
