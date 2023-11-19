class Solution:
    def calculateMinimumHP(self, dungeon):
        if not dungeon or not dungeon[0]:
            return 0

        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]

        dp[rows][cols - 1] = dp[rows - 1][cols] = 1

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                min_hp = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(min_hp, 1)

        return dp[0][0]
