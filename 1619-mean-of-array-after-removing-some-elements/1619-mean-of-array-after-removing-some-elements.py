from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        # Sort the array
        arr.sort()
        # Calculate the index for removing 5% of elements from both ends
        n = len(arr)
        remove_count = n // 20
        # Remove the smallest 5% and largest 5% of elements
        trimmed_arr = arr[remove_count : n - remove_count]
        # Calculate the mean of remaining elements
        mean = sum(trimmed_arr) / len(trimmed_arr)
        return mean