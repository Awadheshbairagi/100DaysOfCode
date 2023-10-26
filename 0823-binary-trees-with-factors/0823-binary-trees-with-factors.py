class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        
        for num in arr:
            dp[num] = 1
            for i in range(len(arr)):
                if arr[i] >= num:
                    break
                if num % arr[i] == 0 and num // arr[i] in dp:
                    dp[num] += dp[arr[i]] * dp[num // arr[i]]
                    dp[num] %= MOD
        
        return sum(dp.values()) % MOD
