from heapq import heappush as push, heappop as pop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(points)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi = points[i]
                xj, yj = points[j]
                adj[i].append(((abs(xi - xj) + abs(yi - yj), j)))

        minHeap = []
        minCost = 0
        push(minHeap, (0, 0))
        visited = set()
        
        while minHeap:
            md, node = pop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            minCost += md
            if len(visited) == n:
                break
            for d, x in adj[node]:
                if x in visited:
                    continue
                push(minHeap, (d, x))
        
        return minCost














