class Solution:
    def containsNearbyDuplicate(self, nums, k):
        num_indices = {}  # Dictionary to store indices of elements
        
        for i, num in enumerate(nums):
            if num in num_indices and abs(i - num_indices[num]) <= k:
                return True
            num_indices[num] = i
        
        return False
