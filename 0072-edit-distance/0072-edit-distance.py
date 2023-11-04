class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Initialize a 2D DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the first row and first column
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        # Fill the DP table considering three operations: insert, delete, replace
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the characters match, no operation is needed
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Minimum of insert, delete, and replace operations
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        
        return dp[m][n]
