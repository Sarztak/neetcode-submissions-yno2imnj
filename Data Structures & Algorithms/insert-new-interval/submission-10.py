class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        while i < n:
            if intervals[i][0] > newInterval[0]:
                break
            i = i + 1
        
        intervals.insert(i, newInterval)
    
        stack = [intervals[0]]

        for j in range(1, n + 1):
            x, y = stack[-1]
            a, b = intervals[j]
            if y < a:
                stack.append([a, b])
            else:
                # x <= a the because how we inserted the newInterval
                # so min(x, a) = x
                stack.pop()
                stack.append([min(x, a), max(y, b)])
        
        return stack








