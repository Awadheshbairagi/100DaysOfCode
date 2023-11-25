from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        # Build the graph with division results
        for (num, den), val in zip(equations, values):
            graph[num][den] = val
            graph[den][num] = 1 / val
        
        # Define DFS function to find the division result
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if end in graph[start]:
                return graph[start][end]
            
            visited.add(start)
            for neighbor in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited | {neighbor})
                    if result != -1.0:
                        return graph[start][neighbor] * result
            return -1.0
        
        # Evaluate the queries using DFS
        results = []
        for num, den in queries:
            results.append(dfs(num, den, set()))
        
        return results
