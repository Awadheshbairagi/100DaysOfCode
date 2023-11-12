from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_set = set(wordList)
        
        if endWord not in word_set:
            return 0
        
        queue = deque([(beginWord, 1)])
        
        while queue:
            current_word, level = queue.popleft()
            
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]
                    
                    if next_word == endWord:
                        return level + 1
                    
                    if next_word in word_set:
                        word_set.remove(next_word)
                        queue.append((next_word, level + 1))
        
        return 0
