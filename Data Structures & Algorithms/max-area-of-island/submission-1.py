class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def dfs(i, j):
            
            area = 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x = i + dx
                y = j + dy

                if 0 <= x <= m - 1 and \
                    0 <= y <= n - 1 and \
                    (x, y) not in visited and \
                    grid[x][y] != 0:

                    visited.add((x, y))
                    area += dfs(x, y)
                
            return area + 1

        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (i, j) not in visited:
                    visited.add((i, j))
                    maxArea = max(maxArea, dfs(i, j))
        
        return maxArea
        