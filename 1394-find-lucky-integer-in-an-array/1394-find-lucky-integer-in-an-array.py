from collections import Counter

class Solution:
    def findLucky(self, arr):
        # Count frequency of each number in the array
        freq = Counter(arr)
        max_lucky = -1
        
        # Iterate through the frequencies and find lucky numbers
        for num, frequency in freq.items():
            if num == frequency:  # Check if number's frequency is equal to its value
                max_lucky = max(max_lucky, num)  # Update the largest lucky number found so far
        
        return max_lucky
