class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # dp[i][j] represents the number of distinct subsequences of s[:i] that equals t[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Empty string t can be formed from any non-empty string s by deleting all characters
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the characters are equal, we have two choices:
                # 1. Include both characters in the subsequence, i.e., dp[i-1][j-1]
                # 2. Exclude the last character of s, i.e., dp[i-1][j]
                dp[i][j] = dp[i - 1][j] + (dp[i - 1][j - 1] if s[i - 1] == t[j - 1] else 0)

        return dp[m][n]
