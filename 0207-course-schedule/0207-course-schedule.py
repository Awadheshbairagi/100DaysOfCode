from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def hasCycle(course):
            if visited[course] == 1:
                return True
            if visited[course] == -1:
                return False
            
            visited[course] = 1
            
            for neighbor in graph[course]:
                if hasCycle(neighbor):
                    return True
            
            visited[course] = -1
            return False
        
        graph = defaultdict(list)
        
        # Build the directed graph
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        visited = [0] * numCourses
        
        # Check for cycles in each unvisited node
        for course in range(numCourses):
            if hasCycle(course):
                return False
        
        return True
