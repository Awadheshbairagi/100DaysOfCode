class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers for nums1 and nums2, starting from the end.
        p1, p2, p = m - 1, n - 1, m + n - 1
        
        # Compare elements from nums1 and nums2 and place the larger element in nums1.
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2, place them in nums1.
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
