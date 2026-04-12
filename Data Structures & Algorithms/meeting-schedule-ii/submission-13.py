"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heapify, heappop, heappush

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        
        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        end_of_times: list[int] = [] # array to store the last meeting in a room 
        end_of_times.append(intervals[0].end)
        heapify(end_of_times) 
        max_len = 1 # at least one room is needed in case there is one meeting
        for i in range(1, n):
            # the logic is to check if the room is available or not
            # if not then I add to end time of the meeting that is last to be conducted in a room
            # if there is a room available then I update the end time of a new meeting
            # there an efficiency in the solution: effectively I am trying to find the room which would
            # be available the soonest, this operation can be done in O(1) time using a priority queue
            # then the total complexity of the solution will be O(nlogn) instead of O(n^2)
            # it should also be noted that the testcase on given for this question are not sufficient 
            # to test the following case: assume that there are 3 meeting that all end at 10 and then next meeting
            # starts at 12, by my solution which passed every test case the answer should be 1; but the answer
            # is actually 3 so the max length of the heap needs to be tracked throughout the loop
            
            if end_of_times and end_of_times[0] <= intervals[i].start:
                heappop(end_of_times)
            heappush(end_of_times, intervals[i].end)

            max_len = max(max_len, len(end_of_times)) # update the max length after every addition
            
        
        return max_len