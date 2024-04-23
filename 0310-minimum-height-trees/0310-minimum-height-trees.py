class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # Special case when there's only one node
        
        # Step 1: Construct adjacency list representation of the tree
        adj_list = defaultdict(list)
        degrees = [0] * n
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        
        # Step 2: Perform BFS to find minimum height trees
        leaves = deque([node for node in range(n) if degrees[node] == 1])
        
        while n > 2:
            num_leaves = len(leaves)
            n -= num_leaves
            
            for _ in range(num_leaves):
                leaf = leaves.popleft()
                for neighbor in adj_list[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        leaves.append(neighbor)
        
        return list(leaves)