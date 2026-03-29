class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False]*n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, currLen):
            visited[i][j] = True
            maxLen = 0
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and \
                    0 <= y < n and \
                    matrix[x][y] > matrix[i][j] and \
                    not visited[x][y]:
                    maxLen = max(dfs(x, y, currLen + 1), maxLen)

            visited[i][j] = False

            return max(maxLen, currLen + 1)

        maxLen = 0
        for i in range(m):
            for j in range(n):
                maxLen = max(dfs(i, j, 0), maxLen)
        
        return maxLen