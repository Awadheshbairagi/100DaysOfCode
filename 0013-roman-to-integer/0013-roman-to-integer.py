class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0
        
        for numeral in s[::-1]:  # Iterate the string in reverse order
            current_value = roman_dict[numeral]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
        
        return total
