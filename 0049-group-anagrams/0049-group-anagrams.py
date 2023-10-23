from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to store anagrams
        anagrams = {}
        for word in strs:
            # Sort the characters in the word and use it as a key in the dictionary
            sorted_word = tuple(sorted(word))
            # If the key exists, append the word to the corresponding anagram group
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            # If the key doesn't exist, create a new list with the word as the first element
            else:
                anagrams[sorted_word] = [word]
        # Convert the values of the dictionary to a list to get the grouped anagrams
        grouped_anagrams = list(anagrams.values())
        return grouped_anagrams
