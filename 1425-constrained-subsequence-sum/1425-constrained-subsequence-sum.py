from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums, k):
        n = len(nums)
        dp = [0] * n  # dp[i] represents the maximum sum of non-empty subsequence ending at index i
        
        # Using deque to efficiently find the maximum element in the sliding window of size k
        dq = deque()
        
        for i in range(n):
            # Remove elements outside the window of size k
            if dq and dq[0] < i - k:
                dq.popleft()
            
            # Calculate dp[i] by taking the maximum of previous dp values within the window
            dp[i] = max(nums[i], nums[i] + (dp[dq[0]] if dq else 0))
            
            # Remove elements from the end of the deque if they are smaller than dp[i]
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)
        
        # Return the maximum value in the dp array
        return max(dp)
