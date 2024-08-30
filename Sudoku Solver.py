class Solution:
    def isvalid(self, board, r, c, val):
        for i in range(9):
            if board[i][c] == val:  
                return False
            if board[r][i] == val: 
                return False
            if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == val:  
                return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':  
                    for k in '123456789': 
                        if self.isvalid(board, i, j, k):
                            board[i][j] = k 
                            if self.solveSudoku(board):  
                                return True
                            else:
                                board[i][j] = '.'  
                    return False 
        return True  
