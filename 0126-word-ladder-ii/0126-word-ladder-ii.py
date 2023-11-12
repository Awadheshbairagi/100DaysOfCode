from collections import deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        res = []
        word_set = set(wordList)
        es = endWord
        if es not in word_set:
            return res
        
        goal = 0
        step = 0
        queue = deque([beginWord])
        seen = set([beginWord])
        mapping = {}
        found = False
        
        while queue:
            sz = len(queue)
            mapping[step] = set()
            for _ in range(sz):
                cs = queue.popleft()
                mapping[step].add(cs)
                if cs == endWord:
                    found = True
                    break
                nbrs = self.nb(cs, word_set, seen)
                for ns in nbrs:
                    queue.append(ns)
                    
            if found:
                break
            step += 1
        
        if not found:
            return res
        
        goal = step
        self.dfs(endWord, goal, [es], res, mapping)
        return res
    
    def dfs(self, s, level, lst, res, mapping):
        if level == 0:
            res.append(lst[::-1])
            return
        
        nbrs = set()
        for nss in mapping[level - 1]:
            if self.isnb(nss, s):
                nbrs.add(nss)
                
        for ns in nbrs:
            lst.append(ns)
            self.dfs(ns, level - 1, lst, res, mapping)
            lst.pop()
    
    def isnb(self, s1, s2):
        d = sum(c1 != c2 for c1, c2 in zip(s1, s2))
        return d == 1
    
    def nb(self, s, word_set, seen):
        res = set()
        n = len(s)
        for i in range(n):
            chi = ord(s[i]) - ord('a')
            for j in range(26):
                if j == chi:
                    continue
                ns = s[:i] + chr(ord('a') + j) + s[i+1:]
                if ns in word_set and ns not in seen:
                    res.add(ns)
                    seen.add(ns)
        return res

