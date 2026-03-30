class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True # represention an empty string

        for j in range(1, n + 1):
            for i in range(j):
                dp[j] = dp[j] or dp[i] and s[i:j] in wordDict
        print(dp) 
        return dp[-1]
        