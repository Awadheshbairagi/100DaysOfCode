from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Create a sorted copy of the input array
        sorted_arr = sorted(arr)
        # Create a dictionary to store ranks of elements
        rank_dict = {}
        rank = 1
        
        # Assign ranks to elements in the sorted array
        for num in sorted_arr:
            if num not in rank_dict:
                rank_dict[num] = rank
                rank += 1
        
        # Iterate through the original array and replace elements with their ranks
        result = [rank_dict[num] for num in arr]
        return result
