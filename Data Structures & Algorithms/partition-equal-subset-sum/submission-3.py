class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        def dfs(set1, set2):
            if sum(set1) == sum(set2):
                return True
            
            for i in range(len(set2)):
                if dfs(set1 + [set2[i]], set2[:i] + set2[i + 1:]):
                    return True
            
            return False
        
        return dfs([], nums)
        