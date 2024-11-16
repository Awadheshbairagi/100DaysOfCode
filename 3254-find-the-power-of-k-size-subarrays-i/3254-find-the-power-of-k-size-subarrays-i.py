class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        result = [0] * (length - k + 1)

        for start in range(length - k + 1):
            is_consecutive_and_sorted = True

            # Check if the current subarray is sorted and consecutive
            for index in range(start, start + k - 1):
                if nums[index + 1] != nums[index] + 1:
                    is_consecutive_and_sorted = False
                    break

            # If valid, take the maximum of the subarray, otherwise set to -1
            if is_consecutive_and_sorted:
                # Maximum element of this subarray
                result[start] = nums[start + k - 1]
            else:
                result[start] = -1

        return result