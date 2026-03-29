class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return
        
        m, n = len(grid), len(grid[0])

        minutes = 0
        fresh = 0

        que = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1


        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while que and fresh:
            for _ in range(len(que)):
                i, j = que.popleft()
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m  and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        que.append((x, y))

            minutes += 1            

        return minutes if not fresh else -1 
