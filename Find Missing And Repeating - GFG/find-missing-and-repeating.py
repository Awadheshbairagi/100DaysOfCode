class Solution:
    def findTwoElement(self, arr, n): 
        # Repeating number
        repeating = -1
        for i in range(n):
            index = abs(arr[i]) - 1
            if arr[index] < 0:
                repeating = abs(arr[i])
            else:
                arr[index] = -arr[index]

        # Missing number
        missing = -1
        for i in range(n):
            if arr[i] > 0:
                missing = i + 1
                break

        return [repeating, missing]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends