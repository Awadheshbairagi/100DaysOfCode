class Solution:
    def palindromicPartition(self, string):
        n = len(string)
        # Initialize a DP table to store palindrome information
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        # Every individual character is a palindrome
        for i in range(n):
            dp[i][i] = True
        
        # Fill the DP table for palindrome substrings
        for cl in range(2, n+1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if string[i] == string[j] and (cl == 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
        
        # Use the DP table to find minimum partitions
        cuts = [0] * n
        for j in range(n):
            min_cuts = float('inf')
            for i in range(j + 1):
                if dp[i][j]:
                    min_cuts = min(min_cuts, cuts[i - 1] + 1 if i > 0 else 0)
            cuts[j] = min_cuts
        
        return cuts[n - 1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends