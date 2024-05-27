from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_not_under_attack(row, col):
            # Check if there is a queen in the same column
            for prev_row in range(row):
                if board[prev_row][col] == 'Q':
                    return False
            # No queens found in the same column, so continue checking

            # Check if there is a queen in the left upper diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            # No queens found in the left upper diagonal, so continue checking

            # Check if there is a queen in the right upper diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if board[i][j] == 'Q':
                    return False
            # No queens found in the right upper diagonal, so continue

            return True
            # Position is safe for placing a queen

        def solve(row):
            if row == n:
                # If all rows are processed, a solution is found
                solutions.append(["".join(row) for row in board])
                return

            for col in range(n):
                if is_not_under_attack(row, col):
                    # Place the queen at (row, col)
                    board[row][col] = 'Q'
                    # Recur to place the queen in the next row
                    solve(row + 1)
                    # Backtrack: remove the queen from (row, col)
                    board[row][col] = '.'

        # Initialize an empty board
        board = [['.' for _ in range(n)] for _ in range(n)]
        # Initialize the solutions list
        solutions = []
        # Start solving from the first row
        solve(0)
        # Return the list of solutions
        return solutions
