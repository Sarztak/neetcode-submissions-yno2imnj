class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = []

        for query in queries:
            minLen = float('inf')
            for interval in intervals:
                if interval[0] <= query <= interval[1]:
                    minLen = min(minLen, interval[1] - interval[0] + 1)
            
            if minLen == float('inf'):
                minLen = -1
            
            ans.append(minLen)

        return ans
        