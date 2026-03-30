class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-float('inf')] * n
        dp[0] = 1 # a sequence of length one is always increasing
        # dp[i] means the longest length subsequence that includes nums[i]
        # now since it should include nums[i] then I need to find the previous j
        # for which dp[j] is maximum so that I can continue to expand the sequence 
        # forward. with the conditions j < i and nums[j] < nums[i] for strictly increasing
        # this is quite similar to the coin change problem

        for i in range(1, n):
            max_prev_length = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_prev_length = max(max_prev_length, dp[j])
            
            dp[i] = max(dp[i], max_prev_length + 1)

        return max(dp)
        