class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        nCoins = [0]*(amount + 1)
        nCoins[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                nCoins[i] += nCoins[i - coin]
        return nCoins[-1]