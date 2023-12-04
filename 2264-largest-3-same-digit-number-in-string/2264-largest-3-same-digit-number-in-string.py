class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good_integer = ""
        
        # Iterate through the string num until 3 characters before the end.
        for i in range(len(num) - 2):
            substr = num[i:i+3]  # Get the 3-digit substring
            
            # Check if the substring consists of only one unique digit.
            if len(set(substr)) == 1:
                # Update the max_good_integer if the current substring is larger.
                max_good_integer = max(max_good_integer, substr)
        
        return max_good_integer
