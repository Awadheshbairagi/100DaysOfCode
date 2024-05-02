class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        
        for i in nums:
            for j in nums:
                # If there exists a number j such that i is the negative of j
                if i == -j:
                    # Update the answer to the maximum of current ans and absolute value of i
                    ans = max(ans, abs(i))

        return ans