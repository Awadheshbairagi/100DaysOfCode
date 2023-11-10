from collections import defaultdict

class Solution:
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)

        max_points = 2

        for i in range(len(points)):
            slopes_count = defaultdict(int)
            duplicate_points = 0
            current_max = 1

            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2 and y1 == y2:
                    duplicate_points += 1
                else:
                    slope = float('inf') if x1 == x2 else (y2 - y1) / (x2 - x1)
                    slopes_count[slope] += 1
                    current_max = max(current_max, slopes_count[slope])

            max_points = max(max_points, current_max + duplicate_points + 1)

        return max_points

