class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(curr, i):
            if i == len(nums) :
                return curr == target
            return dfs(curr + nums[i], i + 1) + dfs(curr - nums[i], i + 1)

        return dfs(0, 0)