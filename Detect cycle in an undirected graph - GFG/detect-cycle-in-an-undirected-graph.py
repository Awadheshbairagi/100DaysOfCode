from typing import List

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Helper function to perform DFS traversal.
        def dfs(node, parent):
            visited[node] = True
            # Traverse all adjacent nodes of the current node.
            for neighbor in adj[node]:
                # If the neighbor is not visited, perform DFS from it.
                if not visited[neighbor]:
                    if dfs(neighbor, node):
                        return True
                # If the neighbor is visited and not the parent, cycle detected.
                elif neighbor != parent:
                    return True
            return False
        
        # Create a boolean array to mark visited nodes.
        visited = [False] * V
        
        # Perform DFS traversal from each unvisited node.
        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True
        
        return False


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends