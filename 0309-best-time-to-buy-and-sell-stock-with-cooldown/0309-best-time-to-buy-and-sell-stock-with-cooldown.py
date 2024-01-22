class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(0, prices[1] - prices[0])
        dp[1][1] = -min(prices[0], prices[1])
        for k in range(2, len(prices)):
            dp[k][1] = max(dp[k-1][1], dp[k-2][0] - prices[k]) 
            dp[k][0] = max(dp[k-1][0], dp[k-1][1] + prices[k]) 
        return dp[-1][0]
