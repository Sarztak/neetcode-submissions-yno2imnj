class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        nrow = len(grid)
        ncol = len(grid[0])
        def dfs(r, c):
            if (
                r < 0 or r >= nrow or
                c < 0 or c >= ncol or
                grid[r][c] == '0'
            ):
                return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        n = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == '1':
                    n += 1
                    dfs(r, c)

        return n
        