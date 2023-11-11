class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        
        while columnNumber > 0:
            remainder = columnNumber % 26
            if remainder == 0:
                remainder = 26
            result += chr(ord('A') + remainder - 1)
            columnNumber = (columnNumber - remainder) // 26
        
        return result[::-1]
