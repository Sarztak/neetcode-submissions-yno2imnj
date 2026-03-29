class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cache = {}

        def dfs(currSum, i):
            if i == n:
                return int(currSum == target)
            if (currSum, i) in cache:
                return cache[(currSum, i)]

            # both currSum and i are important, because that i indicates the number of
            # elements left . 
            # we need to first of all check where there are duplicate computations in 
            # graph, at what state; Here it was for (currSum, i) as a state
            # I did not consider i as a state
            cache[(currSum, i)] = dfs(currSum + nums[i], i + 1) + dfs(currSum - nums[i], i + 1)
            return cache[(currSum, i)]

        return dfs(0, 0)
        
        