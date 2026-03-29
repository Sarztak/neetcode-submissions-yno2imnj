class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(arr):
            s = sum(arr)
            if target == s:
                res.append(arr.copy())
                return
            if target < s:
                return

            for n in nums:
                arr.append(n)
                dfs(arr)
                arr.pop()
        
        dfs([])

        res = set(tuple(sorted(r)) for r in res)
        res = list(list(r) for r in res)
        return res