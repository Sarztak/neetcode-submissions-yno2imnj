class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols, diag1, diag2 = set(), set(), set()
        def dfs(row, board):
            if row == n:
                res.append(board.copy())
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board.append('.'*col + 'Q' + '.'*(n - col - 1))
                dfs(row + 1, board)
                board.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        dfs(0, [])
        return res
        