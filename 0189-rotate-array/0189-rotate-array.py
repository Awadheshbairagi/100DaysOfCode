class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # In case k is larger than the array length

        # Reverse the entire array
        self.reverse(nums, 0, n - 1)
        
        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        
        # Reverse the remaining elements
        self.reverse(nums, k, n - 1)
    
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
