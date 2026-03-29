class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = float('inf') # put minCost = infinity
        n = len(cost) # len of array
        def dfs(k, currCost):
            nonlocal minCost
            # takes two params k which is current position and cost so far
            if k > n - 1:
                minCost = min(minCost, currCost) # we only keep the minimum cost 
                return # end of story
            dfs(k + 1, currCost + cost[k]) # cost to be paid in total to be at k + 1
            dfs(k + 2, currCost + cost[k]) # cost to be paid ....

        dfs(0, 0) # we can start at 0 and no cost 
        dfs(1, 0) # we can start at 1 and no cost

        return minCost # return minCost for all paths travelled
