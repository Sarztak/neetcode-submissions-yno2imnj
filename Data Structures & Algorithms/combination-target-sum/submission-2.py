class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, arr, total):
            if target == total:
                res.append(arr.copy())
                return
            if target < total:
                return 

            for j in range(i, len(nums)):
                arr.append(nums[j])
                dfs(j, arr, total + nums[j])
                arr.pop()
        
        dfs(0, [], 0)

        # res = set(tuple(sorted(r)) for r in res)
        # res = list(list(r) for r in res)
        return res