class Solution:
    def construct2DArray(
        self, original: list[int], m: int, n: int
    ) -> list[list[int]]:
        # Check if it is possible to form an m x n 2D array
        if m * n != len(original):
            # If not, return an empty 2D array
            return []

        # Initialize the result 2D array with m rows and n columns
        result_array = [[0] * n for _ in range(m)]

        # Initialize an index to track the current position in the original array
        index = 0

        for i in range(m):
            for j in range(n):
                # Assign the current element from the original array to the 2D array
                result_array[i][j] = original[index]
                # Move to the next element in the original array
                index += 1

        return result_array