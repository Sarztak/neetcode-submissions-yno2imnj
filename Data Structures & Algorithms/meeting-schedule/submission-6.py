"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # if there is no meeting then there is no conflict
        n = len(intervals)
        if n == 0:
            return True
        
        # the reasoning is simple, once sorted we look at the end time of previous being greater than the current
        intervals = sorted(intervals, key=lambda x: (x.start, x.end))

        prev_end = intervals[0].end
        
        for i in range(1, n):
            if prev_end > intervals[i].start:
                return False
            prev_end = intervals[i].end
        
        return True
        
