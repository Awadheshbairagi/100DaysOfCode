class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        line_length = 0
        
        for word in words:
            if line_length + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                spaces = maxWidth - line_length
                if len(line) == 1:
                    result.append(line[0] + ' ' * spaces)
                else:
                    gaps = len(line) - 1
                    spaces_between_words = spaces // gaps
                    extra_spaces = spaces % gaps
                    line_str = ''
                    for i in range(len(line) - 1):
                        line_str += line[i] + ' ' * spaces_between_words
                        if extra_spaces > 0:
                            line_str += ' '
                            extra_spaces -= 1
                    line_str += line[-1]
                    result.append(line_str)
                
                line = [word]
                line_length = len(word)
        
        last_line = ' '.join(line)
        last_line = last_line.ljust(maxWidth)
        result.append(last_line)
        
        return result
