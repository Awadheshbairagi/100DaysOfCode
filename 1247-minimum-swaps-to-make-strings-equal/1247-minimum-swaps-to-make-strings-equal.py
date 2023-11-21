class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0
        
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if c1 == 'x':
                    xy += 1
                else:
                    yx += 1
        
        if (xy + yx) % 2 != 0:  # If the total count of swaps needed is odd, return -1
            return -1
        
        # Calculate the number of swaps required
        return xy // 2 + yx // 2 + (xy % 2) * 2
