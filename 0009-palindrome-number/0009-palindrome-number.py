class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=str(x)
        if(n[::-1]==n):
            return True
        else:
            return False