class Solution:
    def numDecodings(self, s: str) -> int:
        M = 10**9 + 7
        
        def dp(s, i, memo):
            if i == len(s):
                return 1

            if memo[i] is not None:
                return memo[i]

            if s[i] == "0":
                memo[i] = 0
                return memo[i]

            result = 0

            if s[i] == "*":
                if i + 1 < len(s) and s[i + 1] != "*":
                    if s[i + 1] > "6":
                        result = (9 * dp(s, i + 1, memo) + dp(s, i + 2, memo)) % M
                    else:
                        result = (9 * dp(s, i + 1, memo) + 2 * dp(s, i + 2, memo)) % M

                elif i + 1 < len(s) and s[i + 1] == "*":
                    result = (9 * dp(s, i + 1, memo) + 15 * dp(s, i + 2, memo)) % M

                else:
                    result = 9 * dp(s, i + 1, memo)

            elif s[i] != "*":
                result = dp(s, i + 1, memo)

                if i + 1 < len(s) and s[i + 1] == "*":
                    if s[i] == "1":
                        result = (result + 9 * dp(s, i + 2, memo)) % M
                    elif s[i] == "2":
                        result = (result + 6 * dp(s, i + 2, memo)) % M

                elif i + 1 < len(s):
                    two_digits = int(s[i:i + 2])
                    if 10 <= two_digits <= 26:
                        result = (result + dp(s, i + 2, memo)) % M

            memo[i] = result
            return memo[i]


        return dp(s, 0, [None] * (len(s) + 1))

