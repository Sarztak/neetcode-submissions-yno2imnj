from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        iternary = []
        for u, v in tickets:
            heapq.heappush(adj[u], v)

        def dfs(node):
            while adj[node]:
                dfs(heapq.heappop(adj[node]))
            iternary.append(node)
        
        dfs('JFK')

        return iternary[::-1]
