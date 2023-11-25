class Solution:
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)
        prefix_sum = [0] * n
        suffix_sum = [0] * n
        
        # Calculating prefix sum and suffix sum arrays
        prefix_sum[0] = nums[0]
        suffix_sum[n - 1] = nums[n - 1]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
            suffix_sum[n - i - 1] = suffix_sum[n - i] + nums[n - i - 1]
        
        result = []
        for i in range(n):
            left_sum = nums[i] * i - prefix_sum[i]  # Calculate left side sum
            right_sum = suffix_sum[i] - nums[i] * (n - i - 1)  # Calculate right side sum
            result.append(left_sum + right_sum)
        
        return result
