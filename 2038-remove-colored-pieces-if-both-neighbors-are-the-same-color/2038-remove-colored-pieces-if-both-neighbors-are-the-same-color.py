class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count_A, count_B = 0, 0
        for i in range(1, len(colors) - 1):
            if colors[i] == 'A' and colors[i - 1] == 'A' and colors[i + 1] == 'A':
                count_A += 1
            elif colors[i] == 'B' and colors[i - 1] == 'B' and colors[i + 1] == 'B':
                count_B += 1
        return count_A > count_B
