class Solution:
    def numberOfPaths(self, M, N):
        MOD = 10**9 + 7
        
        # Calculate nCr using factorials
        def nCr(n, r):
            numerator = 1
            denominator = 1
            for i in range(r):
                numerator = (numerator * (n - i)) % MOD
                denominator = (denominator * (i + 1)) % MOD
            return (numerator * pow(denominator, MOD - 2, MOD)) % MOD

        # Calculate total moves and down moves
        total_moves = M + N - 2
        down_moves = M - 1
        
        # Calculate and return the number of unique paths
        return nCr(total_moves, down_moves)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        M, N = map(int, input().split())
        ans = ob.numberOfPaths(M, N)
        print(ans)




# } Driver Code Endsclass Solution:
    def numberOfPaths(self, M, N):
        MOD = 10**9 + 7
        
        # Calculate nCr using factorials
        def nCr(n, r):
            numerator = 1
            denominator = 1
            for i in range(r):
                numerator = (numerator * (n - i)) % MOD
                denominator = (denominator * (i + 1)) % MOD
            return (numerator * pow(denominator, MOD - 2, MOD)) % MOD

        # Calculate total moves and down moves
        total_moves = M + N - 2
        down_moves = M - 1
        
        # Calculate and return the number of unique paths
        return nCr(total_moves, down_moves)
