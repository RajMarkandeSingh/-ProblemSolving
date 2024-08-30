class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row=set()
            col=set()
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
                if board[j][i]!='.':
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
        for i in range(0,9,3):
            for j in range(0,9,3):
                subboard=set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l]!='.':
                            if board[i+k][j+l] in subboard:
                                return False
                            subboard.add(board[i+k][j+l])
        return True
        
