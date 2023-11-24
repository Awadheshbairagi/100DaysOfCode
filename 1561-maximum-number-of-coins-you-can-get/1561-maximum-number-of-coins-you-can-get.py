class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans = 0
        n = len(piles)
        for i in range(n // 3):
            ans += piles[2 * i + 1]
        return ans
