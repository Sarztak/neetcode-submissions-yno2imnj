from collections import defaultdict 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0]) # m is rows and n is columns

        for row in board: # check the rows first
            d = defaultdict(int)
            for r in row:
                if r == '.':
                    continue
                d[r] += 1
                if d[r] > 1:
                    return False
        
        for j in range(n): # check the columns
            d = defaultdict(int)
            for i in range(m):
                r = board[i][j]
                if r == '.':
                    continue
                d[r] += 1
                if d[r] > 1:
                    return False

        # now check each 3x3 box 
        for i in range(0, m, 3):
            for j in range(0, n, 3):
                d = defaultdict(int)
                for a in range(3):
                    for b in range(3):
                        r = board[i + a][j + b] 
                        if r == '.':
                            continue
                        d[r] += 1
                        if d[r] > 1:
                            return False
        return True
