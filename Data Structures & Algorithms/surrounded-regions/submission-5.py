class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O':
                    que = deque([(i, j)])
                    t = True
                    path = [(i, j)]
                    visited = set()
                    visited.add((i, j))
                    while que:
                        a, b = que.popleft()
                        for dx, dy in directions:
                            x, y = a + dx, b + dy
                            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and board[x][y] == 'O':
                                if x in (0, m - 1) or y in (0, n - 1):
                                    t = False
                                que.append((x, y))
                                path.append((x, y))
                                visited.add((x, y))
                    
                    for x, y in path:
                        board[x][y] = 'X' if t else '#'
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'

                

        