class Solution:
    def grayCode(self, n: int) -> List[int]:
        gray_code = []
        for i in range(1 << n):
            gray_code.append(i ^ (i >> 1))
        return gray_code
