from collections import defaultdict
from heapq import heappush as push
from heapq import heappop as pop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(points)

        def manDist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                adj[i].append((manDist(points[i], points[j]), j))
        
        minHeap = [(0, 0)]
        visited = set()
        minDist = 0


        while len(visited) < n:
            dist, idx = pop(minHeap)
            if idx in visited:
                continue
            
            visited.add(idx)
            minDist += dist

            for dist, j in adj[idx]:
                if j in visited:
                    continue
                push(minHeap, (dist, j))
        

        return minDist