class Solution:
    def sumFourDivisors(self, nums):
        def get_divisors(n):
            divisors = set()
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                    if len(divisors) > 4:
                        return []
            return list(divisors) if len(divisors) == 4 else []
        
        result = 0
        for num in nums:
            divisors = get_divisors(num)
            if divisors:
                result += sum(divisors)
        
        return result
