class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = {}
        dp[0] = True
        def dfs(i):
            if i == n - 1:
                return True
            
            end = min(i + nums[i], n - 1)
            
            for j in range(i + 1, end + 1):
                if dfs(j):
                    dp[j] = True
                    return True
            return False
        
        return dfs(0)