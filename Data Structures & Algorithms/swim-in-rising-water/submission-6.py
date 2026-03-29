class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [(grid[0][0], 0, 0)] # time to reach, x, y
        heapq.heapify(minHeap)
        visited = set()
        visited.add((0, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while minHeap:
            currElevation, x, y = heapq.heappop(minHeap)
            if x == n - 1 and y == n - 1:
                return currElevation
            for dx, dy in directions:
                xi = x + dx
                yi = y + dy
                if 0 <= xi < n and 0 <= yi < n and (xi, yi) not in visited:
                    visited.add((xi, yi))
                    maxElevation = max(currElevation, grid[xi][yi])
                    heapq.heappush(minHeap, (maxElevation, xi, yi))
        return -1
                
            