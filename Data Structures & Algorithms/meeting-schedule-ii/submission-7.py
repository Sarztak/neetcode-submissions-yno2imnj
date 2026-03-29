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
        
        n = len(intervals)

        for i in range(1, n):
            overLap = True
            for j in range(len(endTime)):
                if intervals[i].start >= endTime[j]:
                    endTime[j] = intervals[i].end
                    overLap = False
                    break
            
            if overLap:
                endTime.append(intervals[i].end)

        
        return len(endTime)