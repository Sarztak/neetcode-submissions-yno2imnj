class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        updatedIntervals = []
        if n == 0:
            return [newInterval]
        if n == 1:
            x, y = intervals[0]
            a, b = newInterval
            if a < x:
                updatedIntervals = [newInterval] + intervals
            else:
                updatedIntervals = intervals + [newInterval]

        
        def find():
            target = newInterval[0]
            lo, hi = 0, n - 1
            while lo < hi:
                mid = (lo + hi) // 2
                x = intervals[mid][0]
                y = intervals[mid + 1][0]

                if x <= target < y:
                    return mid
                elif target < x:
                    hi = mid - 1
                elif target > y:
                    lo = mid + 1
            
            return lo

        if n > 1:
            insert_pos = find()
            if insert_pos == 0 and intervals[0][0] > newInterval[1]:
                updatedIntervals = [newInterval] + intervals
            else:
                updatedIntervals = intervals[:insert_pos + 1] + [newInterval] + intervals[insert_pos + 1:]

        # reduce the overlapping intervals until no intervals are overlapping
        # it can be done using stack or linked lists since they provide easy deletion of nodes

        stack = [updatedIntervals[0]]

        for i in range(1, n + 1):
            x, y = stack[-1]
            a, b = updatedIntervals[i]
            if y < a:
                stack.append([a, b])
            else:
                # x <= a the because how we inserted the newInterval
                # so min(x, a) = x
                stack.pop()
                stack.append([min(x, a), max(y, b)])
        
        return stack








