class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            new_stone = -abs(x - y)
            if new_stone:
                heapq.heappush(stones, new_stone)
        return -stones[0] if stones else 0
        
        