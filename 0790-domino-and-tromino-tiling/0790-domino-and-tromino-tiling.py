MOD = (10**9) + 7
class Solution:
    def numTilings(self, n: int) -> int:
        memo = {}

        def state(t1, t2):
            if t1 and t2: return 3
            if t1 and not t2: return 1
            if not t1 and t2: return 2

        def recur(i, t1, t2):
            if i == n:
                return 1
            if (i, state(t1, t2)) in memo:
                return memo[(i, state(t1, t2))]
            t3, t4 = i+1 < n, i+1 < n
            count = 0

            if t1 and t2: count += recur(i+1, True, True)
            if t1 and t2 and t3:
                count += recur(i+1, True, False)
                count += recur(i+1, False, True)
            if t1 and not t2 and t3:
                count += recur(i+1, False, True)
            if not t1 and t2 and t4:
                count += recur(i+1, True, False)
            if not t1 and not t2:
                count += recur(i+1, True, True)
            if t1 and t2 and t3 and t4:
                count += recur(i+1, False, False)
            if t1 and not t2 and t3:
                count += recur(i+1, False, False)
            if not t1 and t2 and t3:
                count += recur(i+1, False, False)

            memo[(i, state(t1, t2))] = count
            return count

        return recur(0, True, True) % MOD