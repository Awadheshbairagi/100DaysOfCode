class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_not_under_attack(row, col):
            # Check if there is a queen in the same column
            for prev_row in range(row):
                if board[prev_row][col] == 'Q':
                    return False
            
            # Check if there is a queen in the left upper diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            # Check if there is a queen in the right upper diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if board[i][j] == 'Q':
                    return False
            
            return True
        
        def solve(row):
            if row == n:
                solutions.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if is_not_under_attack(row, col):
                    board[row][col] = 'Q'
                    solve(row + 1)
                    board[row][col] = '.'  # Backtrack
                    
        board = [['.' for _ in range(n)] for _ in range(n)]
        solutions = []
        solve(0)
        return solutions
