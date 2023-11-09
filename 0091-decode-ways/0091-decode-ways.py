class Solution:
    def numDecodings(self, s: str) -> int:
        # Handle edge case: if the input string starts with '0', there is no valid decoding
        if s[0] == '0':
            return 0

        # Initialize an array to store the number of decodings for each position in the string
        dp = [0] * (len(s) + 1)

        # Base case: there is one way to decode an empty string
        dp[0] = 1

        # Fill the dp array
        for i in range(1, len(dp)):
            # If the current digit is not '0', it can be decoded individually
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # If the current and previous digits form a valid two-digit number
            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        # The last element of dp array stores the total number of decodings
        return dp[-1]
