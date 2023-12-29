from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]
        dp[0][0] = 0
        for day in range(1, d + 1):
            for i in range(1, n + 1):
                maxDifficulty = 0
                for j in range(i, 0, -1):
                    maxDifficulty = max(maxDifficulty, jobDifficulty[j - 1])
                    dp[day][i] = min(dp[day][i], dp[day - 1][j - 1] + maxDifficulty)
        return dp[d][n]