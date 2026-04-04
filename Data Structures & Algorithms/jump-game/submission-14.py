class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        

        # the disadvantage of greedy solution is that it requires you to be clever 
        # in this case if the max_pos < i then it means that I can't reach i index regardless so return False
        # and at each position you update what max_pos is position to reach so primary track what is your reach and check at each index if you can reach this particular index or not
        # better way to say that first check if given your previous max_pos can the current index i be reach if yes, then update max_pos from the current index i
        if n == 1:
            return True
        
        max_pos = nums[0] # the only position reachable without doing anything is index 0
        for i in range(n):
            if max_pos < i:
                return False
            max_pos = max(max_pos, nums[i] + i)
        
        return True
