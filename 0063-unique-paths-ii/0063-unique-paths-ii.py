class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Create a DP table to store the number of unique paths at each position
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # Initialize the top-left cell, if it is not an obstacle
        dp[0][0] = 1 - obstacleGrid[0][0]
        
        # Fill the first column, considering obstacles
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] * (1 - obstacleGrid[i][0])
        
        # Fill the first row, considering obstacles
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] * (1 - obstacleGrid[0][j])
        
        # Fill the DP table considering obstacles and available paths
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0  # If there is an obstacle, no path is possible
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # Paths from above + Paths from left
        
        return dp[m - 1][n - 1]
