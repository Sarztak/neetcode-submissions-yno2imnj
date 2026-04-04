class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # the idea with the greedy approach is to ask what is the farthest position that I can reach from my current position
        # for any index i this is i + nums[i] and we compare this with max_pos which is tracked so far and update max_pos 

        if n == 1:
            return True
        
        max_pos = nums[0] # the only position reachable without doing anything is index 0
        for i in range(n):
            if max_pos < i:
                return False
            max_pos = max(max_pos, nums[i] + i)
        
        return True
