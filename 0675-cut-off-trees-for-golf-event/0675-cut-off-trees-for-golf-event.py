class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        order = []
        m = len(forest)
        n = len(forest[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    order.append(forest[i][j])
        order.sort()
        res = 0

        def bfs(start, target):
            if forest[start[0]][start[1]] == target: return start
            nonlocal res
            q = deque([start])
            v = set([start])
            while q:
                res += 1
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr = dr + r
                        nc = dc + c
                        if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in v and forest[nr][nc] != 0:
                            q.append((nr,nc))
                            v.add((nr,nc))
                            if forest[nr][nc] == target:
                                forest[nr][nc] = 1
                                return (nr, nc)
            return -1
        
        curPos = (0,0)
        for i in range(len(order)):
            curPos = bfs(curPos,order[i])
            if curPos == -1: return -1
        return res