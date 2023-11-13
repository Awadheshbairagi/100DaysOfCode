class Solution:
    def singleNumber(self, nums):
        result = 0

        # XOR all the elements in the array
        for num in nums:
            result ^= num

        return result
