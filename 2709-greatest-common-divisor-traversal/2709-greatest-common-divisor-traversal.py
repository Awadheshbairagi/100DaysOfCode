class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n, max_val = len(nums), max(nums)
        sieve, uf = PrimeSieve(max_val), UnionFind(n)

        # Store index of some multiple for each prime
        multiple_idx = {}

        for i, num in enumerate(nums):
            for prime_div in sieve.prime_divs[num]:
                # Add new representative index for this prime if needed
                multiple_idx[prime_div] = multiple_idx.get(prime_div, i)
                # Connect this index, and representative for this prime
                uf.union(i, multiple_idx[prime_div])
        
        return uf.rank[uf.find(0)] == n


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, i):
        if self.par[i] == i:
            return i
        self.par[i] = self.find(self.par[i])
        return self.par[i]
    
    def union(self, i, j):
        par_i, par_j = self.find(i), self.find(j)
        if par_i == par_j:
            return
        if self.rank[par_i] > self.rank[par_j]:
            par_i, par_j = par_j, par_i
        self.par[par_i] = par_j
        self.rank[par_j] += self.rank[par_i]

class PrimeSieve:
    def __init__(self, n):
        self.prime_divs = [list() for i in range(n+1)]
        for p in range(2, n+1):
            if len(self.prime_divs[p]) == 0:
                for i in range(p, n+1, p):
                    self.prime_divs[i].append(p)