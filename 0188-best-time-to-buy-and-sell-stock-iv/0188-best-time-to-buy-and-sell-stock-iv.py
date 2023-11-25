class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if k >= n // 2:
            # If k is large enough, solve with unlimited transactions approach
            return self.unlimitedTransactions(prices)
        
        # Initialize a 3D DP array
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        
        for i in range(n):
            for j in range(k, 0, -1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        
        return dp[n - 1][k][0]
    
    def unlimitedTransactions(self, prices):
        n = len(prices)
        if n <= 1:
            return 0
        
        max_profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit
