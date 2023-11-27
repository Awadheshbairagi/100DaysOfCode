class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache={}
        def dp(i,k):
            if (i,k) in cache:
                return cache[(i,k)]
            if i>len(coins)-1:
                cache[(i,k)]=float('inf')
                return float('inf')
            if k<0:
                cache[(i,k)]=float('inf')
                return float('inf')
            if k==0:
                cache[(i,k)]=0
                return 0
            take=1+dp(i,k-coins[i])
            ntake=dp(i+1,k)
            cache[(i,k)]=min(take,ntake)
            return min(take,ntake)
        return -1 if dp(0,amount)==float('inf') else  dp(0,amount)