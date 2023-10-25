class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create dictionaries to store the frequency of elements in nums1 and nums2
        freq1 = {}
        freq2 = {}
        
        # Populate the frequency dictionaries
        for num in nums1:
            freq1[num] = freq1.get(num, 0) + 1
        for num in nums2:
            freq2[num] = freq2.get(num, 0) + 1
        
        # Find the intersection of elements based on the minimum frequency in both arrays
        intersection = []
        for num in freq1.keys():
            if num in freq2:
                # Add the element to the intersection list the minimum number of times it appears in both arrays
                intersection.extend([num] * min(freq1[num], freq2[num]))
        
        return intersection
