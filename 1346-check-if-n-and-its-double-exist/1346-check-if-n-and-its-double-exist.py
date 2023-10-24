from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Create a set to store seen elements
        seen = set()
        
        # Iterate through the array
        for num in arr:
            # Check if the double or half of the current number exists in the set
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            # Add the current number to the set
            seen.add(num)
        
        # If no such indices are found, return False
        return False
