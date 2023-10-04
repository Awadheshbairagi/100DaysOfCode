class Solution:
    def isPalindrome(self, x: int) -> bool:
       
        if(x<0):
            return False
        rev,temp=0,x
        while(x!=0):
            digit=x%10
            rev=rev*10+digit
            x=x//10
        if(rev==temp):
            return True
        else:
            return False