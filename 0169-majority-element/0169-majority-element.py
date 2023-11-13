class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        # Find the candidate for the majority element
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        # Verify if the candidate is the majority element
        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        return candidate
