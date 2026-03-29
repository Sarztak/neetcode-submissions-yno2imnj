class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n + 1)
        dp[0] = True # because it is always possible to segment an empty string
        # the main idea of any dp is to use the previous solution to the same problem 
        # and then use it to create next solution
        # so we store the solutions to the problem not the calculation or transformation
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]