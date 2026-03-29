"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        prevEnd = intervals[0].end

        for obj in intervals[1:]:
            if prevEnd > obj.start:
                return False
            else:
                prevEnd = obj.end
        return True
