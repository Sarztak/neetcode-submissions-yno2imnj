class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()
        nrow, ncol = len(heights), len(heights[0])
        res = []
        def dfs(r, c, visited, prevHeight):
            if (
                r < 0 or r >= nrow or
                c < 0 or c >= ncol or
                (r, c) in visited or
                prevHeight > heights[r][c]
            ):
                return 
            
            visited.add((r, c))
            dfs(r-1, c, visited, heights[r][c])
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
        
        for c in range(ncol):
            dfs(0, c, pacific, heights[0][c])
            dfs(nrow-1, c, atlantic, heights[nrow-1][c])
        
        for r in range(nrow):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, ncol-1, atlantic, heights[r][ncol-1])
        
        for r in range(nrow):
            for c in range(ncol):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res
        