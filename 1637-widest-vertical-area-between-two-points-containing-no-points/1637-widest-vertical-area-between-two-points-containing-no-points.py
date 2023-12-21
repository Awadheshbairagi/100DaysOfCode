class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=itemgetter(0))
        best=0
        for i in range(len(points)-1):
            p1, p2 = points[i][0], points[i+1][0]
            diff=p2-p1
            if diff>best:
                best=diff
        return best