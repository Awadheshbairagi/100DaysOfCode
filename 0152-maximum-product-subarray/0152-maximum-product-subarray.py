class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0

        max_product = min_product = res = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_product, min_product = min_product, max_product

            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])

            res = max(res, max_product)

        return res
