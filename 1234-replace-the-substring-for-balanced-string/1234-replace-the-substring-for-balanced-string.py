class Solution:
    def balancedString(self, s: str) -> int:
        from collections import Counter
        
        target_count = len(s) // 4
        excess_chars = Counter(s) - Counter({char: target_count for char in 'QWER'})
        
        if all(count <= 0 for count in excess_chars.values()):
            return 0
        
        start = 0
        min_length = float('inf')
        
        for end, char in enumerate(s):
            excess_chars[char] -= 1
            
            while all(count <= 0 for count in excess_chars.values()):
                min_length = min(min_length, end - start + 1)
                excess_chars[s[start]] += 1
                start += 1
        
        return min_length
