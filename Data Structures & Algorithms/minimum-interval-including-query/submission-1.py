class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            minLength = 10000
            for interval in intervals:
                if interval[0] <= q <= interval[1]:
                    minLength = min(minLength, (interval[1] - interval[0] + 1)) 
            res.append(minLength if minLength != 10000 else -1)    
        return res

