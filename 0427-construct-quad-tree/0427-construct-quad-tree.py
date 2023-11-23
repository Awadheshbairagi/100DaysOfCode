class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        n = len(grid)
        if n == 0:
            return None
        
        def isLeaf(grid):
            for row in grid:
                for cell in row:
                    if cell != grid[0][0]:
                        return False
            return True
        
        def helper(x, y, size):
            if size == 1:
                return Node(grid[x][y] == 1, True, None, None, None, None)
            
            half = size // 2
            topLeft = helper(x, y, half)
            topRight = helper(x, y + half, half)
            bottomLeft = helper(x + half, y, half)
            bottomRight = helper(x + half, y + half, half)
            
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and \
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return Node(topLeft.val, True, None, None, None, None)
            
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return helper(0, 0, n)
