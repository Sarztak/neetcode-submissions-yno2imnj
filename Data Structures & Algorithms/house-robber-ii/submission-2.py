class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        arr = [0, 0]
        arr.extend(nums)
        dp = [-float('inf')] * (n + 2)
        dp[0] = dp[1] = 0

        # there solution is simply this start from index 0 or index 1
        # handling circular dependency for each index is hard should not be done

        for i in range(2, n + 1):
            dp[i] = max(dp[i], dp[i - 1], dp[i - 2] + arr[i])

        case1 = dp[n]
        dp = [-float('inf')] * (n + 2)
        dp[0] = dp[1] = dp[2] = 0
        for i in range(3, n + 2):
            dp[i] = max(dp[i], dp[i - 1], dp[i - 2] + arr[i])
        case2 = dp[n + 1]
        return max(case1, case2)