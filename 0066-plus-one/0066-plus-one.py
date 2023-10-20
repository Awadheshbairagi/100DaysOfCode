class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Traverse the digits from right to left
        for i in range(n - 1, -1, -1):
            # If the current digit is less than 9, just increment it and return the digits
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the current digit is 9, set it to 0 and continue to the next digit
            else:
                digits[i] = 0
        
        # If all digits were 9, add a new digit at the beginning of the array
        digits.insert(0, 1)
        return digits
