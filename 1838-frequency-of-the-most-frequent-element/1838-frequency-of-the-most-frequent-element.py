class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()
        freq = 0
        total = 0
        left = 0
        
        for right in range(len(nums)):
            total += nums[right]
            while (right - left + 1) * nums[right] - total > k:
                total -= nums[left]
                left += 1
            freq = max(freq, right - left + 1)
        
        return freq
