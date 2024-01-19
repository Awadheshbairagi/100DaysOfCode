from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]
        for i in range(1, n):
            for j in range(n):
                above = dp[i-1][j]
                if j > 0:
                    above = min(above, dp[i-1][j-1])
                if j < n-1:
                    above = min(above, dp[i-1][j+1])
                dp[i][j] = matrix[i][j] + above
        min_sum = min(dp[n-1])
        return min_sum