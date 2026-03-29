class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        minHeap = []
        heapq.heapify(minHeap)
        ans = [0]*len(queries)
        queries = sorted((query, idx) for idx, query in enumerate(queries))
        i = 0

        for query, idx in queries:
            while i < len(intervals) and intervals[i][0] <= query:
                heapq.heappush(minHeap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1

            while minHeap and query > minHeap[0][1]: # (length of interval, end of interval)
                heapq.heappop(minHeap)
            
            ans[idx] = minHeap[0][0] if minHeap else -1
        
        return ans

        