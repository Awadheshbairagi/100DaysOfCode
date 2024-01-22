class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        l=[1]
        a=[0 for _ in range(len(primes))]
        for i in range(n-1):
            t=[primes[i]*l[a[i]] for i in range(len(primes))]
            m=min(t)
            for j in range(len(t)):
                if t[j]==m:
                    a[j]+=1
            l.append(m) 
        return l[-1]   