class Solution:
    def maxLength(self, arr):
        def hasUniqueChars(s):
            return len(set(s)) == len(s)

        def dfs(idx, curr):
            if idx == len(arr) or not hasUniqueChars(curr):
                return len(curr)
            
            max_length = len(curr)
            for i in range(idx, len(arr)):
                if hasUniqueChars(curr + arr[i]):
                    max_length = max(max_length, dfs(i + 1, curr + arr[i]))
            
            return max_length

        return dfs(0, "")
