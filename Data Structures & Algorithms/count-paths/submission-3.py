class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i: int, j: int) -> int:
            if not ((0 <= i < m) and (0 <= j < n)):
                return 0
            
            if i == m - 1 and j == n - 1:
                return 1
            
            return dfs(i + 1, j) + dfs(i, j + 1)
        
        return dfs(0, 0)
        