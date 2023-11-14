class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        
        while left <= right:
            if s[left] != s[right]:
                # To make the string lexicographically smallest,
                # we'll replace the larger character with the smaller one
                s[right] = min(s[left], s[right])
                s[left] = s[right]
                
            left += 1
            right -= 1
        
        return ''.join(s)
