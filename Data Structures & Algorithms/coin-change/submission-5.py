class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount + 1)
        dp[0] = 0 # when amount is zero, we don't need any coin
        for coin in coins:
            for i in range(coin, amount + 1): # this ensures the case when coin is bigger than amount
                dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[amount] if dp[amount] != float('inf') else -1
        