class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [0]*(amount + 1)
        for i in range(1, amount + 1):
            c = float('inf')
            for coin in coins:
                res = i - coin
                if res < 0 or (res != 0 and dp[res] == 0): # this cover absense of coin
                    continue
                c = min(c, dp[res] + 1)
            if c != float('inf'):
                dp[i] = c
        return dp[-1] if dp[-1] else -1