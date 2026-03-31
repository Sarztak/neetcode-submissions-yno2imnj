class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        n = len(intervals)

        ans = []
        start, end = newInterval

        if n == 0:
            return [newInterval]
            
        i = 0

        # this problem depends on several observation
        # the first one is that the order in which case 1, 2, and 3 appear are fixed
        # first start < intervals[i][1] and then start start <= intervals[i][1] so for 
        # overlap I need end >= intervals[i][0], also question does not clarify
        # if overlapping end points should be merged or not
        # then finally the case 3 when end < intervals[i][0] 
        # without these observations this problem has several edge cases that cannot be handled with breaking your mind
        while i < n and start > intervals[i][1]:
            ans.append(intervals[i])
            i += 1 
        
        while i < n and end >= intervals[i][0]:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        ans.append([start, end])
        ans.extend(intervals[i:])
        
        return ans


