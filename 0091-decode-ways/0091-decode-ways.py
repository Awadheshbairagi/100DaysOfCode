class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]