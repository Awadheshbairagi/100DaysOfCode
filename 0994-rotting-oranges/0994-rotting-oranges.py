class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        s = deque()
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    s.append((i, j))
                    visited.add((i, j))
        k = 0
        while s:
            flag = 0
            for h in range(len(s)):
                x, y = s.popleft()
                for i, j in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
                    if 0 <= i < n and 0 <= j < m:
                        if (i, j) not in visited and grid[i][j] == 1:
                            visited.add((i, j))
                            s.append((i, j))
                            grid[i][j] = 2
                            if flag == 0:
                                k += 1
                                flag = 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return k