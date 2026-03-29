class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.append(0)
        candidates.sort()
        n = len(candidates)
        res = []

        def dfs(i, subset, total):
            if total == target:
                res.append(subset)

            for j in range(i, n):
                if total + candidates[j] > target or (j > i and candidates[j - 1] == candidates[j]):
                    continue
                
                dfs(j + 1, subset + [candidates[j]], total + candidates[j])
            
        dfs(1, [], 0)

        return res
        