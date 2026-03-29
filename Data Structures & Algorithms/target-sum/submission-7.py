from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache
        def dfs(currSum, i):
            if i == n:
                return int(currSum == target)
            return dfs(currSum + nums[i], i + 1) + dfs(currSum - nums[i], i + 1)
    
        return dfs(0, 0)