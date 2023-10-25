from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first):
            # If all integers are used up, add the permutation to the result
            if first == n:
                output.append(nums[:])
                return
            for i in range(first, n):
                # Place the current integer at the first position
                nums[first], nums[i] = nums[i], nums[first]
                # Recursively generate permutations for the remaining integers
                backtrack(first + 1)
                # Undo the swap for backtracking
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack(0)
        return output
