import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        # Push the first k elements into the min heap
        for num in nums[:k]:
            heapq.heappush(heap, num)
        
        # Continue adding elements to the min heap and pop the smallest element
        for num in nums[k:]:
            heapq.heappushpop(heap, num)
        
        # The kth largest element will be the smallest element in the min heap
        return heap[0]

