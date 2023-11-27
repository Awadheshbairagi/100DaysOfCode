from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        memo = [[0 for i in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)]
        area = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    memo[i+1][j+1] = min(memo[i][j+1], memo[i+1][j], memo[i][j]) + 1
                    area = max(area, memo[i+1][j+1])

        return area*area
