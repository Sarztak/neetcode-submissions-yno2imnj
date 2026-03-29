class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        # if we choose to rob the first house we do not visit the last house
        a, b1 = nums[0], max(nums[0], nums[1])
        for i in range(2, n - 1):
            b1, a = max(b1, nums[i] + a), b1
        
        # if we choose to rob the last house we start with the second house
        a, b2 = nums[1], max(nums[1], nums[2])
        for i in range(3, n):
            b2, a = max(b2, a + nums[i]), b2
        
        return max(b1, b2)