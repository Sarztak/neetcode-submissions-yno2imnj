class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        
        # all I need is the sum of True
        if s[-1] == '1': 
            return False
       
        dp = [False] * n
        dp[0] = True

        for i in range(1, min(n, minJump)):
            dp[i] = False # the idea is all position before minJump can't be reached regardless of the value 0/1
        
        for i in range(minJump, min(n, maxJump + 1)):
            dp[i] = (s[i] == '0') # from minJump to maxJump all values where there is a 0 can be reached
        
        k = maxJump + 1
        reachable = sum(dp[k - maxJump: k - minJump]) # keep a count of how many values are true, if this counter hits zero then it means that position cannot be reached
        if maxJump == minJump:
            reachable = int(dp[k - maxJump])

        # print(dp, reachable)
        for i in range(k, n): # now start from the minJump as the first position 
            if reachable > 0 and s[i] == '0':
                dp[i] = True
            
            reachable += int(dp[i - minJump + 1]) # the idea is if this value can be reached then window moves forward otherwise the window stays the same
            reachable -= int(dp[max(0, i - maxJump)]) 
            # print(dp)
    
        return dp[-1]