from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        
        # Populate adjacency list and indegrees
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1
        
        # Initialize queue with courses having indegree 0
        queue = deque([course for course in range(numCourses) if indegree[course] == 0])
        result = []
        
        while queue:
            curr_course = queue.popleft()
            result.append(curr_course)
            
            # Decrement indegree of neighbors and enqueue if indegree becomes 0
            for neighbor in adj_list[curr_course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result if len(result) == numCourses else []
