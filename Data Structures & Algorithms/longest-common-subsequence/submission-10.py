class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = '*' + text1
        text2 = '#' + text2
        m = len(text1)
        n = len(text2)
        cache = [[0]*n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):

                if text1[i] == text2[j]:
                    cache[i][j] = 1 + cache[i - 1][j - 1]
                else:
                    cache[i][j] =  max(cache[i - 1][j], cache[i][j - 1])
        
        return cache[-1][-1]

        