class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        overlap_x = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_y = max(0, min(ay2, by2) - max(ay1, by1))
        overlap_area = overlap_x * overlap_y

        total_area = area1 + area2 - overlap_area

        return total_area
