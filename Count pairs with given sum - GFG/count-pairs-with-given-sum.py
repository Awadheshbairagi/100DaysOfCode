class Solution:
    def getPairsCount(self, arr, n, k):
        # Initialize a dictionary to store the frequency of elements in the array
        frequency_map = {}
        pairs_count = 0  # Initialize the count of pairs with sum K

        # Iterate through the array to count the frequency of each element
        for num in arr:
            # Calculate the difference needed to form a pair with sum K
            required_num = k - num
            # If the required number is present in the frequency map, increment the count of pairs
            pairs_count += frequency_map.get(required_num, 0)
            # Update the frequency map with the current number
            frequency_map[num] = frequency_map.get(num, 0) + 1

        return pairs_count  # Return the count of pairs with sum K


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends