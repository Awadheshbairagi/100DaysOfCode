class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]  # Initialize max_sum with the first element of the array
        current_sum = nums[0]  # Initialize current_sum with the first element of the array
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Compare the current number with the sum of current number and current_sum
            # If the current number is greater, start a new subarray, else continue the subarray
            current_sum = max(num, current_sum + num)
            # Update max_sum if current_sum is greater than max_sum
            max_sum = max(max_sum, current_sum)
        
        return max_sum
