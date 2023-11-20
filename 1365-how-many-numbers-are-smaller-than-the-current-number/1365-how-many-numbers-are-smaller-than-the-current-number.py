class Solution:
    def smallerNumbersThanCurrent(self, nums):
        counts = [0] * 102  # Numbers are in the range 0 to 100, so 102 for flexibility
        for num in nums:
            counts[num + 1] += 1  # Increment the count at the index of the number + 1

        # Calculate the cumulative sum
        for i in range(1, 102):
            counts[i] += counts[i - 1]

        result = []
        for num in nums:
            result.append(counts[num])

        return result
