class Solution:
    def scheduleCourse(self, cs: List[List[int]]) -> int:
        import heapq 

        cs = sorted(cs, key = lambda x: x[1])
        heap = []
        curTime = 0

        for d, l in cs:
            if curTime + d <= l:
                heappush(heap, -d)
                curTime += d
                
            elif heap and -heap[0] > d:
                curTime += d + heappop(heap)
                heappush(heap, -d)

        return len(heap)