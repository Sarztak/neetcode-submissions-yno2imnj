class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        S = sum(nums)

        if S % 2 != 0:
            return False
        
        dp = [[False] * (S//2 + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True 
        
        for i in range(1, n + 1):
            for s in range(1, S//2 + 1):
                dp[i][s] = (dp[i - 1][s - nums[i - 1]] if s >= nums[i - 1] else False) or dp[i - 1][s]

        return dp[-1][-1]