from collections import deque

class Solution:
    # Function to find the level of node X using BFS.
    def nodeLevel(self, V, adj, X):
        visited = [False] * V  # Mark all nodes as not visited
        queue = deque([(0, 0)])  # Queue for BFS, (node, level)

        while queue:
            node, level = queue.popleft()
            if node == X:  # If the current node is X, return the level
                return level
            for neighbor in adj[node]:  # Explore neighbors
                if not visited[neighbor]:  # If neighbor is not visited, enqueue it with increased level
                    visited[neighbor] = True
                    queue.append((neighbor, level + 1))

        return -1  # If X is not found, return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
        X=int(input())
        ob = Solution()
        
        print(ob.nodeLevel(V, adj, X))
# } Driver Code Ends