class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR x and y to find differing bits
        xor_result = x ^ y
        # Count the number of set bits in the XOR result
        hamming_distance = 0
        while xor_result:
            # Increment hamming_distance if the last bit is 1
            hamming_distance += xor_result & 1
            # Right shift xor_result to check the next bit
            xor_result >>= 1
        return hamming_distance
