class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        
        minHeap = []
        heapq.heapify(minHeap)
        connected = [False]*n
        numEdges = 0
        totalCost = 0

        connected[0] = True

        for i, [x, y] in enumerate(points):
            manDist = abs(points[0][0] - x) + abs(points[0][1] - y)
            heapq.heappush(minHeap, (manDist, i))
        
        while minHeap and numEdges < n - 1:
            dist, i = heapq.heappop(minHeap)
            if connected[i]:
                continue
            totalCost += dist
            connected[i] = True
            numEdges += 1
            for j in range(n):
                if not connected[j]:
                    manDist = abs(points[i][0] - points[j][0]) + \
                    abs(points[i][1] - points[j][1])
                    heapq.heappush(minHeap, (manDist, j))
        return totalCost
        