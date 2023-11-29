class Solution(object):
    def pivotIndex(self, nums):
        # Total sum of all integers in list
        totSum = sum(nums)
        # sum of integers left of pivot
        leftSum = 0
        for i in range(len(nums)):
            # Check if sum of all nums left and right of pivot is even, and if they are equal.
            if (totSum - nums[i]) % 2 == 0 and leftSum == (totSum - nums[i]) / 2:
                return i
            # add to left side if pivot index not found
            leftSum += nums[i]
        return -1