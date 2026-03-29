class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(i, j, reached):
            que = deque()
            que.append((i, j))
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
        
        
        for j in range(n):
            if (0, j) not in pacific:
                pacific.add((0, j))
                bfs(0, j, pacific)
            
        for i in range(m):
            if (i, 0) not in pacific:
                pacific.add((i, 0))
                bfs(i, 0, pacific)
        
        for j in range(n):
            if (m - 1, j) not in atlantic:
                atlantic.add((m - 1, j))
                bfs(m - 1, j, atlantic)
        
        for i in range(m):
            if (i, n - 1) not in atlantic:
                atlantic.add((i, n - 1))
                bfs(i, n - 1, atlantic)
            

        return [list(x) for x in pacific.intersection(atlantic)]
                        



        