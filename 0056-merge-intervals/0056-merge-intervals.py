class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        parent = [i for i in range(n)]

        # Merge overlapping intervals using Union-Find
        for i in range(n):
            for j in range(i + 1, n):
                if intervals[i][1] >= intervals[j][0]:
                    union(i, j)

        merged_intervals = collections.defaultdict(list)
        for i in range(n):
            root = find(i)
            merged_intervals[root].extend(intervals[i])

        result = []
        for key, values in merged_intervals.items():
            start = min(values)
            end = max(values)
            result.append([start, end])

        return result
