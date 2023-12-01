class Solution:
    
    def f(self, i, k, s, lst, n):
        if s==0:
            if len(lst)==k:
                self.ans.add(lst)
            return
        if i>=n or i>=10:
            return
        
        self.f(i+1, k, s, lst, n)
        if s-i>=0:
            self.f(i+1, k, s-i, lst+(i,), n)
        
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = set()
        if n//k>=9:
            return []
        self.f(1, k, n, tuple(), n)
        return self.ans