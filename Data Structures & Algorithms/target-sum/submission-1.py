class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def dfs(i, curr):
            if i == n:
                return curr == target
            
            return dfs(i + 1, curr + nums[i]) + dfs(i + 1, curr - nums[i])
        
        return dfs(0, 0)