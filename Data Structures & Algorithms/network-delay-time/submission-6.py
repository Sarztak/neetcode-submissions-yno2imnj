class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, t in times:
            graph[a].append([b, t])
        
        distances = [float('inf')]*(n + 1)
        distances[0] = 0
        distances[k] = 0

        minHeap = [(0, k)]
        heapq.heapify(minHeap)

        while minHeap:
            arrival_time, node = heapq.heappop(minHeap)
            if arrival_time > distances[node]:
                continue # from our discussing yesterday this is done because we already
                # have found the min distance to this node, so no need to visit it again
            for neighbor, travel_time in graph[node]:
                if arrival_time + travel_time < distances[neighbor]:
                    distances[neighbor] = arrival_time + travel_time
                    heapq.heappush(minHeap, (arrival_time + travel_time, neighbor))
        
        maxDist = max(distances)
        return maxDist if maxDist < float('inf') else -1