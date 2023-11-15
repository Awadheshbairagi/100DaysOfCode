class Solution:
    def removeDuplicateLetters(self, s):
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        stack = []

        for idx, char in enumerate(s):
            if char not in stack:
                while stack and char < stack[-1] and idx < last_occurrence[stack[-1]]:
                    stack.pop()
                stack.append(char)

        return ''.join(stack)
