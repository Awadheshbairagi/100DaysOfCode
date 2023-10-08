class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the result array with 0s
        bits = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # To count the number of 1s in a number, we can use the fact that bits[i] = bits[i >> 1] + (i & 1)
            bits[i] = bits[i >> 1] + (i & 1)
        
        return bits
