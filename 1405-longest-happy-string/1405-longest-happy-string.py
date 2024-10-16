class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, "a"))

        if b > 0:
            heapq.heappush(pq, (-b, "b"))

        if c > 0:
            heapq.heappush(pq, (-c, "c"))

        ans = ""
        while pq:
            count, character = heapq.heappop(pq)
            count = -count
            if len(ans) >= 2 and ans[-1] == character and ans[-2] == character:
                if not pq:
                    break
                tempCnt, tempChar = heapq.heappop(pq)
                ans += tempChar
                if (tempCnt + 1) < 0:
                    heapq.heappush(pq, (tempCnt + 1, tempChar))
                heapq.heappush(
                    pq, (-count, character)
                )  # re-add the previous character.
            else:
                count -= 1
                ans += character
                if count > 0:
                    heapq.heappush(pq, (-count, character))
        return ans