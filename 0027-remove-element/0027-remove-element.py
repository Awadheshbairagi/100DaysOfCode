class Solution:
    def removeElement(self, nums, val):
        # Initialize two pointers, one for iterating through the list
        # and another for keeping track of the position to place non-val elements
        i = 0
        
        # Iterate through the list using the pointer j
        for j in range(len(nums)):
            # If the current element is not equal to val, replace the element at i
            # with the non-val element and move the pointer i to the next position
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        
        # The pointer i now represents the number of elements in the list
        # that are not equal to val, and nums[:i] contains these elements.
        return i
