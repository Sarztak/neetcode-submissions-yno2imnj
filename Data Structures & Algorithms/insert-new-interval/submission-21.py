class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        n = len(intervals)

        ans = []
        start, end = newInterval

        if n == 0:
            return [newInterval]
            
        i = 0

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


