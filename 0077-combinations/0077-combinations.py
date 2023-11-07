class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, k, current_combination, combinations):
            if k == 0:
                combinations.append(current_combination[:])
                return
            
            for num in range(start, n + 1):
                current_combination.append(num)
                backtrack(num + 1, k - 1, current_combination, combinations)
                current_combination.pop()
        
        combinations = []
        backtrack(1, k, [], combinations)
        return combinations
