class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Step 1: Create a prefix XOR array
        n = len(arr)
        prefix_xor = [0] * (n + 1)
        
        # Fill the prefix_xor array
        for i in range(1, n + 1):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1]
        
        # Step 2: Answer each query
        result = []
        for left, right in queries:
            result.append(prefix_xor[right + 1] ^ prefix_xor[left])
        
        return result