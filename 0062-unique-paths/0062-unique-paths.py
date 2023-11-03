class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D dp array to store the number of unique paths
        dp = [[1] * n for _ in range(m)]
        
        # Fill the dp array using dynamic programming
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        # The bottom-right cell contains the number of unique paths
        return dp[m - 1][n - 1]
