class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        if s[-1] == '1': 
            return False
        for i in range(1, n):
            dp[i] = any(dp[j] for j in range(max(0, i - maxJump), i - minJump + 1)) if s[i] == '0' else dp[i]
            # if s[i] == '0':
            #     for k in range(minJump, min(i, maxJump) + 1):
            #         dp[i] = dp[i] or dp[i - k]
        return dp[n - 1]