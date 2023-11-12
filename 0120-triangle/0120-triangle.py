class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        # Start from the second-to-last row
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update the current value by adding the minimum of the adjacent values in the row below
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

        # The top element contains the minimum path sum
        return triangle[0][0]

