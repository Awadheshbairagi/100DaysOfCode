class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Calculate factorials for 1 to n
        factorial = [1]
        for i in range(1, n+1):
            factorial.append(factorial[-1] * i)
        
        # Create a list of available numbers to form permutations
        nums = [str(i) for i in range(1, n+1)]
        
        # Decrement k since the list is 0-indexed
        k -= 1
        
        # Build the permutation
        result = []
        for i in range(n, 0, -1):
            index = k // factorial[i - 1]
            k %= factorial[i - 1]
            result.append(nums.pop(index))
        
        # Convert the list to a string and return
        return ''.join(result)
