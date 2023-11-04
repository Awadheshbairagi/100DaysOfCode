MOD = 10**9 + 7

class Solution:
    def nCr(self, n, r):
        # Compute factorials and their inverses using dynamic programming
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = (fact[i - 1] * i) % MOD
            inv_fact[i] = pow(fact[i], MOD - 2, MOD)
        
        # Calculate nCr modulo 10^9 + 7 using the formula
        if r > n:
            return 0
        return (fact[n] * inv_fact[r] * inv_fact[n - r]) % MOD


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends