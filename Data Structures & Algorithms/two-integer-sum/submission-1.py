class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = [(nums[i], i) for i in range(len(nums))]

        nums_idx = sorted(nums_idx, key=lambda x: x[0])

        i = 0
        j = len(nums) - 1

        while i < j:
            if nums_idx[i][0] + nums_idx[j][0] == target:
                return [min(nums_idx[i][1], nums_idx[j][1]), max(nums_idx[i][1], nums_idx[j][1])]
            elif nums_idx[i][0] + nums_idx[j][0] < target:
                i += 1
            else:
                j -= 1

        return [-1, -1]  # should not happen