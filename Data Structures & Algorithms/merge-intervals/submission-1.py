class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        a = intervals[0]
        res = []
        for i in range(1, len(intervals)): 
            if a[1] >= intervals[i][0]:
                a = [min(a[0], intervals[i][0]), max(a[1], intervals[i][1])]
            else:
                res.append(a)
                a = intervals[i]
        res.append(a)
        return res