from collections import defaultdict
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        cache = defaultdict(int)
        def dfs(i, j, currStr):
            if currStr == t:
                return 1
            if i == m or j == n:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            total = 0
            if s[i] == t[j]:
                total += dfs(i + 1, j + 1, currStr + s[i])
            total += dfs(i + 1, j, currStr)
            cache[(i, j)] = total
            return total

        return dfs(0, 0, "")