class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0 # this case won't happen because 1 <= n <= 1000 constrains

        intervals = sorted(intervals, key=lambda x: (x[0], x[1])) 
        
        prev_start, prev_end = intervals[0] # also there is no need to track everything, just the last start, and end
        intervals_to_remove = 0
        # intervals = [[x + 100, y + 100] for x, y in intervals]
        print(intervals)
        for i in range(1, n):
            if prev_end > intervals[i][0]:
                intervals_to_remove += 1
                if prev_end > intervals[i][1]:
                    print([prev_start, prev_end])
                    prev_start, prev_end = intervals[i]
                else:
                    print(intervals[i])
            else:
                prev_start, prev_end = intervals[i]
        return intervals_to_remove
        
        