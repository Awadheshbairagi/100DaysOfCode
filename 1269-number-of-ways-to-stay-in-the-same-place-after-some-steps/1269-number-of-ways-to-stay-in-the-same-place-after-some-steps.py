class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        maxColumn = min(arrLen - 1, steps // 2 + 1)
        dp = [[0] * (maxColumn + 1) for _ in range(steps + 1)]
        dp[0][0] = 1
        
        for i in range(1, steps + 1):
            for j in range(0, maxColumn + 1):
                dp[i][j] = dp[i - 1][j]
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD
                if j < maxColumn:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % MOD
        
        return dp[steps][0]

