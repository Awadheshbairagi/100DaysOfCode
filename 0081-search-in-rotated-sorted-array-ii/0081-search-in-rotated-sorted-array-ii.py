class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # If mid element is the target
            if nums[mid] == target:
                return True
            
            # Skip duplicates
            while left < mid and nums[left] == nums[mid]:
                left += 1
                
            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # If the target is within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # If the target is within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
