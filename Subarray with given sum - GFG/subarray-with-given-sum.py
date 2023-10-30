#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self, arr, n, sum_):
        curr_sum = arr[0]
        start = 0
        end = 1

        while end <= n:
            while curr_sum > sum_ and start < end - 1:
                curr_sum -= arr[start]
                start += 1

            if curr_sum == sum_:
                return [start + 1, end]

            if end < n:
                curr_sum += arr[end]
            end += 1

        return [-1]





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends