class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        minDist = []
        q = deque()
        q.append([src, 0, 0]) # src, nodes travelled between src and dist, price

        for s, d, price in flights:
            graph[s].append([d, price])
        
        while q:
            s, curr_price, count = q.popleft()
            if s == dst and count < k + 2:
                minDist.append(curr_price)
            
            for dest, price in graph[s]:
                if count + 1 < k + 2:
                    q.append([dest, curr_price + price, count + 1])
        
        return min(minDist) if minDist else -1

            




        