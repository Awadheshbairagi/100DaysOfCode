class Solution:
    def isValid(self, code: str) -> bool:
        prefix = suffix = False 
        stack = []
        i = 0 
        while i < len(code): 
            if code[i:i+2] == '</': 
                ii = i = i+2
                for i in range(i, len(code)): 
                    if code[i] == '>': break 
                else: return False 
                if i == len(code)-1: suffix = True 
                tag = code[ii:i]
                if not stack or stack[-1] != tag: return False 
                stack.pop()
                if not stack and not suffix: return False 
            elif code[i:i+3] == '<![': 
                ii = i = i+3
                buffer = 1
                for i in range(i, len(code)): 
                    if code[i] == '[': 
                        if buffer: 
                            buffer = 0 
                            if code[ii:i] != "CDATA": return False 
                    elif code[i:i+3] == ']]>': 
                        if buffer: return False 
                        break 
                else: return False 
            elif code[i] == '<': 
                ii = i = i+1
                for i in range(i, len(code)): 
                    if code[i] == '>': break 
                else: return False 
                if ii == 1: prefix = True 
                tag = code[ii:i]
                if not (all(map(str.isupper, tag)) and 1 <= len(tag) <= 9): return False 
                stack.append(tag)
            i += 1
        return prefix and suffix and not stack 