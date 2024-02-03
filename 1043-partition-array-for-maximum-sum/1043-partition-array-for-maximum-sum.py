class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            currMax = 0
            end = min(n,i+k)
            for j in range(i,end):
                currMax = max(currMax,arr[j])
                dp[i] = max(dp[i],dp[j+1]+currMax*(j-i+1))
        return dp[0]