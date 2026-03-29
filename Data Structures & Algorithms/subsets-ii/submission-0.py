class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = set(), []
        def dfs(start):
            res.add(tuple(sorted(subset.copy())))
            for i in range(start, len(nums)):
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()
        dfs(0)
        res = [list(r) for r in res]
        return res
        