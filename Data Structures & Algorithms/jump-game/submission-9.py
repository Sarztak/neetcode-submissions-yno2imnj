class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        current_end = 0
        farthest = 0
        for i in range(n - 1):
            farthest = max(farthest, nums[i] + i)
            if i == current_end:
                current_end = farthest
                if current_end >= n - 1:
                    return True
        return False