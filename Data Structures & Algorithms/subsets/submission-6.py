class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        n = len(nums)

        def dfs(i):
            res.append(subset.copy())

            for j in range(i, n):
                subset.append(nums[j])

                dfs(j + 1)

                subset.pop()
        
        dfs(0)

        return res