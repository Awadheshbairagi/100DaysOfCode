class Solution:
    def longestOnes(self, nums, k):
        left = 0
        max_ones = 0
        zero_count = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            # If the number of zeros exceeds k, move the left pointer.
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Update the maximum count of ones.
            max_ones = max(max_ones, right - left + 1)
        
        return max_ones
