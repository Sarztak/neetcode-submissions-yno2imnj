class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        result = []
        
        # get all the non-overlapping intervals
        while i < n and intervals[i][1] < newInterval[0]: 
            result.append(intervals[i])
            i += 1

        # merge all the intervals that overlap with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        result.append(newInterval)


        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
