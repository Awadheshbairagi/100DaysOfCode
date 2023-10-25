class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n+1):
            factorial.append(factorial[-1] * i)
        nums = [str(i) for i in range(1, n+1)]
        k -= 1
        result = []
        for i in range(n, 0, -1):
            index = k // factorial[i - 1]
            k %= factorial[i - 1]
            result.append(nums.pop(index))
        return ''.join(result)
