class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nrow, ncol = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r, c, reachable, prev_height):
            if (
                r < 0 or r >= nrow or
                c < 0 or c >= ncol or
                heights[r][c] < prev_height or
                (r, c) in reachable
            ):
                return 
    
            reachable.add((r, c))
            dfs(r + 1, c, reachable, heights[r][c])
            dfs(r - 1, c, reachable, heights[r][c])
            dfs(r, c + 1, reachable, heights[r][c])
            dfs(r, c - 1, reachable, heights[r][c])
                
        for c in range(ncol):
            dfs(0, c, pacific, heights[0][c])
            dfs(nrow - 1, c, atlantic, heights[nrow - 1][c])
        
        for r in range(nrow):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, ncol - 1, atlantic, heights[r][ncol - 1])
        
        res = []

        for r in range(nrow):
            for c in range(ncol):
                if (r, c) in atlantic and (r, c) in pacific:
                    res.append([r, c])
        return res
