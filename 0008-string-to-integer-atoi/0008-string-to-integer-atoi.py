class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Ignore leading whitespaces
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # Step 2: Check for sign
        sign = 1
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 3: Read digits until a non-digit character or end of input is reached
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        # Step 4: Apply sign and handle overflow
        num *= sign
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX
        else:
            return num
