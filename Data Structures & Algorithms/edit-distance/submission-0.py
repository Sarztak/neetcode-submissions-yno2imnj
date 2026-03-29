'''
Filling the DP Table
Now, let's break down how we fill the DP table for each character in word1 and word2:

When word1[i-1] equals word2[j-1]:
If the last characters are the same, no new operation is needed. Thus:
plaintext

Copy Code
dp[i][j] = dp[i-1][j-1]
This means that the edit distance is the same as that for the first i-1 characters of word1 and the first j-1 characters of word2.
When word1[i-1] does not equal word2[j-1]:
You have three options:
Insert: If you want to insert word2[j-1] into word1, you can think of it as transforming the first i characters of word1 to the first j-1 characters of word2, and then inserting the last character of word2. This corresponds to:
plaintext

Copy Code
dp[i][j-1] + 1
Delete: If you want to delete word1[i-1], you can think of it as transforming the first i-1 characters of word1 to the first j characters of word2, and then deleting the last character of word1. This corresponds to:
plaintext

Copy Code
dp[i-1][j] + 1
Replace: If you want to replace word1[i-1] with word2[j-1], you can think of it as transforming the first i-1 characters of word1 to the first j-1 characters of word2, and then replacing the last character of word1 with the last character of word2. This corresponds to:
plaintext

Copy Code
dp[i-1][j-1] + 1
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0]*(n + 1) for _ in range(m + 1)]

        dp[0][0] = 0
        
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
    
        return dp[m][n]

















































        