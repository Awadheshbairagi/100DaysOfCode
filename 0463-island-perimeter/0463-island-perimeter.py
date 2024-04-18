class Solution:
    def islandPerimeter(self, g: List[List[int]]) -> int:
        return sum(sum(map(ne,(0,*r),(*r,0))) for r in g+[*zip(*g)])