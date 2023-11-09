class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        
        # dp[i] represents the number of unique BSTs that can be formed with i nodes
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        
        # Iterate through all possible root nodes
        for i in range(2, n + 1):
            # Calculate the number of unique BSTs for each root node
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
                
        return dp[n]
