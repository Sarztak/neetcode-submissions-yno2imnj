class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        minJumps = [float('inf')]

        def dfs(index, numJumps):
            if index == n - 1:
                minJumps[0] = min(minJumps[0], numJumps)
            if index > n - 1 or nums[index] == 0:
                return 
            
            steps = nums[index]

            for step_size in range(1, steps + 1):
                dfs(index + step_size, numJumps + 1)

        
        dfs(0, 0)
        return minJumps[0]
        