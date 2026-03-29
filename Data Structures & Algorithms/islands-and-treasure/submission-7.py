class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        s = set()
        q = deque()
        nrow = len(grid)
        ncol = len(grid[0])
        if not grid or not grid[0]:
            return grid
        INF = 2147483647
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 0:
                    q.append([r, c])
                    s.add((r, c))

        def addCell(r, c):
            if (
                r >= 0 and r < nrow and
                c >= 0 and c < ncol and
                grid[r][c] != -1 and
                (r, c) not in s
            ):
                q.append([r, c])
                s.add((r, c))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                addCell(r - 1, c)
                addCell(r + 1, c)
                addCell(r, c - 1)
                addCell(r, c + 1)
                grid[r][c] = dist
            dist += 1
        


        