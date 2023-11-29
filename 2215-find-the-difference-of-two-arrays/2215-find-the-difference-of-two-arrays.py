class Solution:
    def getElementsOnlyInFirstList(self, nums1, nums2):
        only_in_nums1 = set()

        for num in nums1:
            exist_in_nums2 = False
            for x in nums2:
                if x == num:
                    exist_in_nums2 = True
                    break

            if not exist_in_nums2:
                only_in_nums1.add(num)

        return list(only_in_nums1)

    def findDifference(self, nums1, nums2):
        return [self.getElementsOnlyInFirstList(nums1, nums2), self.getElementsOnlyInFirstList(nums2, nums1)]
