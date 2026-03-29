from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((v, t))
        
        minHeap = [(0, k)]
        heapq.heapify(minHeap)

        distance = [float('inf')]*(n + 1)
        distance[0] = 0
        distance[k] = 0
        visited = set()
        while minHeap:
            t, node = heapq.heappop(minHeap)
            visited.add(node)
            for nextNode, t1 in adj[node]:
                if nextNode not in visited:
                    heapq.heappush(minHeap, (t + t1, nextNode))
                    distance[nextNode] = min(distance[nextNode], t + t1)
            
        return max(distance) if len(visited) == n else -1
        