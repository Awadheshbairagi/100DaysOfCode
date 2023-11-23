class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort balloons by their ending points
        points.sort(key=lambda x: x[1])
        
        arrows = 1  # Initialize the arrow count
        end = points[0][1]
        
        for start, x_end in points[1:]:
            # If the current balloon's start point is beyond the end point,
            # a new arrow is required, update the arrow count and the end point
            if start > end:
                arrows += 1
                end = x_end
        
        return arrows
