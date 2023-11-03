class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self, n):
        if n <= 0:
            return False
        # Count the number of set bits (1s) in the binary representation of n
        count_set_bits = 0
        while n:
            n = n & (n - 1)
            count_set_bits += 1
        # If there is only one set bit, it's a power of 2
        return count_set_bits == 1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        if ob.isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends