class Solution:
    def solve(self, board: List[List[str]]) -> None:
        nrow, ncol = len(board), len(board[0])
        def dfs(r, c):
            if (
                r < 0 or r >= nrow or
                c < 0 or c >= ncol or
                board[r][c] == 'X' or
                board[r][c] == 'T'
            ):
                return
            board[r][c] = 'T'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
    
        for c in range(ncol):
            dfs(0, c)
            dfs(nrow - 1, c)
        for r in range(nrow):
            dfs(r, 0)
            dfs(r, ncol - 1)

        for r in range(nrow):
            for c in range(ncol):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'