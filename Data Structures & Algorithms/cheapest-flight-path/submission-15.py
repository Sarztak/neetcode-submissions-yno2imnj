from heapq import heappop as pop
from heapq import heappush as push
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))
        
        minHeap = []
        push(minHeap, (0, src, 0))

        while minHeap:
            price, node, stops = pop(minHeap)

            if stops == k + 1 and node != dst:
                continue
            
            if stops <= k + 1 and node == dst:
                return price
            
            for nextNode, p_dash in adj[node]:
                push(minHeap, (price + p_dash, nextNode, stops + 1))
        
        return -1