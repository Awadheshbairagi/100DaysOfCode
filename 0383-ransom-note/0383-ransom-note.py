class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a dictionary to store character counts in the magazine
        char_counts = {}
        for char in magazine:
            char_counts[char] = char_counts.get(char, 0) + 1
        
        # Check if ransomNote can be constructed from magazine
        for char in ransomNote:
            if char in char_counts and char_counts[char] > 0:
                char_counts[char] -= 1
            else:
                return False
        
        return True
