class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(starts, reached):
            que = deque(starts)
            for x, y in starts:
                reached.add((x, y))

            while que:
                i, j = que.popleft()
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < m and \
                        0 <= y < n and \
                        heights[x][y] >= heights[i][j] and \
                        (x, y) not in reached:
                        reached.add((x, y))
                        que.append((x, y))
        
        
        bfs([(0, j) for j in range(n)] + [(i, 0) for i in range(m)], pacific)
        bfs([(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n)], atlantic)            

        return [list(x) for x in pacific & atlantic]
                        



        