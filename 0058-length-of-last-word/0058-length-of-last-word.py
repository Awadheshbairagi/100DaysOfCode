class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()  # Split the input string by spaces
        if not words:  # If there are no words, return 0
            return 0
        return len(words[-1])  # Return the length of the last word
