class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        firstRowZero, firstColZero = False, False
        
        # Check if the first row contains zero
        for i in range(n):
            if matrix[0][i] == 0:
                firstRowZero = True
                break
        
        # Check if the first column contains zero
        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True
                break
        
        # Mark the first row and first column based on other cells
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set zeros based on the marks in the first row and first column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Set the first row to zeros if necessary
        if firstRowZero:
            matrix[0] = [0] * n
        
        # Set the first column to zeros if necessary
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0
