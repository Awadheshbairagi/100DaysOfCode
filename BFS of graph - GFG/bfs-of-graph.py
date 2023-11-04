from typing import List
from queue import Queue

class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # Create a boolean array to mark visited nodes.
        visited = [False] * V
        # Create a queue for BFS traversal.
        queue = Queue()
        # List to store BFS traversal result.
        bfs_result = []
        
        # Mark the starting node as visited and enqueue it.
        visited[0] = True
        queue.put(0)
        
        # BFS traversal
        while not queue.empty():
            # Dequeue a vertex from the queue and add it to the result list.
            vertex = queue.get()
            bfs_result.append(vertex)
            # Explore all adjacent vertices of the dequeued vertex.
            for adj_vertex in adj[vertex]:
                if not visited[adj_vertex]:
                    visited[adj_vertex] = True
                    queue.put(adj_vertex)
        
        return bfs_result


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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends