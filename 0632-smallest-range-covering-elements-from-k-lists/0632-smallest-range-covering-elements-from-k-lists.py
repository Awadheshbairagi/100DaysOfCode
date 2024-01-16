class Solution:
    def smallestRange(self, arrays):
        heap = []
        start, end, maximum = -inf, inf, -inf
        for arr in arrays:
            heappush(heap, (arr[0], 0, arr))
            maximum = max(maximum, arr[0])
        while heap:
            minimum, i, arr = heappop(heap)
            if maximum - minimum < end - start:
                start, end = minimum, maximum
            if i + 1 == len(arr):
                return [start, end]
            heappush(heap, (arr[i + 1], i + 1, arr))
            maximum = max(maximum, arr[i + 1])