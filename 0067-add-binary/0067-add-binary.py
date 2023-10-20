class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        
        # Iterate through the binary strings from right to left
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            # Get the current bits from a and b (or 0 if index out of range)
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate the sum of bits and carry
            bit_sum = bit_a + bit_b + carry
            carry = bit_sum // 2  # Update carry for the next iteration
            bit_sum %= 2  # Update bit_sum to the current result bit
            
            # Insert the current result bit to the left side of the result list
            result.insert(0, str(bit_sum))
            
            # Move to the next bits in a and b
            i -= 1
            j -= 1
        
        # If there is a carry after iterating through all bits, add it to the leftmost side
        if carry:
            result.insert(0, '1')
        
        # Join the result list into a string and return
        return ''.join(result)
