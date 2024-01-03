from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0
        for s in bank:
            count = 0
            for c in s:
                if c == '1':
                    count += 1
            if count != 0:
                ans += (prev * count)
                prev = count
        return ans