from collections import Counter

class Solution:
    def sortString(self, s):
        count = Counter(s)
        result = []
        while count:
            for char in sorted(count):
                if char in count:
                    result.append(char)
                    count[char] -= 1
                    if count[char] == 0:
                        del count[char]
            for char in sorted(count, reverse=True):
                if char in count:
                    result.append(char)
                    count[char] -= 1
                    if count[char] == 0:
                        del count[char]
        return ''.join(result)
