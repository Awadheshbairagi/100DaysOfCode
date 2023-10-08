class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        pattern_dict = {}
        word_dict = {}
        
        for i in range(len(pattern)):
            if pattern[i] in pattern_dict:
                if pattern_dict[pattern[i]] != words[i]:
                    return False
            else:
                pattern_dict[pattern[i]] = words[i]
                
            if words[i] in word_dict:
                if word_dict[words[i]] != pattern[i]:
                    return False
            else:
                word_dict[words[i]] = pattern[i]
        
        return True
