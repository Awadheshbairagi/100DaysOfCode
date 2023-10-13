class Solution:
    def __init__(self):
        self.mod = 10**9 + 7

    def numOfArrays(self, n, m, k):
        dp = [[[0 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
        sum_arr = [[[0 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(2)]

        for i in range(1, m + 1):
            dp[1][i][1] = 1
            sum_arr[1][i][1] = i

        for sz in range(1, n + 1):
            for maxN in range(1, m + 1):
                for cost in range(1, k + 1):
                    ans = (maxN * dp[sz - 1][maxN][cost]) % self.mod
                    ans = (ans + sum_arr[(sz - 1) & 1][maxN - 1][cost - 1]) % self.mod
                    dp[sz][maxN][cost] = (dp[sz][maxN][cost] + ans) % self.mod
                    sum_arr[sz & 1][maxN][cost] = (sum_arr[sz & 1][maxN - 1][cost] + dp[sz][maxN][cost]) % self.mod

        return sum_arr[n & 1][m][k]
