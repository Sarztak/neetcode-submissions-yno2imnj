class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False]*n for _ in range(m)]

        def dfs(substring, i, j):
            if len(substring) > len(word):
                return False
            
            if substring == word:
                return True
            
            for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    x = i + dx
                    y = j + dy

                    if (0 <= x <= m - 1) and (0 <= y <= n - 1) and not visited[x][y]:
                        visited[x][y] = True
                        res = dfs(substring + board[x][y], x, y)
                        visited[x][y] = False

                        if res:
                            return res
            
            return False

        for i in range(m):
            for j in range(n):
                visited[i][j] = True
                if dfs(board[i][j], i, j):
                    return True
                visited[i][j] = False
        
        return False