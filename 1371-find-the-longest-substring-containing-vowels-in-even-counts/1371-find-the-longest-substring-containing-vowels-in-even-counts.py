class Solution:
    def findTheLongestSubstring(self, s):
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        counts = {0: -1}  # Initialize count 0 with index -1
        mask = 0
        max_length = 0

        for i, char in enumerate(s):
            if char in vowels:
                # Toggle the mask bit corresponding to the vowel
                mask ^= 1 << vowels[char]

            # If the mask is encountered previously, calculate the length of the substring
            if mask in counts:
                max_length = max(max_length, i - counts[mask])
            else:
                counts[mask] = i

        return max_length
