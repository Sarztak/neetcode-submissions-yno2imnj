class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, t in times:
            graph[s].append([d, t])

        distances = {i : float('inf') for i in range(1, n+1)}
        distances[k] = 0
        minHeap = [(0, k)]
        heapq.heapify(minHeap)

        while minHeap:
            curr_dist, curr_node = heapq.heappop(minHeap)
            if curr_dist > distances[curr_node]:
                continue # if I can reach this mode via some other path that is shorter, 
                # then I will take that and leave this one
            
    
            for neighbor, travel_dist in graph[curr_node]:
                distance = curr_dist + travel_dist
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(minHeap, (distance, neighbor))



        max_dist = max(distances.values())
        return max_dist if max_dist < float('inf') else -1

            