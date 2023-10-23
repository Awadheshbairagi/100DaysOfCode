from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize the candidate and count
        candidate = nums[0]
        count = 1
        
        # Iterate through the rest of the array
        for num in nums[1:]:
            # If count becomes zero, update the candidate
            if count == 0:
                candidate = num
                count = 1
            # If the current number is the same as the candidate, increment count
            elif num == candidate:
                count += 1
            # If the current number is different from the candidate, decrement count
            else:
                count -= 1
        
        return candidate
