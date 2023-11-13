class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        vowel_indices = [i for i, char in enumerate(s) if char in vowels]

        sorted_vowels = sorted([s[i] for i in vowel_indices])

        result = list(s)

        for i, char in zip(vowel_indices, sorted_vowels):
            result[i] = char

        return ''.join(result)

