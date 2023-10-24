from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Sort the array in ascending order
        arr.sort()
        # Initialize variables to store the minimum difference and pairs
        min_diff = float('inf')
        pairs = []
        
        # Find the minimum absolute difference
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            # If the current difference is smaller, update min_diff and reset pairs
            if diff < min_diff:
                min_diff = diff
                pairs = [[arr[i - 1], arr[i]]]
            # If the current difference equals min_diff, add the pair to pairs list
            elif diff == min_diff:
                pairs.append([arr[i - 1], arr[i]])
        
        return pairs
