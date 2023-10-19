class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Use the find() method to find the first occurrence of needle in haystack
        index = haystack.find(needle)
        
        # Return the index of the first occurrence or -1 if not found
        return index
