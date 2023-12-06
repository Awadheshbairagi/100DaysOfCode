class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors=[1]
        for i in range(2,n+1):
            if n%i==0:
                factors.append(i)
        return -1 if k>len(factors) else factors[k-1]