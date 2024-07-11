class Solution:
    def reverseParentheses(self, s: str) -> str:
        open_parentheses_indices = deque()
        result = []
        for current_char in s:
            if current_char == "(":
                open_parentheses_indices.append(len(result))
            elif current_char == ")":
                start = open_parentheses_indices.pop()
                result[start:] = result[start:][::-1]
            else:
                result.append(current_char)
        return "".join(result)