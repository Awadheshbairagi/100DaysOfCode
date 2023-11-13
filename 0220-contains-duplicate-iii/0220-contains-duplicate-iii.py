from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        # Create a dictionary to store the buckets and their corresponding elements
        buckets = {}

        # Function to map the number to the corresponding bucket
        def get_bucket(num, width):
            return num // width

        # Calculate the width of each bucket
        width = valueDiff + 1

        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the bucket index for the current number
            bucket = get_bucket(num, width)

            # Check if the bucket or adjacent buckets contain elements within the valueDiff
            if bucket in buckets or (bucket - 1 in buckets and num - buckets[bucket - 1] <= valueDiff) or \
                    (bucket + 1 in buckets and buckets[bucket + 1] - num <= valueDiff):
                return True

            # Add the current bucket to the dictionary
            buckets[bucket] = num

            # Remove the leftmost bucket if exceeding the indexDiff
            if i >= indexDiff:
                leftmost_bucket = get_bucket(nums[i - indexDiff], width)
                del buckets[leftmost_bucket]

        return False

