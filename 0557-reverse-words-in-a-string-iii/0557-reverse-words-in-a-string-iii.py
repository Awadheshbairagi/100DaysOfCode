class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        last_space_index = -1
        for str_index in range(len(s)):
            if str_index == len(s) - 1 or s[str_index] == ' ':
                reverse_str_index = str_index if str_index == len(s) - 1 else str_index - 1
                while reverse_str_index > last_space_index:
                    result += s[reverse_str_index]
                    reverse_str_index -= 1
                if str_index != len(s) - 1:
                    result += ' '
                last_space_index = str_index
        return result
