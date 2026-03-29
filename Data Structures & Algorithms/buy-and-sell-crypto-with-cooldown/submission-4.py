class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        def dfs(day, canBuy):
            if day >= n:
                return 0
            
            if canBuy:
                return max(
                    dfs(day + 1, False) - prices[day],
                    dfs(day + 1, True)
                )

            else:
                return max(
                    dfs(day + 2, True) + prices[day],
                    dfs(day + 1, False)
                )

        return dfs(0, True)


































