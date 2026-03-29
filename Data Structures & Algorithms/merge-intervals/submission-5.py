class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        stack = [intervals[0]]
        n = len(intervals)
        for j in range(1, n):
            x, y = stack[-1]
            a, b = intervals[j]
            if y < a:
                stack.append([a, b])
            elif b < x:
                t = stack.pop()
                stack.append([a, b])
                stack.append(t)
            else:
                stack.pop()
                stack.append([min(x, a), max(y, b)])
        
        return stack


        