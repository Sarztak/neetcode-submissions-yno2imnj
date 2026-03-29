class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        pos = 0

        def dfs(i):
            if i == n - 1:
                return True
            
            end = min(nums[i] + i, n - 1)
            for j in range(i + 1, end + 1):
                if dfs(j):
                    return True
            return False
        return dfs(0)

