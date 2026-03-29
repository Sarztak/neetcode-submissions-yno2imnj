import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [(grid[0][0], 0, 0)]
        heapq.heapify(minHeap)
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while minHeap:
            currMax, x, y = heapq.heappop(minHeap)
            if x == n - 1 and y == n - 1:
                return currMax
            
            for xi, yi in direction:
                nx, ny = x + xi, y + yi
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    newMax = max(currMax, grid[nx][ny])
                    heapq.heappush(minHeap, (newMax, nx, ny))      

      