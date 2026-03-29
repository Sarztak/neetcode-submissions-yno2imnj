class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]

        ans = []
        insert_pos = 0
        for i in range(n):
            ans.append(intervals[i])
            insert_pos = i
            if intervals[i][1] < newInterval[0]:
                if i == n - 1:
                    ans.append(newInterval)
                continue
            else:
                # various edge cases are possible here 
                if newInterval[1] < intervals[i][0]:
                    temp = ans.pop()
                    ans.extend([newInterval, temp])
                else:
                    ans[-1] = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                
                break

        # all these downstream processing tasks depend on the previous one, and this one
        # has an assumption, that the last interval and new interval are overlapping, when they
        # may not be overlapping, to correct this we need to check again or better yet, do 
        # do it upstream
        # ans[-1][1] = max(ans[-1][1], newInterval[1])

        for j in range(insert_pos + 1, n):
            if intervals[j][0] > ans[-1][1]:
                ans.append(intervals[j])
            else:
                ans[-1][1] = max(intervals[j][1], ans[-1][1])

        return ans
        