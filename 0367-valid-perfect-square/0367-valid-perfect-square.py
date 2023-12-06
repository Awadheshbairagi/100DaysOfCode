class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num > 0:
            root = int(num ** 0.5)
            return root * root == num