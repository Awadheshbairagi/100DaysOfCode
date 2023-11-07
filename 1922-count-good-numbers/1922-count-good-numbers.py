class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Calculate (a^b) % MOD using exponentiation by squaring
        def power(a, b):
            result = 1
            while b > 0:
                if b % 2 == 1:
                    result = (result * a) % MOD
                a = (a * a) % MOD
                b //= 2
            return result
        
        # Calculate the total number of good digit strings
        return (power(5, (n + 1) // 2) * power(4, n // 2)) % MOD
