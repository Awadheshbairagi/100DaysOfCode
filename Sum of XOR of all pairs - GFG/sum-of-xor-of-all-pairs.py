class Solution:
    def sumXOR(self, arr, n):
        total_xor_sum = 0
        max_bit = 31  # Considering integers are 32-bit
        
        for i in range(max_bit, -1, -1):
            count_set_bits = 0
            for num in arr:
                if num & (1 << i):
                    count_set_bits += 1
            total_xor_sum += (count_set_bits * (n - count_set_bits)) * (1 << i)
        
        return total_xor_sum



#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.sumXOR(arr, n)
    print(res)


# } Driver Code Ends