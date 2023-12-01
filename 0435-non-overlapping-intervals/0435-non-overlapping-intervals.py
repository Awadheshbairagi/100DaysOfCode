class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0
        inn = sorted(intervals, key=lambda x: x[0], reverse=True)
        ans = [inn[0]]
        for s, e in inn[1:]:
            if ans[-1][0] >= e: 
                ans.append([s, e])
            else: 
                cnt += 1
        return cnt