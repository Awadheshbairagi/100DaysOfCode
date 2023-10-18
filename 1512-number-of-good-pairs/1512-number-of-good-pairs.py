from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count_dict = {}  # Dictionary to store counts of each number
        
        # Count occurrences of each number
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        
        good_pairs = 0  # Variable to store the count of good pairs
        
        # Calculate good pairs for each number that occurs more than once
        for count in count_dict.values():
            if count > 1:
                good_pairs += count * (count - 1) // 2
        
        return good_pairs
