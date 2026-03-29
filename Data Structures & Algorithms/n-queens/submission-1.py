class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, diag1, diag2 = set(), set(), set()
        res = []

        def dfs(row, board):
            if row == n:
                res.append(board.copy())
                return
            for col in range(n):
                if col not in cols and (row + col) not in diag1 and\
                 (row - col) not in diag2:
                 cols.add(col)
                 diag1.add(row + col)
                 diag2.add(row - col)
                 current_row = '.' * col + 'Q' + '.' * (n - col - 1)
                 board.append(current_row)  
                 
                 dfs(row + 1, board)
                 
                 board.pop()
                 cols.remove(col)
                 diag1.remove(row + col)
                 diag2.remove(row - col)

        dfs(0, [])
        return res