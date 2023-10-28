class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for char in jewels:
            res += stones.count(char)       
        return res
