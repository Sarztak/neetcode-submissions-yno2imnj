class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list = []
        for i in range(len(nums) - k + 1):
            max_list.append(max(nums[i: i + k]))
        return max_list

        