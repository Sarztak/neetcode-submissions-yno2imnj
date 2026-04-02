"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        
        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        end_of_times: list[int] = [] # array to store the last meeting in a room 
        end_of_times.append(intervals[0].end)
        for i in range(1, n):
            is_room_available = False

            # the logic is to check if the room is available or not
            # if not then I add to end time of the meeting that is last to be conducted in a room
            # if there is a room available then I update the end time of a new meeting
            for j in range(len(end_of_times)):
                if end_of_times[j] <= intervals[i].start:
                    is_room_available = True
                    end_of_times[j] = intervals[i].end
                    break
            
            if not is_room_available:
                end_of_times.append(intervals[i].end)
        
        return len(end_of_times)