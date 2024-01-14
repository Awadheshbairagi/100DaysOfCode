class Solution:
    def findIntegers(self, n: int) -> int:
        f = [1,2]
        for i in range(2,30):
            f.append(f[-1] + f[-2])
        
        ans = last_seen = 0

        for i in range(29,-1,-1):
            if (1 << i) & n:
                ans += f[i]
                if last_seen :
                    return ans
                last_seen = 1
            else:
                last_seen = 0
        return ans + 1