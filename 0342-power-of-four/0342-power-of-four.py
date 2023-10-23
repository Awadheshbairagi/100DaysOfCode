import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Check if n is positive and its logarithm to the base 4 is an integer
        return n > 0 and math.log(n, 4).is_integer()
