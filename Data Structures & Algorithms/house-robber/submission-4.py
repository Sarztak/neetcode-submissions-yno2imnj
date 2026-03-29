class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0 # if there are no houses to rob
        if n <= 2:
            return max(nums) # if there is 1 or 2 house to rob then we take maximum
        a, b = nums[0], max(nums[:2])
        for i in range(2, n):
            b, a = max(nums[i] + a, b), b
        return b
        
