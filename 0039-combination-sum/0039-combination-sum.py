from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path, result):
            if target == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                backtrack(i, target - candidates[i], path + [candidates[i]], result)

        candidates.sort()  # Sort the candidates for early stopping in the backtracking
        result = []
        backtrack(0, target, [], result)
        return result
