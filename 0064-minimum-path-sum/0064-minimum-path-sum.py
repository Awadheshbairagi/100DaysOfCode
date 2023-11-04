class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Create a DP table to store the minimum path sum at each position
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # Initialize the top-left cell
        dp[0][0] = grid[0][0]
        
        # Fill the first column
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        # Fill the first row
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        
        # Fill the DP table considering minimum path sum
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[m - 1][n - 1]
