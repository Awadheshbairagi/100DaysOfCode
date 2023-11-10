from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacency_dict = defaultdict(list)

        # Build the adjacency dictionary
        for pair in adjacentPairs:
            u, v = pair
            adjacency_dict[u].append(v)
            adjacency_dict[v].append(u)

        # Find the start node (a node with only one neighbor)
        start = None
        for node, neighbors in adjacency_dict.items():
            if len(neighbors) == 1:
                start = node
                break

        # Perform depth-first search to reconstruct the array
        def dfs(node, visited):
            visited.add(node)
            result.append(node)
            for neighbor in adjacency_dict[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        result = []
        dfs(start, set())

        return result
