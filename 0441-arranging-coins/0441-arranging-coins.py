class Solution:
    def arrangeCoins(self, n: int) -> int:
        f = 1
        l = n
        while f<=l:
            mid = (f+l)//2
            temp = (mid*(mid+1))//2
            if temp == n:
                return mid
            elif temp > n:
                l = mid-1
            else:
                f = mid+1
        return l