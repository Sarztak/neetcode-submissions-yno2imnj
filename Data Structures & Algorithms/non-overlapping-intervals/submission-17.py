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
                # it is not enough to just remove the one in the front because that does not 
                # lead to minimal removals, we need to keep those that are shorter and remove those that are longer
                # we can remove both the previous one and the current one, so decide based on the end point
                # start point is already decided by sorting
                if prev_end > intervals[i][1]:
                    prev_end = intervals[i][1]
            else:
                prev_end = intervals[i][1]
        return intervals_to_remove
        
        