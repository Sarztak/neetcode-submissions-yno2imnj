class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(i, subset, total):
            if total == target:
                res.append(subset) 

            for j in range(i, n):
                if total + nums[j] > target:
                    continue

                dfs(j, subset + [nums[j]], total + nums[j])

        dfs(0, [], 0)

        return res       