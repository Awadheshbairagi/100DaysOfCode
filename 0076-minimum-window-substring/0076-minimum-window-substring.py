class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_count_s = {}
        char_count_t = {}
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1
        
        left, right = 0, 0
        min_len = float('inf')
        start_index = 0
        
        required_chars = len(char_count_t)
        chars_found = 0
        
        while right < len(s):
            char = s[right]
            char_count_s[char] = char_count_s.get(char, 0) + 1
            if char in char_count_t and char_count_s[char] == char_count_t[char]:
                chars_found += 1
            
            while chars_found == required_chars:
                window_size = right - left + 1
                if window_size < min_len:
                    min_len = window_size
                    start_index = left
                
                char = s[left]
                char_count_s[char] -= 1
                if char in char_count_t and char_count_s[char] < char_count_t[char]:
                    chars_found -= 1
                
                left += 1
            
            right += 1
        
        return "" if min_len == float('inf') else s[start_index:start_index + min_len]
