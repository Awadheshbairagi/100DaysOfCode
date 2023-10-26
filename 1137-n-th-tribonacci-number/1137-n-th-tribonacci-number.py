class Solution:
    def tribonacci(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        # Initialize Tribonacci sequence with base values
        tribonacci_sequence = [0, 1, 1]
        
        # Calculate Tribonacci numbers from 3 to n
        for i in range(3, n + 1):
            next_tribonacci = tribonacci_sequence[i - 1] + tribonacci_sequence[i - 2] + tribonacci_sequence[i - 3]
            tribonacci_sequence.append(next_tribonacci)
        
        return tribonacci_sequence[n]
