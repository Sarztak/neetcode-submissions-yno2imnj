class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if (
                r < 0 or r >= nrow or
                c < 0 or c >= ncol or
                grid[r][c] == "0" or
                (r, c) in visited
            ):
                return
            
            visited.add((r, c))
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1) 
            dfs(r, c+1)

        res = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    res +=1
        return res