from collections import defaultdict

class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        # Using memoization to store intermediate results
        memo = defaultdict(list)

        def backtrack(start):
            if start == len(s):
                return [[]]

            if start in memo:
                return memo[start]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # Recursively check the remaining part of the string
                    next_sentences = backtrack(end)
                    for next_sentence in next_sentences:
                        sentences.append([word] + next_sentence)

            memo[start] = sentences
            return sentences

        sentences = backtrack(0)
        # Joining the word lists into strings
        return [' '.join(words) for words in sentences]
