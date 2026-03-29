class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = set()

        def dfs(i, j):

            res = False

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x = i + dx
                y = j + dy

                if 0 <= x <= m - 1 and \
                0 <= y <= n - 1 and \
                (x, y) not in visited and \
                grid[x][y] != "0":
                    visited.add((x, y))

                    dfs(x, y)

        count = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] != "0":
                    visited.add((i, j))
                    dfs(i, j)
                    count += 1
        return count
        