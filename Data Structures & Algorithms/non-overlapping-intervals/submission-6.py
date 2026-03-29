class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        a = intervals[0]
        n = len(intervals)
        count = 0
        res = [a]
        for i in range(1, n):
            if a[1] > intervals[i][0]:
                count += 1
            else:
                a = intervals[i]
                res.append(a)
        
        return n - len(res)
        