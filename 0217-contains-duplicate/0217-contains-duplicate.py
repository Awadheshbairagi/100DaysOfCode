from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for num in nums:
            # If the current element is already in the set, return True
            if num in seen:
                return True
            # Otherwise, add the element to the set
            seen.add(num)
        
        # If the loop completes without returning, no duplicates were found
        return False

