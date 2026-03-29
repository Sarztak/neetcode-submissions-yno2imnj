class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(mask, subset):
            if len(subset) == n:
                res.append(subset)
                return 

            for i in range(n):
                if i in mask:
                    continue
                dfs(mask + [i], subset + [nums[i]])
            
        dfs([], [])

        return res
        