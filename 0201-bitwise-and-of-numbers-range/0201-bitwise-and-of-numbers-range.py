class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while (right > left):  # Loop until right is no longer greater than left
            right = right & (right - 1) # Clear the least significant bit of right
        return right & left