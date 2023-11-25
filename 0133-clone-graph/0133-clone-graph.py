from collections import defaultdict
from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}
        
        def dfs(original):
            if original in visited:
                return visited[original]
            
            cloned = Node(original.val)
            visited[original] = cloned
            
            for neighbor in original.neighbors:
                cloned_neighbor = dfs(neighbor)
                cloned.neighbors.append(cloned_neighbor)
            
            return cloned
        
        return dfs(node)
