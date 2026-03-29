import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Min-heap to store (maximum elevation so far, x, y)
        minHeap = [(grid[0][0], 0, 0)]
        # Visited array to keep track of visited cells
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        # Directions for moving right and down
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while minHeap:
            currMaxElevation, x, y = heapq.heappop(minHeap)
            
            # If we reach the bottom-right corner, return the maximum elevation
            if x == n - 1 and y == n - 1:
                return currMaxElevation
            
            # Explore the neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # Calculate the new maximum elevation for this path
                    newMaxElevation = max(currMaxElevation, grid[nx][ny])
                    heapq.heappush(minHeap, (newMaxElevation, nx, ny))

        return -1  # This line should never be reached if the input is valid
