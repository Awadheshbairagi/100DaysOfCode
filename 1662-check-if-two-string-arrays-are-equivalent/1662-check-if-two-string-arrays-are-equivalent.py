class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_combined = ''.join(word1)
        word2_combined = ''.join(word2)
        return word1_combined == word2_combined
