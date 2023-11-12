class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # Initialize a table to store whether a substring is a palindrome
        is_palindrome = [[False] * n for _ in range(n)]
        
        # Helper function to check if a substring is a palindrome
        def precompute_palindromes():
            for length in range(1, n + 1):
                for i in range(n - length + 1):
                    j = i + length - 1
                    if length == 1:
                        is_palindrome[i][j] = True
                    else:
                        is_palindrome[i][j] = (s[i] == s[j]) and (length == 2 or is_palindrome[i + 1][j - 1])
        
        precompute_palindromes()
        
        # Initialize a table to store minimum cuts
        cuts = [float('inf')] * n
        
        # Fill the cuts table
        for j in range(n):
            if is_palindrome[0][j]:
                cuts[j] = 0
            else:
                for i in range(j):
                    if is_palindrome[i + 1][j]:
                        cuts[j] = min(cuts[j], cuts[i] + 1)
        
        return cuts[-1]
