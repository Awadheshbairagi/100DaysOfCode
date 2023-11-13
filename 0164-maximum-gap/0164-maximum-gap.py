class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        # Find the maximum number to determine the number of digits
        max_num = max(nums)

        # Perform Radix Sort
        exp = 1
        while max_num // exp > 0:
            self.countingSort(nums, exp)
            exp *= 10

        # Calculate the maximum gap
        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i] - nums[i - 1])

        return max_gap

    def countingSort(self, nums, exp):
        n = len(nums)
        output = [0] * n
        count = [0] * 10

        # Count occurrences of each digit
        for i in range(n):
            index = nums[i] // exp
            count[index % 10] += 1

        # Update count to store the position of each digit in the output
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array using counting sort
        i = n - 1
        while i >= 0:
            index = nums[i] // exp
            output[count[index % 10] - 1] = nums[i]
            count[index % 10] -= 1
            i -= 1

        # Update the original array
        for i in range(n):
            nums[i] = output[i]
