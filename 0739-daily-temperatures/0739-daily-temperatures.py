class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        stack = [] 
        result = [0] * n 
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)     
        return result