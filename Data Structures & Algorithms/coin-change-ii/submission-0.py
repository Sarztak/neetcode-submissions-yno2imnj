class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0]*(amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount + 1):
                print(coin)
                dp[j] += dp[j - coin]
        return dp[amount]