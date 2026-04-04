class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True

        for i in range(1, n):
            if s[i] == '0':
                for k in range(minJump, maxJump + 1):
                    if 0 <= k <= i:
                        dp[i] = dp[i] or dp[i - k]
        # print(dp)
        return dp[n - 1]