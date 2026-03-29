class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(index):
            if index >= (len(nums) - 1):
                return True
            steps = nums[index]
            if steps == 0:
                return False
            

            for i in range(1, steps + 1):
                if dfs(index + i):
                    return True
            
            return False

        
        return dfs(0)