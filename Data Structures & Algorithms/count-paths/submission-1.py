class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n + 1) for _ in range(m + 1)]

        for i in range(n + 1):
            dp[0][i] = 1
        for j in range(m + 1):
            dp[j][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]