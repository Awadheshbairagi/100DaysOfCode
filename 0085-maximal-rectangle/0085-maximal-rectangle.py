class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        matrix = [[int(col) for col in row] for row in matrix]
        rows, cols = len(matrix), len(matrix[0])
        
        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)
            for i, h in enumerate(heights):
                while stack and h < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
            return max_area
        
        max_area = 0
        heights = [0] * cols
        
        for row in matrix:
            for i in range(cols):
                if row[i] == 1:
                    heights[i] += 1
                else:
                    heights[i] = 0
            max_area = max(max_area, largestRectangleArea(heights))
        
        return max_area
