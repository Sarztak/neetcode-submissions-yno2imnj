class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        end  = intervals[0][1]
        count = 1
        for i in range(n):
            x, y = intervals[i]
            if x >= end:
                end = y
                count += 1

            
        return n - count 