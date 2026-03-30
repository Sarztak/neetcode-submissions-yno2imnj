class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True # represention an empty string

        # here the dp[i] means are the first i characters s[:i] segmented or not.
        # therefore dp[0] = True because there is nothing to segmented; empty string is already segmented
        for j in range(1, n + 1):
            for i in range(j):
                dp[j] = dp[j] or dp[i] and s[i:j] in wordDict
        print(dp) 
        return dp[-1]
        