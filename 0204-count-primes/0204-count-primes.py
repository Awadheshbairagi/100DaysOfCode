class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        # Create a boolean array "is_prime[0..n]" and initialize all entries it as true.
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes.

        # Iterate through all numbers less than the square root of n.
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # Mark all multiples of i as not prime.
                for j in range(i*i, n, i):
                    is_prime[j] = False

        # Count the number of primes.
        return sum(is_prime)
