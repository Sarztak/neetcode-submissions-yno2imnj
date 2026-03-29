class Solution:
    def rob(self, nums: List[int]) -> int:
        arr = [0, 0] # to simulate the initial condition of having two dummy houses before the first real houses
        arr.extend(nums)
        n = len(arr)
        dp = [-9999999999] * n
        dp[0] = dp[1] = 0

        for i in range(2, n):
            # here dp[i] - the maximum amount of money that can be robbed from house at index i
            # at each house the robber can decide
            # whether to rob the house or not
            # if he does decide then that is only possible 
            # if the adjacent house at i - 1 was not robbed
            # so the money he makes is dp[i - 2] + arr[i]
            # else he decides to leave the house and move on, in which case he gains nothing dp[i - 1]
            dp[i] = max(dp[i], dp[i - 1], dp[i - 2] + arr[i])
        return dp[-1]