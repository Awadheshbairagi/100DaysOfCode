class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize a list to store the number of ways to reach each step
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1
        dp[1] = 1
        
        # Fill the DP table considering the two options: climb 1 step or climb 2 steps
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
