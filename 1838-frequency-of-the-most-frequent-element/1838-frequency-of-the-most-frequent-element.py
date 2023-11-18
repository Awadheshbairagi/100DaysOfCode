class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()
        freq = 0
        total = 0
        left = 0
        
        for right, num in enumerate(nums):
            total += num
            while (right - left + 1) * nums[right] - total > k:
                total -= nums[left]
                left += 1
            freq = max(freq, right - left + 1)
        
        return freq
