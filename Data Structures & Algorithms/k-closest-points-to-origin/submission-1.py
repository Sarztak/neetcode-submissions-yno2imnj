class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = defaultdict(list)
        for x, y in points:
            d = (x**2 + y**2)**0.5
            dist[round(d, 4)].append([x, y])
        
        d = [k for k in dist.keys()]

        heapq.heapify(d)

        closest_points = []

        while len(closest_points) < k:
            closest_points += dist[heapq.heappop(d)]
        
        return closest_points[:k]
        


        