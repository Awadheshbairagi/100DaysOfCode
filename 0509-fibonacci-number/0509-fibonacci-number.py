class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        
        def fib_helper(n):
            if n in memo:
                return memo[n]
            if n <= 1:
                memo[n] = n
            else:
                memo[n] = fib_helper(n - 1) + fib_helper(n - 2)
            return memo[n]
        
        return fib_helper(n)
