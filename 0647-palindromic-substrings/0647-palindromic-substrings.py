class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total = n
        center = 0.0
        while center < n:
            if center.is_integer():
                left, right = int(center) - 1, int(center) + 1
            else:
                left, right = floor(center), ceil(center)
            while left >= 0 and right < n:
                if s[left] != s[right]:
                    break
                total += 1
                left -= 1
                right += 1
            center += 0.5
        return total