from collections import defaultdict
class Solution:
    def checkRecord(self, n: int) -> int:
        
        dp=[[[0 for i in range(3)]for j in range(2)]for k in range(n+1)]
        def func(n,a,l):
            if n==0:
                if a<2 and l<=2:
                    return 1
            if a>=2 or l>2:
                return 0
            elif dp[n][a][l]:
                return dp[n][a][l]
            ret=(func(n-1,a+1,0)+func(n-1,a,0)+func(n-1,a,l+1))%1000000007
            dp[n][a][l]=ret
            return ret
        y=func(n,0,0)
        return y%1000000007
