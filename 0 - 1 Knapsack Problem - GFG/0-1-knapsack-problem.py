class Solution:
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        # Initialize a 2D DP table with zeros
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        # Fill the DP table
        for i in range(1, n + 1):
            for w in range(1, W + 1):
                # If the current item's weight is less than or equal to the knapsack capacity,
                # choose the maximum of including or excluding the current item
                if wt[i - 1] <= w:
                    dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
                else:
                    dp[i][w] = dp[i - 1][w]

        return dp[n][W]  # Return the maximum possible value



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends