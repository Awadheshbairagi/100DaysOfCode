class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        positions = {char: [] for char in 'abcdefghijklmnopqrstuvwxyz'}

        # Store positions of each character
        for i, char in enumerate(s):
            positions[char].append(i)

        # Check for palindromes
        for char, pos_list in positions.items():
            if len(pos_list) > 1:
                left, right = pos_list[0], pos_list[-1]
                unique_chars = set(s[left + 1:right])
                count += len(unique_chars)

        return count

