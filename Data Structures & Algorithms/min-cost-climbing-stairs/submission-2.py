class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.extend([0, 0]) # add two extra cost for position n, n + 1
        n = len(cost)
        dp = [float('inf')] * (n) # the length is now original + 2
        dp[0] = dp[1] = 0
        for i in range(2, n):
            dp[i] = min(dp[i], dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return min(dp[-2], dp[-1])
        