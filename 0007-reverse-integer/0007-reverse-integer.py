class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1
        reversed_x = 0
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
        reversed_x *= sign
        if reversed_x > INT_MAX or reversed_x < INT_MIN:
            return 0
        
        return reversed_x
