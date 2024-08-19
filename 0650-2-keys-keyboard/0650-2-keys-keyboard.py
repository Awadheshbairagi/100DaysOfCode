class Solution:

    def __init__(self):
        self.n = 0

    def _min_steps_helper(self, curr_len, paste_len):
        # base case: reached n A's, don't need more operations
        if curr_len == self.n:
            return 0
        # base case: exceeded n `A`s, not a valid sequence, so
        # return max value
        if curr_len > self.n:
            return 1000

        # copy all + paste
        opt1 = 2 + self._min_steps_helper(curr_len * 2, curr_len)
        # paste
        opt2 = 1 + self._min_steps_helper(curr_len + paste_len, paste_len)

        return min(opt1, opt2)

    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        self.n = n
        # first step is always a Copy All operation
        return 1 + self._min_steps_helper(1, 1)