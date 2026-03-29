class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        def dfs(i, j, currStr):
            if currStr == t:
                return 1
            if i == m or j == n:
                return 0
            
            total = 0
            if s[i] == t[j]:
                total += dfs(i + 1, j + 1, currStr + s[i])
            
            total += dfs(i + 1, j, currStr)

            return total
        
        total = 0

        # for i in range(1):
        #     total += dfs(i, 0, "")
        
        return dfs(0, 0, "")