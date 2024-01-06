class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        
        for gap in range(len(nums)):
            for left in range(len(nums)-gap):
                right = left + gap
                
                res = 0
                for i in range(left+1, right):
                    coins = nums[left] * nums[i] * nums[right]
                    res = max(res, coins + dp[left][i] + dp[i][right])
                dp[left][right] = res
                
        return dp[0][len(nums)-1]