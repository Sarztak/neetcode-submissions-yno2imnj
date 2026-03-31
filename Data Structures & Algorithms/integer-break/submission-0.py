class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [-float('inf')] * (n + 1)
        dp[0] = dp[1] = 1

        for t in range(2, n + 1):
            for k in range(1, t):
                dp[t] = max(dp[t], dp[t - k] * k, (t - k) * k)
        
        return dp[-1]