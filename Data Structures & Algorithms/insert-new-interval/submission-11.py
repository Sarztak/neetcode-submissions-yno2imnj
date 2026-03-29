class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        ans = [intervals[0]]
        for i in range(1, n + 1):
            if intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(intervals[i][1], ans[-1][1])

        return ans
        