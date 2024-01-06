class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)
        def fn(lo, hi): 
            if lo+1 >= hi: return 0 
            mid = lo + hi >> 1
            ans = fn(lo, mid) + fn(mid, hi)
            k = kk = mid 
            for i in range(lo, mid): 
                while k < hi and prefix[k] - prefix[i] < lower: k += 1
                while kk < hi and prefix[kk] - prefix[i] <= upper: kk += 1
                ans += kk - k 
            prefix[lo:hi] = sorted(prefix[lo:hi])
            return ans 
        return fn(0, len(prefix))