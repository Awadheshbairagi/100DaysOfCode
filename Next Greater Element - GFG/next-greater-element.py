class Solution:
    def nextLargerElement(self, arr, n):
        result = [-1] * n  # Initialize the result list with -1
        stack = []  # Stack to store indices of elements in the input array
        
        for i in range(n):
            # Check if the stack is not empty and the current element is greater than the element at the index stored in the stack
            while stack and arr[i] > arr[stack[-1]]:
                # Update the result list with the next greater element for the element at the index stored in the stack
                result[stack.pop()] = arr[i]
            # Push the current index onto the stack
            stack.append(i)
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends