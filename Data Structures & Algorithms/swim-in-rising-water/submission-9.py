from heapq import heappush, heappop
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minHeap = [(grid[0][0], 0, 0)]  # (max elevation encountered so far, x, y)
        visited = set()

        while minHeap:
            elevation, i, j = heappop(minHeap)
            if (i, j) == (m - 1, n - 1):
                return elevation  # Found the minimum maximum elevation path
            
            visited.add((i, j))
            for dx, dy in direction:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    heappush(minHeap, (max(elevation, grid[x][y]), x, y))
                    visited.add((x, y))  # Mark as visited when adding to heap to avoid duplicates
