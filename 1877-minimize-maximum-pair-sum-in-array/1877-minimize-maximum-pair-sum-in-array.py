class Solution:
    def minPairSum(self, nums):
        nums.sort()
        
        max_sum = 0
        for i in range(len(nums) // 2):
            max_sum = max(max_sum, nums[i] + nums[len(nums) - 1 - i])
        
        return max_sum
