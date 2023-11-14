class Solution:
    def wordBreak(self, s, wordDict):
        # Create a set from wordDict for faster lookup
        word_set = set(wordDict)
        # Initialize a dp list to store whether a substring ending at index i can be segmented
        dp = [False] * (len(s) + 1)
        dp[0] = True  # An empty string can always be segmented

        for i in range(1, len(s) + 1):
            for j in range(i):
                # Check if dp[j] is True and the substring from j to i is in the wordDict
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[len(s)]

