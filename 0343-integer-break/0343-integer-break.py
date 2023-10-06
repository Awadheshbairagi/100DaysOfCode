class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] stores the maximum product for number i
        dp = [0] * (n + 1)
        
        # Base case
        dp[2] = 1
        
        # Compute maximum product for numbers from 3 to n
        for i in range(3, n + 1):
            # For each number i, iterate from 1 to i - 1 to find the best split
            for j in range(1, i):
                # Either break i into j and i - j, or use the existing dp[i]
                dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))
        
        return dp[n]
