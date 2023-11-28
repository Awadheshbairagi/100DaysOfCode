class Solution:
    def maxVowels(self, s, k):
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        max_vowels = 0
        window_vowels = 0
        
        for i in range(k):
            if s[i] in vowels:
                window_vowels += 1
        
        max_vowels = window_vowels
        
        for i in range(k, len(s)):
            if s[i] in vowels:
                window_vowels += 1
            if s[i - k] in vowels:
                window_vowels -= 1
            
            max_vowels = max(max_vowels, window_vowels)
        
        return max_vowels
