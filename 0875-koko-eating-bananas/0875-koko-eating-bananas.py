class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check_can_eat(k):
            actual_h = 0
            for pile in piles:
                actual_h += (pile+k-1)//k
            return actual_h <= h
        l,r = 0,max(piles)
        while r-l>1:
            m=(l+r)//2
            if check_can_eat(m):
                r = m
            else:
                l = m
        return r