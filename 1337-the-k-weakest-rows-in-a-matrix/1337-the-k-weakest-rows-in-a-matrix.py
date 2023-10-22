from typing import List, Tuple

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Step 1: Calculate the strength of each row and store it in a list along with the row index
        row_strengths = []
        for i, row in enumerate(mat):
            strength = sum(row)
            row_strengths.append((i, strength))
        
        # Step 2: Sort the list of rows based on their strengths and original indices
        row_strengths.sort(key=lambda x: (x[1], x[0]))
        
        # Return the first k indices from the sorted list
        return [row[0] for row in row_strengths[:k]]
