class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        queue = deque(piles)
        ans = 0
        while queue:
            queue.pop() 
            ans += queue.pop() 
            queue.popleft() 
        return ans