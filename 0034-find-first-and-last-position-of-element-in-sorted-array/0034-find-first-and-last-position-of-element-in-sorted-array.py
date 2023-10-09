class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper function to find the leftmost or rightmost occurrence of the target
        def binarySearch(nums, target, leftmost):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] > target or (leftmost and nums[mid] == target):
                    right = mid
                else:
                    left = mid + 1
            return left
        
        # Find the leftmost and rightmost positions of the target element
        left_idx = binarySearch(nums, target, True)
        right_idx = binarySearch(nums, target, False) - 1
        
        # Check if the target element is found, return the range; otherwise, return [-1, -1]
        if left_idx <= right_idx and nums[left_idx] == target:
            return [left_idx, right_idx]
        else:
            return [-1, -1]
