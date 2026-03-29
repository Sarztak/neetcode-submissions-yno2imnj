class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        cache = {}
        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in cache:
                return cache[(i, j)]
            
            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            return min(dfs(i + 1, j + 1), dfs(i, j + 1), dfs(i + 1, j)) + 1


        return dfs(0, 0)