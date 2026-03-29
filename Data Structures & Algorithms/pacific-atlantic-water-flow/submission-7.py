class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        if m == 1 or n == 1:
            res = []
            for i in range(m):
                for j in range(n):
                    res.append([i, j])
            return res
            
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(i, j):
            A = P = False
            visited = set()
            que = deque()
            que.append((i, j))
            visited.add((i, j))

            while que:
                i, j = que.popleft()
                for dx, dy in directions:
                    x, y = i + dx, j + dy

                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited and heights[x][y] <= heights[i][j]:
                        if x == m - 1 or y == n - 1:
                            A = True
                        

                        if x == 0 or y == 0:
                            P = True

                        if A and P:
                            return True

                        else:
                            que.append((x, y))
                            visited.add((x, y))
            return False
        
        res = [[0, n - 1], [m - 1, 0]]

        for i in range(m):
            for j in range(n):
                if [i, j] in [[0, n - 1], [m - 1, 0]]:
                    continue
                if bfs(i, j):
                    res.append([i, j])
        
        return res

        