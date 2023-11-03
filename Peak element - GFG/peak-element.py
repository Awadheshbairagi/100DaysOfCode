class Solution:   
    def peakElement(self, arr, n):
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Compare mid element with its neighbors (if they exist)
            if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
                return mid  # Found a peak element

            # If the element to the left is greater, move left
            elif mid > 0 and arr[mid - 1] > arr[mid]:
                right = mid - 1
            # If the element to the right is greater, move right
            else:
                left = mid + 1

        return -1  # No peak element found



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends