class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[1] * 5 for _ in range(n)]
        transitions = {
            0: [1],  
            1: [0, 2],  
            2: [0, 1, 3, 4],  
            3: [2, 4],  
            4: [0]  
        }       
        for i in range(1, n):
            for j in range(5):
                dp[i][j] = sum(dp[i - 1][k] for k in transitions[j]) % MOD     
        return sum(dp[n - 1]) % MOD
