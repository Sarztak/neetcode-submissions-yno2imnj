class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return intervals
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        ans = [intervals[0]]
        
        for i in range(1, n):
            # this particular ans[-1] was not something I had on paper, it just wrote itself down as I was typing
            if ans[-1][1] >= intervals[i][0]:
                start, end = ans.pop()
                # start is not required because sorting guarantees that start will be less than or equal to
                # start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
                ans.append([start, end])
            else:
                ans.append(intervals[i])
        
        return ans
        