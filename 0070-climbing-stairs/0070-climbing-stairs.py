class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize dp array to store number of ways to reach each step
        dp = [0] * (n + 1)
        dp[1] = 1  # There's 1 way to climb 1 step
        dp[2] = 2  # There are 2 ways to climb 2 steps (1+1 or 2)
        
        # Fill the dp array using dynamic programming
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

    