class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers for nums1, nums2, and the merged array
        p1, p2, p = m - 1, n - 1, m + n - 1
        
        # Merge nums1 and nums2 starting from the end
        while p1 >= 0 and p2 >= 0:
            # Compare the elements from the end of nums1 and nums2
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            # Move the pointer for the merged array to the left
            p -= 1
        
        # If there are remaining elements in nums2, copy them to nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
