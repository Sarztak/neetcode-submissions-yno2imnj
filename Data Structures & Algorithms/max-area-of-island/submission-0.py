class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        nrow, ncol = len(grid), len(grid[0])
        def dfs(r, c):
            if (
                r < 0 or r >= nrow or
                c < 0 or c >= ncol or
                grid[r][c] == 0
            ):
                return 0
            
            grid[r][c] = 0
            area = 1 + dfs(r + 1, c) + \
            dfs(r - 1, c) + \
            dfs(r, c + 1) + \
            dfs(r, c - 1)
            return area
        
        max_area = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1:
                    max_area = max(dfs(r, c), max_area)
        return max_area

        