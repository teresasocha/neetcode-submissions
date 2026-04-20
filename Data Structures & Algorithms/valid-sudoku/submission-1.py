class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            temp = [r for r in row if r != "."]
            if len(temp) != len(set(row)) - 1:
                return False
        for j in range(0, 9):
            column = [board[i][j] for i in range(0, 9)]
            temp = [c for c in column if c != "."]
            if len(temp) != len(set(column)) - 1:
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                mini_board = [board[i][j], board[i][j+1], board[i][j+2], board[i + 1][j], board[i + 1][j+1], board[i + 1][j+2], board[i + 2][j], board[i + 2][j+1], board[i + 2][j+2]]
                temp = [m for m in mini_board if m != "."]
                if len(temp) != len(set(mini_board)) - 1:
                    return False
        return True
