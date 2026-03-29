from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((v, t))
        
        minHeap = [(0, k)]
        heapq.heapify(minHeap)

        maxTime = 0
        visited = set()
        while minHeap:
            t, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            maxTime = t
            
            for nextNode, t1 in adj[node]:
                if nextNode not in visited:
                    heapq.heappush(minHeap, (t + t1, nextNode))
            
        return maxTime if len(visited) == n else -1
        