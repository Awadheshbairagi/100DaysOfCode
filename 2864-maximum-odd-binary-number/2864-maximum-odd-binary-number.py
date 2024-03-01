class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        arr = sorted(s)
        secondLast = len(arr) - 2
        for i in range(len(arr) // 2):
            arr[i], arr[secondLast - i] = arr[secondLast - i], arr[i]
        return "".join(arr)