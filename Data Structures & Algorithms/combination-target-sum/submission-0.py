class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, subset = set(), []
        def backtrack(t):
            if t == 0:
                res.add(tuple(sorted(subset.copy())))
                return
            for i in nums:
                subset.append(i)
                if t >= i:
                    backtrack(t - i)
                subset.pop()
            
        backtrack(target)
        res = [list(r) for r in res]
        return res
        