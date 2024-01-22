class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s, s2, n = 0, 0, len(nums)
        for num in nums:
            s += num
            s2 += num*num
        diff = n*(n+1)//2 - s
        diff2 = n*(n+1)*(2*n+1)//6 - s2
        missing = (diff2//diff + diff)//2
        return [missing-diff, missing]