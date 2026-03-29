class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for r in rows:
            for i in range(n):
                matrix[r][i] = 0
        
        for c in cols:
            for j in range(m):
                matrix[j][c] = 0

        
        