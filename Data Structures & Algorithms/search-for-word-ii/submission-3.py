class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        visited = [[False]*n for _ in range(m)]
        wl = set()
        def dfs(i, j, word):
            if word in words:
                wl.add(word)

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + dx, j + dy
                if (0 <= x <= m - 1) and (0 <= y <= n - 1) and not visited[x][y]:
                    visited[x][y] = True
                    dfs(x, y, word + board[x][y])
                    visited[x][y] = False
                
        
        for i in range(m):
            for j in range(n):
                visited[i][j] = True
                dfs(i, j, board[i][j])
                visited[i][j] = False

        return list(wl)