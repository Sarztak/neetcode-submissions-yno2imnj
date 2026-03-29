from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return 
        INF = 2147483647
        m, n = len(grid), len(grid[0])

        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while queue:
            i, j = queue.popleft()
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] == INF:
                    grid[x][y] = grid[i][j] + 1
                    queue.append((x, y))
            




        