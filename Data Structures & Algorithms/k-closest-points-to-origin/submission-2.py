class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [[-math.sqrt(x*x + y*y), [x, y]] for x, y in points]

        heapq.heapify(minHeap)

        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        return [[x, y] for d, [x, y] in minHeap]
        