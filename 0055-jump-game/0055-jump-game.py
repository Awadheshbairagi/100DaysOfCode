class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0  # Initialize the maximum index that can be reached
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current index is beyond the maximum reachable index, return False
            if i > max_reachable:
                return False
            
            # Update the maximum reachable index if the current index plus jump length is greater
            max_reachable = max(max_reachable, i + nums[i])
            
            # If the last index can be reached, return True
            if max_reachable >= len(nums) - 1:
                return True
        
        return False
