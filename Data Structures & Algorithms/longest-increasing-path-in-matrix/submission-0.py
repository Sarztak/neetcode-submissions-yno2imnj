class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = {} # we store the max path length as value and key is the position

        def dfs(x, y): 
            if (x, y) in dp:
                return dp[(x, y)] # if we already know max till this point return the value
            
            # loop through all the possible next positions and find the max length
            d = [(-1 ,0), (1, 0), (0, -1), (0, 1)]
            maxLength = 1
            for dx, dy in d:
                xi, yi = x + dx, y + dy

                if (xi >= 0 and xi < m) and (yi >= 0 and yi < n) and \
                    matrix[x][y] < matrix[xi][yi]:
                    maxLength = max(maxLength, dfs(xi, yi) + 1)
            
            dp[(x, y)] = maxLength
            return maxLength
        
        maxLength = -float("inf")
        for i in range(m):
            for j in range(n):
                maxLength = max(maxLength, dfs(i, j))
            
        return maxLength

        