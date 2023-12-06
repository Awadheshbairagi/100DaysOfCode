class Solution:
    def partitionString(self, s: str) -> int:
        d = ''
        r = 1
        for c in s:
            if c in d:
                d = c
                r += 1
            else:
                d += c
        return r