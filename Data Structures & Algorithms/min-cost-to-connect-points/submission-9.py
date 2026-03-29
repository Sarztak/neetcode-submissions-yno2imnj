class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        minHeap = []
        heapq.heapify(minHeap)
        x0, y0 = points[0]
        connected = [False]*n
        connected[0] = True
        minCost = 0
        for i in range(1, n):
            xi, yi = points[i]
            manDist =  abs(xi - x0) + abs(yi - y0)
            heapq.heappush(minHeap, (manDist, i))
            
        while minHeap:
            dist, idx = heapq.heappop(minHeap)
            
            if not connected[idx]:
                minCost += dist
                connected[idx] = True
                x, y = points[idx]
                for i in range(n):
                    if not connected[i]:
                        xi, yi = points[i]
                        manDist = abs(xi - x) + abs(yi - y)
                        heapq.heappush(minHeap, (manDist, i))
        return minCost