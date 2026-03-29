"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        
        intervals.sort(key=lambda x: x.start)
        endTime = [intervals[0].end]
        heapq.heapify(endTime)

        n = len(intervals)

        for i in range(1, n):
            if intervals[i].start >= endTime[0]:
                heapq.heappop(endTime)
            heapq.heappush(endTime, intervals[i].end)

        
        return len(endTime)