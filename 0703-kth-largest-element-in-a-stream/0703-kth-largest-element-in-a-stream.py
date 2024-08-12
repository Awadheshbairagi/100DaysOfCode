class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums
        self.stream.sort()

    def add(self, val: int) -> int:
        index = self.getIndex(val)
        # Add val to correct position
        self.stream.insert(index, val)
        return self.stream[-self.k]

    def getIndex(self, val: int) -> int:
        left, right = 0, len(self.stream) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_element = self.stream[mid]
            if mid_element == val:
                return mid
            # Go to left half
            elif mid_element > val:
                right = mid - 1
            # Go to right half
            else:
                left = mid + 1
        return left