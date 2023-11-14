class Solution:
    def reverseWords(self, s):
        # Split the string into words using whitespace as a delimiter
        words = s.split()
        # Reverse the list of words
        words.reverse()
        # Join the reversed words with a single space between them
        return ' '.join(words)

