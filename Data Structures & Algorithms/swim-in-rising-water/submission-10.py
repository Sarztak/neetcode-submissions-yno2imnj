from heapq import heappush as push
from heapq import heappop as pop
from collections import defaultdict
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
      m, n = len(grid), len(grid[0])
      minHeap = []
      push(minHeap, (grid[0][0], 0, 0))
      visited = set()
      directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
      while minHeap:
        elevation, i, j = pop(minHeap)
        if i == m - 1 and j == n - 1:
            return elevation
        visited.add((i, j))

        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                push(minHeap, (max(grid[x][y], elevation), x, y))

