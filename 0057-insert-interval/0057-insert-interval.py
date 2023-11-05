class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        import bisect

        bisect.insort(intervals, newInterval)
        answer = []
        for i in intervals:
            if not answer or answer[-1][1] < i[0]:
                answer.append(i)
            else:
                answer[-1][1] = max(answer[-1][1], i[1])
        return answer
