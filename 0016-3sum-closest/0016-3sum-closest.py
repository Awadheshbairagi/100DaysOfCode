class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the input array
        
        closest_sum = float('inf')  # Initialize closest_sum to positive infinity
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1  # Initialize two pointers
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]  # Calculate the current sum
                
                # Check if the current sum is closer to the target
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                
                # Move pointers based on the comparison with the target
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return closest_sum  # If the sum is equal to the target, return the sum as it can't get closer
                
        return closest_sum
