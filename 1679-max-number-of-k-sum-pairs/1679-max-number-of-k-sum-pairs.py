class Solution:
    def maxOperations(self, nums, k):
        nums.sort()
        i, j = 0, len(nums) - 1
        cnt = 0
        
        while i < j:
            summ = nums[i] + nums[j]
            if summ == k:
                cnt += 1
                i += 1
                j -= 1
            elif summ < k:
                i += 1
            else:
                j -= 1
        
        return cnt
