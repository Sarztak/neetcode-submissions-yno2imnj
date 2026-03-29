class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        if not grid or not grid[0]:
            return -1
        nrow = len(grid)
        ncol = len(grid[0])
        def addCell(r, c):
            nonlocal fresh
            if (
                r in range(nrow) and
                c in range(ncol) and
                grid[r][c] == 1
            ):
                grid[r][c] = 2
                q.append([r, c])
                fresh -= 1
        
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1
        
        time = 0
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                addCell(r - 1, c)
                addCell(r + 1, c)
                addCell(r, c - 1)
                addCell(r, c + 1)
            time += 1
        
        return -1 if fresh else time
















