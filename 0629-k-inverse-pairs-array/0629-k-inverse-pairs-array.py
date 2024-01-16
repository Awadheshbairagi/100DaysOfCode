class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        M = 1000000007
        if k == 0:
            return 1
        if n == 1:
            return 1 if k == 0 else 0
        current_count = [0] * (k + 1)
        current_count[0] = 1
        previous_count = [0] * (k + 1)
        for i in range(n - 2, -1, -1):
            total_count = 0
            threshold = n - i
            for j in range(0, k + 1):
                total_count += current_count[j]
                if j >= threshold:
                    total_count -= current_count[j - threshold]
                total_count %= M
                previous_count[j] = total_count
            current_count, previous_count = previous_count, current_count
        return current_count[k]