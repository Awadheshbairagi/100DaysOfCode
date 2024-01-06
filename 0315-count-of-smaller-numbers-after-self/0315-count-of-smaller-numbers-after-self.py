from array import array

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = array('i', bytes(len(nums) << 2))
        
        nums2 = array('h')

        for i in range(l-1,-1,-1):
            n = nums.pop()
            lpos = bisect_left(nums2, n)
            ans[i] = lpos
            nums2.insert(lpos, n)

        return ans