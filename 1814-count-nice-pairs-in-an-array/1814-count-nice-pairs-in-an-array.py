class Solution:
    def countNicePairs(self, nums):
        mod = 10**9 + 7
        rev_diffs = {}
        count = 0
        for num in nums:
            diff = num - int(str(num)[::-1]) 
            rev_diffs[diff] = rev_diffs.get(diff, 0) + 1 
        for val in rev_diffs.values():
            count += val * (val - 1) // 2 
        return count % mod