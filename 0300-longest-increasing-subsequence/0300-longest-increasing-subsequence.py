from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [nums[0]]

        for i in range(1, n):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
            else:
                ind = self.lower_bound(temp, nums[i])
                temp[ind] = nums[i]

        return len(temp)
    
    def lower_bound(self, arr, target):
        left, right = 0, len(arr)
        
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left
