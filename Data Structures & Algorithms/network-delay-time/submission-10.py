from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        minHeap = [(0, k)]
        heapq.heapify(minHeap)
        distance = [float('inf')]*(n + 1)
        distance[k] = 0
        distance[0] = 0
        totalTime = 0
        visited = set()
        
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            distance[node] = time

            for nextNode, weight in adj[node]:
                heapq.heappush(minHeap, ((weight + time), nextNode))

        return max(distance) if len(visited) == n else -1

        