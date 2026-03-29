class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        def dfs(i, j):
            if i == m and j == n:
                return True
            
            if j < n - 1 and p[j + 1] == '*':
                if dfs(i, j + 2):
                    return True
                if i < m and (s[i] == p[j] or p[j] == '.'):
                    if dfs(i + 1, j):
                        return True
            if i < m and j < n and (s[i] == p[j] or p[j] == '.'):
                if dfs(i + 1, j + 1):
                    return True

            return False
        
        return dfs(0, 0)