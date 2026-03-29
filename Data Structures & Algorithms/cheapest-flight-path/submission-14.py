class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))
        
        def dfs(currStop, currPrice, totalStops):
            print(currStop, currPrice, totalStops)
            if totalStops == k + 1 and currStop != dst:
                return -1
            if currStop == dst and totalStops <= k + 1:
                return currPrice

            minPrice = []
            for nextStop, nextPrice in adj[currStop]:
                minPrice.append(dfs(nextStop, currPrice + nextPrice, totalStops + 1))
            
            minPrice = [price for price in minPrice if price != -1]
                
            return min(minPrice) if minPrice else -1
        
        return dfs(src, 0, 0)