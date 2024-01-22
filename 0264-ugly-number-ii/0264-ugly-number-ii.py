class Solution:
    def nthUglyNumber(self, n: int) -> int:
        min_heap = [1] 
        seen = set([1]) 
        prime_no = (2,3,5)
        for i in range(n-1):  
            ugly_no = heapq.heappop(min_heap)
            for ele in prime_no:
                no = ugly_no * ele
                if no not in seen:
                    seen.add(no)
                    heapq.heappush(min_heap, no)
        return min_heap[0]