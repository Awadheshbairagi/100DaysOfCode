from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        flat_board = [0]
        direction = 1
        
        # Flatten the 2D board into a 1D list
        for i in range(n - 1, -1, -1):
            if direction == 1:
                flat_board.extend(board[i])
            else:
                flat_board.extend(reversed(board[i]))
            direction *= -1
        
        queue = deque([(1, 0)])  # Start from cell 1 with 0 moves
        visited = set()
        
        while queue:
            cell, moves = queue.popleft()
            
            if cell == n * n:
                return moves
            
            for i in range(1, 7):
                next_cell = cell + i
                if next_cell <= n * n:
                    if flat_board[next_cell] != -1:
                        next_cell = flat_board[next_cell]
                    if next_cell not in visited:
                        visited.add(next_cell)
                        queue.append((next_cell, moves + 1))
        
        return -1  # Unable to reach n*n
