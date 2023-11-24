class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            max_sum = float('-inf')
            curr_sum = 0
            for num in nums:
                curr_sum = max(num, curr_sum + num)
                max_sum = max(max_sum, curr_sum)
            return max_sum

        total_sum = sum(nums)
        max_sum = kadane(nums)
        min_sum = kadane([-num for num in nums])
        if min_sum == -total_sum:
            return max_sum
        return max(max_sum, total_sum + min_sum)
