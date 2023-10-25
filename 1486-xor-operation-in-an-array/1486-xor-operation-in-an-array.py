class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # Initialize the result with the first element of the array
        result = start
        
        # Generate the nums array and calculate XOR of all elements
        for i in range(1, n):
            num = start + 2 * i
            result ^= num  # Bitwise XOR operation
            
        return result
