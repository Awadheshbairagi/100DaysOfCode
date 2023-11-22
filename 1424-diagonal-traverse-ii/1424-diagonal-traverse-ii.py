from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums):
        groups = defaultdict(list)
        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                diagonal = row + col
                groups[diagonal].append(nums[row][col])
        ans = []
        for _, values in sorted(groups.items()):
            ans.extend(values)
        return ans