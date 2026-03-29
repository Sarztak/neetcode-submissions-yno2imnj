class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        nrow = len(board)
        ncol = len(board[0])
        def dfs(i, j, c):
            if c == len(word):
                return True
            if (i < 0 or i >= nrow or j < 0 or j >= ncol \
                    or board[i][j] == "#" or board[i][j] != word[c]):
                return False
            temp = board[i][j]
            board[i][j] = "#"
            res = (
                dfs(i - 1, j, c + 1) or 
                dfs(i + 1, j, c + 1) or 
                dfs(i, j - 1, c + 1) or 
                dfs(i, j + 1, c + 1) 
            )

            board[i][j] = temp

            return res
        
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
        