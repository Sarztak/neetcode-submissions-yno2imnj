class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if nums[i] in subset:
                    continue
                subset.append(nums[i])
                dfs(subset)
                subset.pop()
        dfs([])
        return res
            
        