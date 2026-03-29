class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            filtered = [
                    (interval[1] - interval[0] + 1) for interval in intervals 
                    if interval[0] <= q <= interval[1]
                ]

            if filtered:
                res.append(min(filtered))
            else:
                res.append(-1)
        return res

