class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        xx=(a|b)^c
        yy=a&b&xx
        return bin(xx).count('1')+bin(yy).count('1')