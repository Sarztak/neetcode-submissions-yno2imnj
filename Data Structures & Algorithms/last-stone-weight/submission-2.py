class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            y = abs(x - y)
            if y != 0:
                heapq.heappush(maxHeap, -y)
        
        return 0 if len(maxHeap) == 0 else -maxHeap[0]
        